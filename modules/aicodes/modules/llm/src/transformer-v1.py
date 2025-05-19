import tensorflow as tf

def transformer_encoder_layer(d_model, num_heads, dff, dropout_rate=0.1):
    inputs = tf.keras.Input(shape=(None, d_model))  # (batch_size, seq_len, d_model)

    # Multi-head Self-Attention
    attention_output = tf.keras.layers.MultiHeadAttention(num_heads=num_heads, key_dim=d_model)(inputs, inputs)
    attention_output = tf.keras.layers.Dropout(dropout_rate)(attention_output)
    out1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)(inputs + attention_output)

    # Feed Forward
    ffn = tf.keras.Sequential([
        tf.keras.layers.Dense(dff, activation='relu'),  # Expande dimensão
        tf.keras.layers.Dense(d_model)  # Volta para d_model
    ])
    ffn_output = ffn(out1)
    ffn_output = tf.keras.layers.Dropout(dropout_rate)(ffn_output)
    out2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)(out1 + ffn_output)

    return tf.keras.Model(inputs=inputs, outputs=out2)

# Exemplo de uso
encoder_layer = transformer_encoder_layer(d_model=64, num_heads=4, dff=256)
dummy_input = tf.random.uniform((1, 10, 64))  # (batch, seq_len, d_model)
output = encoder_layer(dummy_input)
print("Output shape:", output.shape)
