struct token_metadata {
    int line;
    char *str;
    int integer_value;
    float float_value;
    int type;
    char * code;
};

typedef struct token_metadata token_metadata;