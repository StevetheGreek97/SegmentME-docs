def get_text(section
):
    """
    Get the text for a given section from the text.yaml file.
    
    Args:
        section (str): The section to retrieve text for.
        
    Returns:
        str: The text for the specified section.
    """
    import yaml
    from pathlib import Path

    # Load the YAML file
    text_file = Path(__file__).parent.parent / 'assets' / 'text.yaml'
    with open(text_file, 'r') as file:
        text_data = yaml.safe_load(file)

    # Return the requested section
    return text_data.get(section, '')

if __name__ == "__main__":
    # Example usage
    section = 'intro'
    text = get_text(section)
    print(f"Text for section '{section}': {text}")
    # Output: Text for section 'intro': SegmentME is a powerful image annotation and segmentation tool designed for high-throughput phenotyping, object instance analysis, and smart annotation workflows using models like