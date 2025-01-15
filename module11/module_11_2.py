def introspection_info(obj):
    """
    Conduct introspection on the given object to determine its type,
    attributes, methods, module, and other properties.

    :param obj: Any object to inspect.
    :return: A dictionary with details about the object.
    """
    info = {
        'type': type(obj).__name__,
        'module': getattr(obj, '__module__', 'built-in'),
        'attributes': [],
        'methods': []
    }

    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            info['methods'].append(attr)
        else:
            info['attributes'].append(attr)

    if hasattr(obj, '__doc__'):
        info['doc'] = obj.__doc__.strip() if obj.__doc__ else None

    return info


number_info = introspection_info(42)
print(number_info)
