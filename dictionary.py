from foundry_local_sdk import Configuration, FoundryLocalManager
from foundry_local_sdk.configuration import LogLevel

config = Configuration(
    app_name="MyApp",
    model_cache_dir="/path/to/cache",     # optional
    log_level=LogLevel.INFORMATION,        # optional (default: Warning)
)
FoundryLocalManager.initialize(config)
manager = FoundryLocalManager.instance

catalog = manager.catalog

# List all models in the catalog
models = catalog.list_models()

# Get a specific model by alias
model = catalog.get_model("qwen2.5-0.5b")

# Get a specific variant by ID
variant = catalog.get_model_variant("qwen2.5-0.5b-instruct-generic-cpu:4")

# List locally cached models
cached = catalog.get_cached_models()

# List currently loaded models
loaded = catalog.get_loaded_models()