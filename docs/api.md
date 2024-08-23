# API Documentation

## Overview

This document provides a comprehensive guide to the APIs exposed by our LLM-Powered Microservice. The API follows RESTful principles and uses JSON for request and response bodies.

## Base URL

All API endpoints are relative to the base URL:

```
https://api.example.com/v1
```

## Authentication

Most endpoints require authentication. Use Bearer token authentication by including an `Authorization` header in your requests:

```
Authorization: Bearer <your_access_token>
```

## Endpoints

### 1. Text Generation

Generate text based on a given prompt.

- **URL:** `/generate`
- **Method:** POST
- **Auth required:** Yes
- **Request Body:**
  ```json
  {
    "prompt": "Once upon a time",
    "max_tokens": 100,
    "temperature": 0.7
  }
  ```
- **Success Response:**
  - **Code:** 200
  - **Content:**
    ```json
    {
      "generated_text": "Once upon a time, in a land far away...",
      "tokens_used": 20
    }
    ```
- **Error Response:**
  - **Code:** 400
  - **Content:** `{ "detail": "Invalid input parameters" }`

### 2. Text Completion

Complete a given text prompt.

- **URL:** `/complete`
- **Method:** POST
- **Auth required:** Yes
- **Request Body:**
  ```json
  {
    "prompt": "The quick brown fox",
    "max_tokens": 50,
    "temperature": 0.5
  }
  ```
- **Success Response:**
  - **Code:** 200
  - **Content:**
    ```json
    {
      "completed_text": "The quick brown fox jumps over the lazy dog.",
      "tokens_used": 15
    }
    ```
- **Error Response:**
  - **Code:** 400
  - **Content:** `{ "detail": "Invalid input parameters" }`

### 3. Sentiment Analysis

Analyze the sentiment of a given text.

- **URL:** `/analyze/sentiment`
- **Method:** POST
- **Auth required:** Yes
- **Request Body:**
  ```json
  {
    "text": "I love this product! It's amazing."
  }
  ```
- **Success Response:**
  - **Code:** 200
  - **Content:**
    ```json
    {
      "sentiment": "positive",
      "confidence": 0.95
    }
    ```
- **Error Response:**
  - **Code:** 400
  - **Content:** `{ "detail": "Text too short for analysis" }`

## Error Handling

All endpoints may return the following error responses:

- 400 Bad Request: Invalid input data
- 401 Unauthorized: Missing or invalid authentication token
- 403 Forbidden: Insufficient permissions
- 429 Too Many Requests: Rate limit exceeded
- 500 Internal Server Error: Unexpected server error

Error responses will include a JSON body with a `detail` field explaining the error.

## Rate Limiting

API requests are subject to rate limiting. The current limits are:

- 100 requests per minute for authenticated users
- 10 requests per minute for unauthenticated users

Rate limit information is included in the response headers:

- `X-RateLimit-Limit`: The number of allowed requests in the current period
- `X-RateLimit-Remaining`: The number of remaining requests in the current period
- `X-RateLimit-Reset`: The time at which the current rate limit window resets

## Versioning

The API is versioned using URL path versioning. The current version is `v1`. When breaking changes are introduced, a new version (e.g., `v2`) will be created, and the old version will be maintained for a deprecation period.

For questions or support regarding the API, please contact our developer support team at codewiththompson@gmail.com.