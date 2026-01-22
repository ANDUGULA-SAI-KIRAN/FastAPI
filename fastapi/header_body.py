from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI(title="Bearer Token Auth Demo")

# -------- Security setup --------
security = HTTPBearer()

# -------- Tokens setup --------
# In real apps, these would be JWTs. For simplicity, we use strings.
TOKENS = {
    "token_all": "user1-token",    # Access to all endpoints
    "token_one": "user2-token",    # Access to only one endpoint
}

# -------- Dependency to verify token and permissions --------
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token not in TOKENS.values():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing token"
        )
    # Determine user and permissions
    if token == "user1-token":
        return {"user": "user1", "access": "all"}
    elif token == "user2-token":
        return {"user": "user2", "access": "limited"}

# -------- Endpoints --------

@app.get("/public")
def public_endpoint():
    return {"message": "Anyone can access this endpoint, no token needed."}

@app.get("/protected")
def protected_endpoint(current_user: dict = Depends(get_current_user)):
    # Both tokens can access
    return {
        "message": f"Hello {current_user['user']}, you can access this endpoint.",
        "access_level": current_user['access']
    }

@app.get("/restricted")
def restricted_endpoint(current_user: dict = Depends(get_current_user)):
    # Only token_all can access
    if current_user["access"] != "all":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access to this endpoint"
        )
    return {
        "message": f"Hello {current_user['user']}, this is a restricted endpoint.",
        "access_level": current_user['access']
    }
