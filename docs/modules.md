# Module Overview

This document provides a summary of the project modules after refactor.

## Modules

### Auth Module
- Handles login, logout, token refresh.
- Provides RBAC (role-based access control).

### Data Processor
- Executes business logic workflows.
- Designed for high concurrency and reliability.

### API Gateway
- Centralizes API routing.
- Implements caching and throttling.

### Database Layer
- Responsible for persistent storage.
- Uses ORM for database interactions.

### Utilities
- Shared helpers for logging, configuration, and error handling.
