import requests

def scrap_twitter(userid):
    url = f"https://api.twitter.com/graphql/ns5lx7OYUtNZ46KtFoVAIw/UserTweets?variables=%7B%22userId%22%3A%22{userid}%22%2C%22count%22%3A40%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%7D&features=%7B%22responsive_web_twitter_blue_verified_badge_is_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Afalse%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22vibe_api_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22freedom_of_speech_not_reach_appeal_label_enabled%22%3Afalse%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Afalse%2C%22interactive_text_enabled%22%3Atrue%2C%22responsive_web_text_conversations_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D"
    payload={}
    headers = {
    'authority': 'api.twitter.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'cookie': 'personalization_id="v1_UP7A08DDAf3uag6d0HQZ/g=="; guest_id_marketing=v1%3A167170920206934570; guest_id_ads=v1%3A167170920206934570; guest_id=v1%3A167170920206934570; _gid=GA1.2.1674848371.1676208564; kdt=J09jIwSyun8a2lbJGHwlXRlSpzgfgfuS6c48M4zG; auth_token=bee1e48ab998c8554e293739ab290a2485877ede; ct0=a943dc006afeb4885c95234b7efacb4a36bfecf002110b930c465fd02e62da33105679d68812f38cfffd1988d669a9266181b6f2aa8f8e8bd32316ca70758cbd75a83e934889ad892f1d48e66e518a7f; twid=u%3D735256350708633600; des_opt_in=Y; _gcl_au=1.1.518790589.1676218907; mbox=PC#dc792f58a54d46e587d9ec23460606e3.37_0#1739491007|session#c395bed6cac94e9cb8e1e65464bf55a3#1676248067; _ga_34PHSZMC42=GS1.1.1676245893.5.1.1676246215.0.0.0; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _ga=GA1.2.1402135257.1676208564',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-csrf-token': 'a943dc006afeb4885c95234b7efacb4a36bfecf002110b930c465fd02e62da33105679d68812f38cfffd1988d669a9266181b6f2aa8f8e8bd32316ca70758cbd75a83e934889ad892f1d48e66e518a7f',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    object = response.json()
    tweets = object['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']
    return tweets