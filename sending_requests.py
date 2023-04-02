import json
import requests
url="http://127.0.0.1:8000/breast_cancer_prediction"
 
input_data={
"radius_mean":    17.990000,
"texture_mean":   10.380000,
"perimeter_mean":              122.800000,
"area_mean":                  1001.000000,
"smoothness_mean":               0.118400,
"compactness_mean":              0.277600,
"concavity_mean":                0.300100,
"concave_points_mean":           0.147100,
"symmetry_mean":                 0.241900,
"fractal_dimension_mean":        0.078710,
"radius_se":                     1.095000,
"texture_se":                    0.905300,
"perimeter_se":                  8.589000,
"area_se":                     153.400000,
"smoothness_se":                 0.006399,
"compactness_se":                0.049040,
"concavity_se":                  0.053730,
"concave_points_se":             0.015870,
"symmetry_se":                   0.030030,
"fractal_dimension_se":          0.006193,
"radius_worst":                 25.380000,
"texture_worst":                17.330000,
"perimeter_worst":            184.600000,
"area_worst":                 2019.000000,
"smoothness_worst":              0.162200,
"compactness_worst":            0.665600,
"concavity_worst":               0.711900,
"concave_points_worst":          0.265400,
"symmetry_worst":                0.460100,
"fractal_dimension_worst":       0.118900
}
json_data=json.dumps(input_data)
print(json_data)
response=requests.post(url,data=json_data)
print(response.text)

