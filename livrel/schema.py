schema_text = {
    'texte': {
        'type': 'string',
        'required': True,
        'nullable': False,
        'empty': False
    }
}

schema_stage_direction = {
    'didascalie': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'texte': {
                    'type': 'string',
                    'nullable': True,
                    'empty': False
                },
                'typologie': {
                    'type': 'string',
                    'dependencies': 'texte',
                    'nullable': True,
                    'empty': False
                }
            }
        },
        'required': False,
        'nullable': True,
        'empty': False
    }
}

schema_scene = {
    'scene': {
        'type': 'integer',
        'required': True,
        'nullable': False,
        'empty': False
    },
    'personnages': {
        'type': 'list',
        'schema': {
            'type': 'string',
            'required': True,
            'nullable': False,
            'empty': False
        },
        'required': True,
        'nullable': False,
        'empty': False
    }
}

drama = {
    'personnage': {
        'type': 'string',
        'required': True,
        'nullable': False,
        'empty': False
    },
    **schema_stage_direction
}
