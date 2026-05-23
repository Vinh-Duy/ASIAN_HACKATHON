# Frontend Deployment Guide (Render)

## Step 1: Create Static Site on Render
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **+ New** → **Static Site**
3. Connect your GitHub repository

## Step 2: Configure Settings

| Field | Value |
|-------|-------|
| **Name** | `agridrop-frontend` |
| **Branch** | `main` |
| **Root Directory** | `frontend` |
| **Build Command** | `npm install && npm run build` |
| **Publish Directory** | `dist` |

## Step 3: Add Environment Variable
After creating the service:
1. Go to **Settings** → **Environment**
2. Add new environment variable:
   - **Key**: `VITE_API_URL`
   - **Value**: `https://your-backend-name.onrender.com/api`
   
   *(Replace `your-backend-name` with your actual backend service name)*

## Step 4: Deploy Backend First! ⚠️
Make sure your backend is deployed first and get the URL:
- Deploy backend service on Render
- Get the URL from Render dashboard (e.g., `https://agridrop-backend.onrender.com`)
- Use that URL for the `VITE_API_URL` environment variable

## Example:
If your backend URL is: `https://agridrop-backend-xyz123.onrender.com`

Then set:
```
VITE_API_URL=https://agridrop-backend-xyz123.onrender.com/api
```

## Local Testing
For local development, use `.env` file:
```
VITE_API_URL=http://localhost:8000/api
```

## Files Updated
- `vite.config.js` - Now uses `VITE_API_URL` environment variable
- `frontend/src/services/api.js` - Centralized API client
- `frontend/.env` - Local development config
- `frontend/.env.example` - Template for production
