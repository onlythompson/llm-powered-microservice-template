import os

def create_directory_structure(base_path):
    structure = {
        'my_fastapi_microservice': {
            'src': {
                'application': {
                    'chains': {
                        '__init__.py': '',
                        'base_chain.py': '',
                        'specific_chains': {
                            '__init__.py': '',
                            'example_chain.py': ''
                        }
                    },
                    'models': {
                        '__init__.py': '',
                        'base_model.py': '',
                        'model_factory.py': ''
                    },
                    'prompt_management': {
                        '__init__.py': '',
                        'prompt_template.py': '',
                        'prompt_repository.py': ''
                    },
                    'services': {
                        '__init__.py': '',
                        'llm_orchestrator.py': '',
                        'usage_tracker.py': ''
                    }
                },
                'core': {
                    '__init__.py': '',
                    'config.py': '',
                    'exceptions.py': '',
                    'dependencies.py': '',
                    'cross_cutting.py': ''
                },
                'domain': {
                    '__init__.py': '',
                    'llm_request.py': '',
                    'llm_response.py': ''
                },
                'infrastructure': {
                    'cache': {
                        '__init__.py': '',
                        'redis_cache.py': ''
                    },
                    'llm_providers': {
                        '__init__.py': '',
                        'base.py': '',
                        'openai.py': '',
                        'anthropic.py': ''
                    }
                },
                'presentation': {
                    'api': {
                        '__init__.py': '',
                        'routes': {
                            '__init__.py': '',
                            'llm_routes.py': ''
                        },
                        'schemas': {
                            '__init__.py': '',
                            'llm_request.py': '',
                            'llm_response.py': ''
                        }
                    }
                },
                '__init__.py': '',
                'main.py': ''
            },
            'tests': {
                'unit': {
                    'application': {
                        'test_prompt_management.py': '',
                        'test_llm_orchestrator.py': ''
                    },
                    'infrastructure': {
                        'test_cache.py': '',
                        'test_llm_providers.py': ''
                    }
                },
                'integration': {
                    'test_api_endpoints.py': ''
                },
                'conftest.py': ''
            },
            'docs': {
                'api.md': '',
                'architecture.md': '',
                'deployment.md': ''
            },
            'k8s': {
                'deployment.yaml': '',
                'service.yaml': '',
                'configmap.yaml': ''
            },
            '.env.example': '',
            '.gitignore': '',
            'README.md': '',
            'requirements.txt': '',
            'setup.py': ''
        }
    }

    def create_structure(current_path, structure):
        for name, content in structure.items():
            path = os.path.join(current_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            else:
                with open(path, 'w') as f:
                    f.write(content)

    create_structure(base_path, structure)
    print(f"Directory structure created at {base_path}")

if __name__ == "__main__":
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set the base path to the parent directory of the script
    base_path = os.path.dirname(script_dir)
    
    create_directory_structure(base_path)