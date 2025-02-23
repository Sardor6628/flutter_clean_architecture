import os

def create_folder_structure(base_path):
    folders = [
        "core/error",
        "core/usecases",
        "core/utils",
        "core/network",
        "core/database",
        "core/theme",
        "core/di",
        "features/feature_name/domain/entities",
        "features/feature_name/domain/repositories",
        "features/feature_name/domain/usecases",
        "features/feature_name/data/models",
        "features/feature_name/data/datasources",
        "features/feature_name/data/repositories",
        "features/feature_name/presentation/pages",
        "features/feature_name/presentation/widgets",
        "features/feature_name/presentation/cubit",  # or use 'bloc' if using Bloc
        "features/feature_name/presentation/controllers",
        "routes",
        "l10n",
        "config",
        "env"
    ]
    
    files = {
        "main.dart": "void main() => runApp(App());",
        "app.dart": "// App initialization and routing",
        "core/error/failures.dart": "// Define failure classes",
        "core/usecases/usecase.dart": "// Define base use case",
        "core/utils/helpers.dart": "// Utility functions",
        "core/network/api_client.dart": "// API client setup",
        "core/database/db_helper.dart": "// Database setup",
        "core/theme/app_theme.dart": "// Theme setup",
        "core/di/injection.dart": "// Dependency injection setup",
        "features/feature_name/domain/entities/example_entity.dart": "// Define entity",
        "features/feature_name/domain/repositories/example_repository.dart": "// Define repository interface",
        "features/feature_name/domain/usecases/get_example.dart": "// Define use case",
        "features/feature_name/data/models/example_model.dart": "// Define data model",
        "features/feature_name/data/datasources/example_remote_data_source.dart": "// Define remote data source",
        "features/feature_name/data/repositories/example_repository_impl.dart": "// Implement repository",
        "features/feature_name/presentation/pages/example_page.dart": "// Define UI page",
        "features/feature_name/presentation/widgets/example_widget.dart": "// Define reusable widget",
        "features/feature_name/presentation/cubit/example_cubit.dart": "// Define Cubit for state management",
        "features/feature_name/presentation/controllers/example_controller.dart": "// Define controller",
        "routes/app_routes.dart": "// Define app routes",
        "l10n/app_localizations.dart": "// Localization setup",
        "config/app_config.dart": "// App-wide configurations",
        "env/dev.env": "// Development environment variables",
        "env/prod.env": "// Production environment variables",
    }
    
    # Create folders
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
    
    # Create files with initial content
    for file, content in files.items():
        file_path = os.path.join(base_path, file)
        with open(file_path, "w") as f:
            f.write(content)
    
    print("Flutter Clean Architecture structure created successfully!")

if __name__ == "__main__":
    base_directory = input("Enter the project base directory: ")
    create_folder_structure(base_directory)
