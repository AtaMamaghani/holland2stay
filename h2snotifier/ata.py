import requests
import json

url = "https://api.holland2stay.com/graphql/"

payload = json.dumps({
  "operationName": "GetCategories",
  "variables": {
    "currentPage": 1,
    "id": "Nw==",
    "filters": {
      "available_to_book": {
        "in": [
          "179",
          "336"
        ]
      },
      "city": {
        "in": [
          "619"
        ]
      },
      "category_uid": {
        "eq": "Nw=="
      }
    },
    "pageSize": 30,
    "sort": {
      "available_startdate": "ASC"
    }
  },
  "query": "            query GetCategories($id: String!, $pageSize: Int!, $currentPage: Int!, $filters: ProductAttributeFilterInput!, $sort: ProductAttributeSortInput) {              categories(filters: {category_uid: {in: [$id]}}) {                items {                  uid                  ...CategoryFragment                  __typename                }                __typename              }              products(                pageSize: $pageSize                currentPage: $currentPage                filter: $filters                sort: $sort              ) {                ...ProductsFragment                __typename              }            }            fragment CategoryFragment on CategoryTree {              uid              meta_title              meta_keywords              meta_description              __typename            }            fragment ProductsFragment on Products {              items {                name                sku                city                url_key                available_to_book                available_startdate                building_name                finishing                living_area                no_of_rooms                resident_type                offer_text_two                offer_text                maximum_number_of_persons                type_of_contract                price_analysis_text                allowance_price                floor                basic_rent                lumpsum_service_charge                inventory                caretaker_costs                cleaning_common_areas                energy_common_areas                allowance_price                small_image {                  url                  label                  position                  disabled                  __typename                }                thumbnail {                  url                  label                  position                  disabled                  __typename                }                image {                  url                  label                  position                  disabled                  __typename                }                media_gallery {                  url                  label                  position                  disabled                  __typename                }                price_range {                  minimum_price {                    regular_price {                      value                      currency                      __typename                    }                    final_price {                      value                      currency                      __typename                    }                    discount {                      amount_off                      percent_off                      __typename                    }                    __typename                  }                  maximum_price {                    regular_price {                      value                      currency                      __typename                    }                    final_price {                      value                      currency                      __typename                    }                    discount {                      amount_off                      percent_off                      __typename                    }                    __typename                  }                  __typename                }                __typename              }              page_info {                total_pages                __typename              }              total_count              __typename            }        "
})
headers = {
    'authority': 'api.holland2stay.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # Random modern browser user agent
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'origin': 'https://holland2stay.com',
    'referer': 'https://holland2stay.com/',
}

session = requests.Session()

# First make a GET request to establish cookies
session.get("https://holland2stay.com/", headers=headers)

# Now make the POST request with established cookies
response = session.post(url, headers=headers, data=payload)

print(response.status_code)
print(response.text)