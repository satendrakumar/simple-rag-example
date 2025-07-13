# simple-rag-example
A minimal Retrieval Augmented Generation (RAG) API to answer climate-related questions.

## Usage

The API exposes a single endpoint for question answering:

**POST** `/v1/api/rag`  
**Body:**

### Local setup:
```shell
git clone https://github.com/satendrakumar/simple-rag-example.git
cd simple-rag-example
uv sync
python main.py
```


### Rest API Request and response:
```shell
1. Request:
    curl --location 'http://localhost:8000/v1/api/rag' \
    --header 'accept: application/json' \
    --header 'Content-Type: application/json' \
    --data '{
      "question": "How much has global temperature increased since pre-industrial times?"
    }'

  Response:
    {
        "response": "**Answer:**\nSince pre-industrial times, global temperature has increased by approximately 1.1°C to 1.3°C."
    }
2. Request:
    curl --location 'http://localhost:8000/v1/api/rag' \
    --header 'accept: application/json' \
    --header 'Content-Type: application/json' \
    --data '{
      "question": "Is sea level rise avoidable? When will it stop?"
    }'
    Reponse: 
    {
    "response": "In the IPCC 2023 Synthesis Report, WGII SPM B.3.1 states:\n\nSea level rise is unavoidable for centuries to millennia due to continuing deep ocean warming and ice sheet melt, and sea levels will remain elevated for thousands of years (high-conﬁdence). Global mean sea level rise will continue in the 21st century (virtually certain), with projected regional relative sea level rise within 20% of the global mean along two-thirds of the global coastline (medium-conﬁdence). The magnitude, the rate, the timing of threshold\nexceedances, and the long-term commitment of sea level rise depend on emissions, with higher emissions leading to greater and faster rates of sea level rise. Due to relative sea level rise, extreme sea level events that occurred once per century in the recent past are projected to occur at least annually at more than half of all tide gauge locations by 2100 123 This outcome is characterized by deep uncertainty: Its likelihood defies quantitative assessment but is considered due to its high potential impact. {WGI Box TS.1; WGII Cross-Chapter Box DEEP}\n\nBased on this information, it is clear that sea level rise is unavoidable for centuries to millennia, and it will continue for thousands of years, with projected regional relative sea level rise within 20% of the global mean. The magnitude, the rate, the timing of threshold exceedances, and the long-term commitment of sea level rise depend on emissions, and higher emissions lead to greater and faster rates of sea level rise. However, the probability and rate of sea level rise is uncertain due to deep uncertainty, and it is characterized by high potential impact. Consequently, sea level rise will continue to impact coastal ecosystems, people, and infrastructure in the 21st century, and it is likely to be chronic high tide flooding and extreme flooding during storms. The range of sea level rise varies depending on the emissions scenario, and it is between 0.15 to 0.23 m under the very low GHG emissions scenario and 0.20 to 0.29 m under the very high GHG emissions scenario. The sea level rise by 2100 depends on the emissions scenario, and it is between 0.28 to 0.55 m under SSP1-1.9 and 0.63 to 1.01 m under SSP5-8.5. It is also projected"
    }
    
3. Request:
    curl --location 'http://localhost:8000/v1/api/rag' \
    --header 'accept: application/json' \
    --header 'Content-Type: application/json' \
    --data '{
      "question": "How is climate change affecting biodiversity?"
    }'
    Reponse:
    {
    "response": "Climate change is affecting biodiversity in a variety of ways. As temperatures rise, many species are shifting their ranges to higher latitudes or elevations, which can lead to habitat loss and fragmentation. This can result in the loss of biodiversity in some regions, as well as in the loss of species that are unable to adapt to the changing conditions.\n\nIn addition, changes in temperature and precipitation patterns are affecting the timing and distribution of species' life cycles. This can lead to mismatches between the availability of food and the needs of species, as well as changes in the timing of breeding and migration. These changes can have cascading effects on ecosystems, as species interactions are disrupted and new relationships are formed.\n\nClimate change can also affect the ability of species to adapt to changing conditions. Some species may not be able to adjust their behavior or physiology in time to cope with new conditions, leading to declines in populations and the loss of genetic diversity.\n\nOverall, climate change is having significant impacts on biodiversity, and these impacts are likely to be far-reaching and long-lasting."
    }