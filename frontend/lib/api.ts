import axios from "axios";

export const analyzeDrug = async (
  drug_name: string,
  review: string
) => {
  const response = await axios.post(
    "http://127.0.0.1:8000/predict",
    {
      drug_name,
      review,
    }
  );

  return response.data;
};