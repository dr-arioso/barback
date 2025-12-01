
def main():
    import argparse
    from core.resolvers import ProductResolver, BottleResolver

    AVAILABLE_RESOLVERS = {
        "bottle": BottleResolver,
        # Add future resolvers here
    }

    parser = argparse.ArgumentParser()
    parser.add_argument("--resolver", type=str, default="bottle", help="Resolver to use")
    args = parser.parse_args()

    resolver_name = args.resolver.lower()
    resolver_cls = AVAILABLE_RESOLVERS.get(resolver_name)
    if resolver_cls is None:
        print(f"Unknown resolver '{resolver_name}', using default BottleResolver.")
        resolver_cls = BottleResolver

    resolver: ProductResolver = resolver_cls()

    print(f"Initialized resolver: {resolver_cls.__name__}")

if __name__ == "__main__":
    main()
