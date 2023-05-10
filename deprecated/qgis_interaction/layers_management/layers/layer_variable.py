class layerVariables:
    def __init__(
        self,
        layer_style,
        layer_type,
        layer_group=None,
        layer_themes=[],
        layer_name=None,
        layer_expression=None,
        layer_source=None,
        query=None,
        add_visible=True,
        layer_name_format_string=None,
    ):
        self.layer_name_format_string = layer_name_format_string
        self.layer_name = layer_name
        self.layer_expression = layer_expression
        self.layer_group = layer_group
        self.layer_style = layer_style
        self.layer_type = layer_type
        self.layer_source = layer_source
        self.layer_themes = layer_themes
        self.query = query
        self.add_visible = add_visible
