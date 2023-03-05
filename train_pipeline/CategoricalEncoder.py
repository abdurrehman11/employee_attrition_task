import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import joblib

class CategoricalEncoder:
    def __init__(
            self, 
            categories='auto', 
            sparse_output=False, 
            handle_unknown='error', 
            ohe_path=None,
            target_enc_path=None,
            categorical_cols=None, 
            target_col=None
        ):
        self.encoder = OneHotEncoder(categories=categories, sparse_output=sparse_output, handle_unknown=handle_unknown)
        self.trg_encoder = LabelEncoder()
        self.ohe_path = ohe_path
        self.target_enc_path = target_enc_path
        self.categorical_cols = categorical_cols
        self.target_col = target_col

    def fit_transform(self, data):
        if self.categorical_cols is None:
            raise ValueError('No categorical columns specified')

        # Split the data into categorical and numerical columns
        categorical_data = data[self.categorical_cols]
        numerical_data = data.drop(columns=self.categorical_cols + [self.target_col])

        # Fit and transform the categorical data using the encoder
        encoded_data = pd.DataFrame(self.encoder.fit_transform(categorical_data))
        encoded_data.columns = self.encoder.get_feature_names_out(categorical_data.columns)
        
        target_encoded = pd.DataFrame(self.trg_encoder.fit_transform(data[self.target_col]))
        target_encoded.columns = [self.target_col]

        # Concatenate the encoded categorical data with the original numerical data
        encoded_data = pd.concat([encoded_data, numerical_data, target_encoded], axis=1)

        if self.ohe_path:
            joblib.dump(self.encoder, self.ohe_path)
            print(f"Saved ohe to {self.ohe_path}")
            # with open(self.ohe_path, 'wb') as f:
            #     pickle.dump(self.encoder, f)

        if self.target_enc_path:
            joblib.dump(self.trg_encoder, self.target_enc_path)
            print(f"Saved target_encoder to {self.target_enc_path}")
            
        return encoded_data