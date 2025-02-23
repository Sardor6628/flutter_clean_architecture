# Flutter Clean Architecture Folder Structure

This script creates a **Clean Architecture** folder structure for a Flutter project. It sets up directories and necessary placeholder files to maintain separation of concerns and improve maintainability.

## Folder Structure

```
lib/
│── core/
│   ├── error/
│   ├── usecases/
│   ├── utils/
│   ├── network/
│   ├── database/
│   ├── theme/
│   ├── di/
│
│── features/
│   ├── feature_name/
│   │   ├── domain/
│   │   │   ├── entities/
│   │   │   ├── repositories/
│   │   │   ├── usecases/
│   │   │
│   │   ├── data/
│   │   │   ├── models/
│   │   │   ├── datasources/
│   │   │   ├── repositories/
│   │   │
│   │   ├── presentation/
│   │   │   ├── pages/
│   │   │   ├── widgets/
│   │   │   ├── cubit/  # or bloc/
│   │   │   ├── controllers/
│
│── routes/
│── l10n/
│── config/
│── env/
│── main.dart
│── app.dart
```

## Explanation

- **core/**: Contains shared functionality like error handling, theme setup, network clients, database configurations, and dependency injection.
- **features/**: Each feature has a separate folder with its **domain**, **data**, and **presentation** layers.
  - **domain/**: Defines business rules and repository interfaces.
  - **data/**: Implements repositories, data models, and sources (remote/local).
  - **presentation/**: Contains UI-related components (pages, widgets, state management).
- **routes/**: Defines application navigation.
- **l10n/**: Handles localization.
- **config/**: Stores global configuration settings.
- **env/**: Environment variables for different build stages.
- **main.dart**: Entry point of the application.
- **app.dart**: Handles app initialization and routing.

## Usage

Run the Python script and specify the base directory to generate this structure automatically.

