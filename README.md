# simple-rag-example
A minimal Retrieval Augmented Generation (RAG) API to answer climate-related questions from [Climate Change 2023 Synthesis Report](https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_LongerReport.pdf) 

## Prerequisites

Before getting started, ensure you have the following installed:

- **Python 3.11 or above** 
- **uv** (Python package management, install with `pip install uv` if needed)




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
       "enable_thinking": "True"
    }'

  Response:
    {
    "response": "Global surface temperatures have risen by **1.1°C since the pre-industrial baseline (1850–1900)**, as reported in the IPCC 2023 Synthesis Report. This increase is **highly confident** and reflects the cumulative impact of human-driven greenhouse gas emissions. The warming has accelerated since the 1970s, with ocean warming and sea level rise contributing significantly to the overall climate system changes. While uncertainties exist in long-term projections, the 1.1°C threshold underscores the urgency of addressing climate change to mitigate its impacts on ecosystems, economies, and societies.",
    "thinking": "<think>\nOkay, the user is asking how much global temperature has increased since pre-industrial times. Let me check the provided IPCC 2023 synthesis report.\n\nThe report states that global surface temperature has reached 1.1°C above 1850-1900 in 2011-2020. That's a key point. But I need to make sure about the exact figure. The report mentions 1.1°C, but I should check if there's a more precise value. Wait, the user might be looking for the exact number, so I should mention the 1.1°C figure. Also, the report talks about the increase since 1850-1900, so that's the baseline. \n\nI should note that the increase is 1.1°C, but the report also mentions that the warming is ongoing. The user might want to know the current status, so including the 2011-2020 data is important. Also, the report emphasizes that this is a 1.1°C increase, which is a significant figure. \n\nI need to make sure the response is clear and concise, under 512 tokens. Avoid jargon, explain that the 1.1°C is the current figure, and mention the confidence level. Also, note that this is the latest data from the report. \n\nWait, the user might also be interested in the rate of increase. The report mentions that the rate of warming has accelerated, but the exact rate isn't given here. The question is about the total increase, not the rate. So focus on the 1.1°C figure. \n\nCheck if there's any uncertainty mentioned. The report says \"high confidence\" in the 1.1°C figure. So the answer should state that the increase is 1.1°C since 1850-1900, with high confidence. Also, mention that this is the current state as per the report. \n\nI should structure the response to first state the 1.1°C figure, then explain the confidence level, and mention the context of the increase. Keep it under the token limit.\n</think>"
    }
2. Request:
    curl --location 'http://localhost:8000/v1/api/rag' \
        --header 'accept: application/json' \
        --header 'Content-Type: application/json' \
        --data '{
          "question": "Is sea level rise avoidable? When will it stop?",
          "enable_thinking": "False"
      
    }'
    Reponse: 
    {
        "response": "Sea level rise is **not avoidable** under current climate trajectories, as it is driven by warming oceans and ice sheet melt. The IPCC emphasizes that rising global temperatures will continue to cause sea levels to rise for centuries, with projections showing a rise of 2 to 3 meters by 2100 and potentially up to 6 meters by 2100 in high-emission scenarios. \n\nThe **rate and magnitude** of sea level rise depend on emissions, with higher emissions leading to faster and greater increases. While some regions may experience slower rises, the overall trend is irreversible. \n\nSea level rise will **not stop** in the near future, and its impacts will intensify as warming continues. Coastal communities, ecosystems, and infrastructure will face increasing risks, including flooding, erosion, and displacement. \n\nThe **likelihood of avoiding significant rise** depends on limiting global warming to 1.5°C, but even with this goal, sea levels will continue to rise for millennia. \n\n**Action is critical** to reduce emissions and slow sea level rise, but the reality is that it is a long-term, irreversible process.",
        "thinking": ""
    }
    
3. Request:
    curl --location 'http://localhost:8000/v1/api/rag' \
    --header 'accept: application/json' \
    --header 'Content-Type: application/json' \
    --data '{
      "question": "How is climate change affecting biodiversity?",
       "enable_thinking": "False"
    }'
    Reponse:
    {
        "response": "Climate change is significantly impacting biodiversity through multiple pathways. It is causing species to shift poleward or to higher elevations, with approximately half of the species assessed globally moving in response to warming (very high confidence). However, these shifts are often insufficient to help species cope with recent climate change, leading to local losses and mass mortality events, particularly in terrestrial and marine ecosystems (very high confidence). \n\nChanges in precipitation patterns, ocean acidification, and sea level rise are altering habitats and food webs, pushing some ecosystems toward irreversibility, such as the loss of glaciers and Arctic ecosystems due to permafrost thaw (high confidence). Additionally, extreme weather events and land degradation are exacerbating biodiversity loss, especially in coastal and dryland regions.\n\nWhile some species may adapt, the pace of climate change is outpacing biological responses, leading to increased extinction risks. Climate change also disrupts ecosystems, reducing resilience and threatening the stability of ecosystems services that support human well-being. \n\nDespite these challenges, many species are showing resilience, and conservation efforts can help mitigate the worst impacts. The goal is to protect biodiversity while adapting to a changing climate.",
        "thinking": ""
    }