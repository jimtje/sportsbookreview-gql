import sgqlc.types


sbr_schema_march_2021 = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class BestLine(sgqlc.types.Scalar):
    __schema__ = sbr_schema_march_2021


Boolean = sgqlc.types.Boolean

class ENT(sgqlc.types.Enum):
    __schema__ = sbr_schema_march_2021
    __choices__ = ('EVENT', 'EVENTLASTPLAY', 'EVENTROSTER', 'EVENTPARTICIPANT', 'TEAMBYLEAGUE', 'PLAYERBYLEAGUE', 'GROUPBYLEAGUE', 'SEASON', 'EVENTLASTPLAYDETAILS', 'TEAMROSTER')


Float = sgqlc.types.Float

Int = sgqlc.types.Int

class JSON(sgqlc.types.Scalar):
    __schema__ = sbr_schema_march_2021


class JSON(sgqlc.types.Scalar):
    __schema__ = sbr_schema_march_2021


class JSON(sgqlc.types.Scalar):
    __schema__ = sbr_schema_march_2021


class MarketTypeLayout(sgqlc.types.Enum):
    __schema__ = sbr_schema_march_2021
    __choices__ = ('PARTICIPANTS', 'BETTING_OPTIONS')


class ORDER(sgqlc.types.Enum):
    __schema__ = sbr_schema_march_2021
    __choices__ = ('ASC', 'DESC')


class SEASONGROUP(sgqlc.types.Enum):
    __schema__ = sbr_schema_march_2021
    __choices__ = ('PRE', 'REG', 'PST')


class ShowLive(sgqlc.types.Enum):
    __schema__ = sbr_schema_march_2021
    __choices__ = ('ONLY_LIVE_EVENTS', 'HIDE_LIVE_EVENTS', 'IGNORE')


String = sgqlc.types.String

class TopPerformerIdentity(sgqlc.types.Enum):
    __schema__ = sbr_schema_march_2021
    __choices__ = ('PASSING', 'RUSHING', 'RECEIVING')


class TypeInput(sgqlc.types.Enum):
    __schema__ = sbr_schema_march_2021
    __choices__ = ('TOP', 'UPCOMING')



########################################################################
# Input Objects
########################################################################
class BetSlipArgs(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('eid', 'mtid', 'partid', 'boid', 'sbid')
    eid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='eid')
    mtid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mtid')
    partid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='partid')
    boid = sgqlc.types.Field(Int, graphql_name='boid')
    sbid = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='sbid')


class EidsByPartid(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('partid', 'eids')
    partid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='partid')
    eids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='eids')


class EventFilterGroupMarketTypeSetting(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('spid', 'mtid', 'layout')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')
    layout = sgqlc.types.Field(String, graphql_name='layout')


class EventFilterGroupsArgs(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('efgids', 'sitid', 'time_zone_offset', 'startdate', 'show_live', 'spid', 'market_types', 'active', 'enabled')
    efgids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='efgids')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    time_zone_offset = sgqlc.types.Field(Float, graphql_name='timeZoneOffset')
    startdate = sgqlc.types.Field(Float, graphql_name='startdate')
    show_live = sgqlc.types.Field(ShowLive, graphql_name='showLive')
    spid = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='spid')
    market_types = sgqlc.types.Field(sgqlc.types.list_of(EventFilterGroupMarketTypeSetting), graphql_name='marketTypes')
    active = sgqlc.types.Field(Boolean, graphql_name='active')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')


class GeolocationIntput(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('latitude', 'longitude', 'max_distance')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitude')
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitude')
    max_distance = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='maxDistance')


class GroupInput(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('by',)
    by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='by')


class InputQueryFloat(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('gt', 'eq', 'between')
    gt = sgqlc.types.Field(Float, graphql_name='gt')
    eq = sgqlc.types.Field(Float, graphql_name='eq')
    between = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='between')


class LeagueFilter(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('enabled', 'sitid', 'did', 'lid')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    sitid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sitid')
    did = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='did')
    lid = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='lid')


class LeagueGroup(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtid', 'lid', 'spid', 'writeingame')
    mtid = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='mtid')
    lid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='lid')
    spid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='spid')
    writeingame = sgqlc.types.Field(Boolean, graphql_name='writeingame')


class LineGroupArgs(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('eid', 'mtid', 'partid', 'boid', 'sbid', 'market_type_layout')
    eid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='eid')
    mtid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mtid')
    partid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='partid')
    boid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='boid')
    sbid = sgqlc.types.Field(Int, graphql_name='sbid')
    market_type_layout = sgqlc.types.Field(sgqlc.types.non_null(MarketTypeLayout), graphql_name='marketTypeLayout')


class LocationInput(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('city', 'dt')
    city = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='city')
    dt = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dt')


class MenuOptionInput(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mid', 'sitid', 'mbid', 'parentlink', 'level')
    mid = sgqlc.types.Field(String, graphql_name='mid')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    mbid = sgqlc.types.Field(Int, graphql_name='mbid')
    parentlink = sgqlc.types.Field(String, graphql_name='parentlink')
    level = sgqlc.types.Field(Int, graphql_name='level')


class MenuOptionSettingInput(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mid', 'did', 'title', 'url', 'iconurl', 'showicon', 'showtext', 'enabled', 'ord')
    mid = sgqlc.types.Field(String, graphql_name='mid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    title = sgqlc.types.Field(String, graphql_name='title')
    url = sgqlc.types.Field(String, graphql_name='url')
    iconurl = sgqlc.types.Field(String, graphql_name='iconurl')
    showicon = sgqlc.types.Field(String, graphql_name='showicon')
    showtext = sgqlc.types.Field(String, graphql_name='showtext')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    ord = sgqlc.types.Field(Int, graphql_name='ord')


class RangeInput(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('gt', 'gte', 'eq', 'between')
    gt = sgqlc.types.Field(Float, graphql_name='gt')
    gte = sgqlc.types.Field(Float, graphql_name='gte')
    eq = sgqlc.types.Field(Float, graphql_name='eq')
    between = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='between')


class SortInput(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('by', 'order')
    by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='by')
    order = sgqlc.types.Field(ORDER, graphql_name='order')


class SportbooksByCategoryArgs(sgqlc.types.Input):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('sitid', 'did', 'cid', 'spid', 'enabled', 'sort_with', 'famid')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    cid = sgqlc.types.Field(Int, graphql_name='cid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    sort_with = sgqlc.types.Field(Boolean, graphql_name='sortWith')
    famid = sgqlc.types.Field(Int, graphql_name='famid')



########################################################################
# Output Objects and Interfaces
########################################################################
class Astronomy(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('sunrise', 'sunset', 'moonrise', 'moonset')
    sunrise = sgqlc.types.Field(String, graphql_name='sunrise')
    sunset = sgqlc.types.Field(String, graphql_name='sunset')
    moonrise = sgqlc.types.Field(String, graphql_name='moonrise')
    moonset = sgqlc.types.Field(String, graphql_name='moonset')


class BetSlipInfo(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('events', 'current_lines', 'market_types')
    events = sgqlc.types.Field(sgqlc.types.list_of('Event'), graphql_name='events')
    current_lines = sgqlc.types.Field(sgqlc.types.list_of(JSON), graphql_name='currentLines', args=sgqlc.types.ArgDict((
        ('paid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='paid', default=None)),
))
    )
    market_types = sgqlc.types.Field(sgqlc.types.list_of('MarketTypeWithSettings'), graphql_name='marketTypes')


class BettingOption(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('boid', 'nam', 'sequence')
    boid = sgqlc.types.Field(Int, graphql_name='boid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    sequence = sgqlc.types.Field(Int, graphql_name='sequence')


class CMSRegion(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('name', 'catid')
    name = sgqlc.types.Field(String, graphql_name='name')
    catid = sgqlc.types.Field(Int, graphql_name='catid')


class CMSSportsbook(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('id', 'name', 'provider_id', 'affiliate_link', 'image')
    id = sgqlc.types.Field(Int, graphql_name='ID')
    name = sgqlc.types.Field(String, graphql_name='name')
    provider_id = sgqlc.types.Field(Int, graphql_name='providerId')
    affiliate_link = sgqlc.types.Field(String, graphql_name='affiliateLink')
    image = sgqlc.types.Field(String, graphql_name='image')


class Category(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('catid', 'nam', 'alias', 'sitid', 'enabled', 'ord', 'generate_best_lines')
    catid = sgqlc.types.Field(Int, graphql_name='catid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    generate_best_lines = sgqlc.types.Field(Boolean, graphql_name='generateBestLines')


class ClimateAverages(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('month',)
    month = sgqlc.types.Field(sgqlc.types.list_of('Month'), graphql_name='month')


class Conference(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('id', 'name', 'shortname', 'favoriteshortname', 'favoritename')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    shortname = sgqlc.types.Field(String, graphql_name='shortname')
    favoriteshortname = sgqlc.types.Field(String, graphql_name='favoriteshortname')
    favoritename = sgqlc.types.Field(String, graphql_name='favoritename')


class Consensus(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('eid', 'mtid', 'bb', 'boid', 'partid', 'sbid', 'paid', 'lineid', 'wag', 'perc', 'vol', 'tvol', 'sequence', 'tim', 'wb', 'line')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')
    bb = sgqlc.types.Field(Int, graphql_name='bb')
    boid = sgqlc.types.Field(Int, graphql_name='boid')
    partid = sgqlc.types.Field(Int, graphql_name='partid')
    sbid = sgqlc.types.Field(Int, graphql_name='sbid')
    paid = sgqlc.types.Field(Int, graphql_name='paid')
    lineid = sgqlc.types.Field(Float, graphql_name='lineid')
    wag = sgqlc.types.Field(Int, graphql_name='wag')
    perc = sgqlc.types.Field(Float, graphql_name='perc')
    vol = sgqlc.types.Field(Float, graphql_name='vol')
    tvol = sgqlc.types.Field(Float, graphql_name='tvol')
    sequence = sgqlc.types.Field(Int, graphql_name='sequence')
    tim = sgqlc.types.Field(Float, graphql_name='tim')
    wb = sgqlc.types.Field(Int, graphql_name='wb')
    line = sgqlc.types.Field(JSON, graphql_name='line')


class ConsensusWithMaxSequence(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('consensus', 'max_sequence')
    consensus = sgqlc.types.Field(sgqlc.types.list_of(Consensus), graphql_name='consensus')
    max_sequence = sgqlc.types.Field(Float, graphql_name='maxSequence')


class CurrentCondition(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('observation_time', 'temp__c', 'temp__f', 'weather_code', 'weather_icon_url', 'weather_desc', 'windspeed_miles', 'windspeed_kmph', 'winddir_degree', 'winddir16_point', 'precip_mm', 'humidity', 'visibility', 'pressure', 'cloudcover', 'feels_like_c', 'feels_like_f')
    observation_time = sgqlc.types.Field(String, graphql_name='observation_time')
    temp__c = sgqlc.types.Field(String, graphql_name='temp_C')
    temp__f = sgqlc.types.Field(String, graphql_name='temp_F')
    weather_code = sgqlc.types.Field(String, graphql_name='weatherCode')
    weather_icon_url = sgqlc.types.Field(sgqlc.types.list_of('Value'), graphql_name='weatherIconUrl')
    weather_desc = sgqlc.types.Field(sgqlc.types.list_of('Value'), graphql_name='weatherDesc')
    windspeed_miles = sgqlc.types.Field(String, graphql_name='windspeedMiles')
    windspeed_kmph = sgqlc.types.Field(String, graphql_name='windspeedKmph')
    winddir_degree = sgqlc.types.Field(String, graphql_name='winddirDegree')
    winddir16_point = sgqlc.types.Field(String, graphql_name='winddir16Point')
    precip_mm = sgqlc.types.Field(String, graphql_name='precipMM')
    humidity = sgqlc.types.Field(String, graphql_name='humidity')
    visibility = sgqlc.types.Field(String, graphql_name='visibility')
    pressure = sgqlc.types.Field(String, graphql_name='pressure')
    cloudcover = sgqlc.types.Field(String, graphql_name='cloudcover')
    feels_like_c = sgqlc.types.Field(String, graphql_name='FeelsLikeC')
    feels_like_f = sgqlc.types.Field(String, graphql_name='FeelsLikeF')


class CurrentLinesWithMaxSequence(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('current_lines', 'max_sequence')
    current_lines = sgqlc.types.Field(sgqlc.types.list_of(JSON), graphql_name='currentLines')
    max_sequence = sgqlc.types.Field(Float, graphql_name='maxSequence')


class Customized(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('value', 'parentid')
    value = sgqlc.types.Field(Boolean, graphql_name='value')
    parentid = sgqlc.types.Field(Int, graphql_name='parentid')


class DepthChart(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('id', 'seid', 'tmid', 'pid', 'pposid', 'week', 'val', 'position')
    id = sgqlc.types.Field(Int, graphql_name='id')
    seid = sgqlc.types.Field(Int, graphql_name='seid')
    tmid = sgqlc.types.Field(Int, graphql_name='tmid')
    pid = sgqlc.types.Field(Int, graphql_name='pid')
    pposid = sgqlc.types.Field(Int, graphql_name='pposid')
    week = sgqlc.types.Field(Int, graphql_name='week')
    val = sgqlc.types.Field(Int, graphql_name='val')
    position = sgqlc.types.Field('Position', graphql_name='position')


class Division(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('id', 'name', 'shortname', 'favoriteshortname')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    shortname = sgqlc.types.Field(String, graphql_name='shortname')
    favoriteshortname = sgqlc.types.Field(String, graphql_name='favoriteshortname')


class Domain(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('did', 'sitid', 'nam', 'is_sport_customized', 'is_league_customized', 'is_market_type_customized', 'is_market_type_group_customized', 'is_footer_bar_customized', 'is_family_bar_customized', 'ord', 'ismainregion', 'countries', 'enabled')
    did = sgqlc.types.Field(Int, graphql_name='did')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    is_sport_customized = sgqlc.types.Field(Customized, graphql_name='isSportCustomized')
    is_league_customized = sgqlc.types.Field(Customized, graphql_name='isLeagueCustomized')
    is_market_type_customized = sgqlc.types.Field(Customized, graphql_name='isMarketTypeCustomized')
    is_market_type_group_customized = sgqlc.types.Field(Customized, graphql_name='isMarketTypeGroupCustomized')
    is_footer_bar_customized = sgqlc.types.Field(Customized, graphql_name='isFooterBarCustomized')
    is_family_bar_customized = sgqlc.types.Field(Customized, graphql_name='isFamilyBarCustomized')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    ismainregion = sgqlc.types.Field(Boolean, graphql_name='ismainregion')
    countries = sgqlc.types.Field(String, graphql_name='countries')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')


class Event(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('eid', 'cit', 'dt', 'des', 'es', 'ic', 'hl', 'lu', 'lid', 'rid', 'spid', 'sta', 'st', 'cou', 'zcode', 'ven', 'tvs', 'sequence', 'seid', 'writeingame', 'scores', 'league', 'participants', 'statistics', 'statistics_by_groups', 'event_statistics_by_group', 'market_type', 'market_types', 'current_lines', 'opening_lines', 'best_lines', 'betting_options', 'plays', 'event_group', 'event_tags', 'consensus', 'weather', 'event_markets_count', 'tl', 'att', 'fo', 'tr', 'lat', 'lon', 'seg', 'slg', 'cov')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    cit = sgqlc.types.Field(String, graphql_name='cit')
    dt = sgqlc.types.Field(Float, graphql_name='dt')
    des = sgqlc.types.Field(String, graphql_name='des')
    es = sgqlc.types.Field(String, graphql_name='es')
    ic = sgqlc.types.Field(Boolean, graphql_name='ic')
    hl = sgqlc.types.Field(Boolean, graphql_name='hl')
    lu = sgqlc.types.Field(String, graphql_name='lu')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    rid = sgqlc.types.Field(Int, graphql_name='rid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    sta = sgqlc.types.Field(String, graphql_name='sta')
    st = sgqlc.types.Field(String, graphql_name='st')
    cou = sgqlc.types.Field(String, graphql_name='cou')
    zcode = sgqlc.types.Field(String, graphql_name='zcode')
    ven = sgqlc.types.Field(String, graphql_name='ven')
    tvs = sgqlc.types.Field(String, graphql_name='tvs')
    sequence = sgqlc.types.Field(Int, graphql_name='sequence')
    seid = sgqlc.types.Field(Int, graphql_name='seid')
    writeingame = sgqlc.types.Field(Boolean, graphql_name='writeingame')
    scores = sgqlc.types.Field(sgqlc.types.list_of('Score'), graphql_name='scores')
    league = sgqlc.types.Field('LeagueWithSettings', graphql_name='league')
    participants = sgqlc.types.Field(sgqlc.types.list_of('Participant'), graphql_name='participants')
    statistics = sgqlc.types.Field(sgqlc.types.list_of('Statistic'), graphql_name='statistics', args=sgqlc.types.ArgDict((
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
        ('typ', sgqlc.types.Arg(String, graphql_name='typ', default=None)),
        ('sgid_when_finished', sgqlc.types.Arg(Int, graphql_name='sgidWhenFinished', default=None)),
))
    )
    statistics_by_groups = sgqlc.types.Field(sgqlc.types.list_of('StatisticByGroup'), graphql_name='statisticsByGroups', args=sgqlc.types.ArgDict((
        ('statistic_group', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='statisticGroup', default=None)),
        ('identities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='identities', default=None)),
        ('eids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eids', default=None)),
        ('tmids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='tmids', default=None)),
        ('partids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partids', default=None)),
        ('seids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='seids', default=None)),
        ('ent', sgqlc.types.Arg(sgqlc.types.list_of(ENT), graphql_name='ent', default=None)),
))
    )
    event_statistics_by_group = sgqlc.types.Field(sgqlc.types.list_of('StatisticByGroup'), graphql_name='eventStatisticsByGroup', args=sgqlc.types.ArgDict((
        ('statistic_group', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='statisticGroup', default=None)),
))
    )
    market_type = sgqlc.types.Field('MarketTypeWithSettings', graphql_name='marketType')
    market_types = sgqlc.types.Field(sgqlc.types.list_of('MarketTypeWithSettings'), graphql_name='marketTypes')
    current_lines = sgqlc.types.Field(sgqlc.types.list_of(JSON), graphql_name='currentLines', args=sgqlc.types.ArgDict((
        ('need_sbid', sgqlc.types.Arg(Boolean, graphql_name='needSbid', default=None)),
        ('paid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='paid', default=None)),
        ('sbid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='sbid', default=None)),
        ('catid', sgqlc.types.Arg(Int, graphql_name='catid', default=None)),
))
    )
    opening_lines = sgqlc.types.Field(sgqlc.types.list_of(JSON), graphql_name='openingLines', args=sgqlc.types.ArgDict((
        ('need_sbid', sgqlc.types.Arg(Boolean, graphql_name='needSbid', default=None)),
        ('paid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='paid', default=None)),
        ('sbid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='sbid', default=None)),
        ('catid', sgqlc.types.Arg(Int, graphql_name='catid', default=None)),
))
    )
    best_lines = sgqlc.types.Field(sgqlc.types.list_of(JSON), graphql_name='bestLines', args=sgqlc.types.ArgDict((
        ('mtid', sgqlc.types.Arg(Int, graphql_name='mtid', default=None)),
        ('paid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='paid', default=None)),
        ('catid', sgqlc.types.Arg(Int, graphql_name='catid', default=None)),
))
    )
    betting_options = sgqlc.types.Field(sgqlc.types.list_of('EventBettingOption'), graphql_name='bettingOptions')
    plays = sgqlc.types.Field(sgqlc.types.list_of('Play'), graphql_name='plays', args=sgqlc.types.ArgDict((
        ('pgid', sgqlc.types.Arg(Int, graphql_name='pgid', default=None)),
        ('limit_last_seq', sgqlc.types.Arg(Int, graphql_name='limitLastSeq', default=None)),
        ('pgid_when_finished', sgqlc.types.Arg(Int, graphql_name='pgidWhenFinished', default=None)),
))
    )
    event_group = sgqlc.types.Field('EventGroup', graphql_name='eventGroup')
    event_tags = sgqlc.types.Field(sgqlc.types.list_of('EventTag'), graphql_name='eventTags')
    consensus = sgqlc.types.Field(sgqlc.types.list_of(Consensus), graphql_name='consensus')
    weather = sgqlc.types.Field(sgqlc.types.list_of('WeatherOutput'), graphql_name='weather')
    event_markets_count = sgqlc.types.Field(Int, graphql_name='eventMarketsCount')
    tl = sgqlc.types.Field(String, graphql_name='tl')
    att = sgqlc.types.Field(Int, graphql_name='att')
    fo = sgqlc.types.Field(String, graphql_name='fo')
    tr = sgqlc.types.Field(Int, graphql_name='tr')
    lat = sgqlc.types.Field(Float, graphql_name='lat')
    lon = sgqlc.types.Field(Float, graphql_name='lon')
    seg = sgqlc.types.Field(String, graphql_name='seg')
    slg = sgqlc.types.Field(String, graphql_name='slg')
    cov = sgqlc.types.Field(String, graphql_name='cov')


class EventBettingOption(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('eid', 'partid', 'boid', 'nam', 'mtid', 'spid', 'sequence')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    partid = sgqlc.types.Field(Int, graphql_name='partid')
    boid = sgqlc.types.Field(Int, graphql_name='boid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    sequence = sgqlc.types.Field(Int, graphql_name='sequence')


class EventCatalog(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('des', 'date', 'league', 'sport', 'spid', 'region', 'eid', 'search_participants', 'event_participants', 'lid', 'path')
    des = sgqlc.types.Field(String, graphql_name='des')
    date = sgqlc.types.Field(String, graphql_name='date')
    league = sgqlc.types.Field(String, graphql_name='league')
    sport = sgqlc.types.Field(String, graphql_name='sport')
    spid = sgqlc.types.Field(String, graphql_name='spid')
    region = sgqlc.types.Field(String, graphql_name='region')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    search_participants = sgqlc.types.Field(sgqlc.types.list_of('SearchParticipant'), graphql_name='searchParticipants')
    event_participants = sgqlc.types.Field(String, graphql_name='eventParticipants')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    path = sgqlc.types.Field(String, graphql_name='path')


class EventDateCount(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('dt', 'size')
    dt = sgqlc.types.Field(Float, graphql_name='dt')
    size = sgqlc.types.Field(Int, graphql_name='size')


class EventFilter(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('efid', 'nam', 'efgids', 'spid', 'mtids', 'events', 'lids', 'eids', 'rids', 'sortmode', 'filtertype', 'eventtoshow', 'cutoffpoint', 'amount', 'ord', 'showlive', 'minutes', 'enabled', 'active')
    efid = sgqlc.types.Field(String, graphql_name='efid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    efgids = sgqlc.types.Field(String, graphql_name='efgids')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    mtids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='mtids')
    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events')
    lids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='lids')
    eids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='eids')
    rids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rids')
    sortmode = sgqlc.types.Field(String, graphql_name='sortmode')
    filtertype = sgqlc.types.Field(String, graphql_name='filtertype')
    eventtoshow = sgqlc.types.Field(Int, graphql_name='eventtoshow')
    cutoffpoint = sgqlc.types.Field(String, graphql_name='cutoffpoint')
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    showlive = sgqlc.types.Field(Boolean, graphql_name='showlive')
    minutes = sgqlc.types.Field(Int, graphql_name='minutes')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    active = sgqlc.types.Field(Boolean, graphql_name='active')


class EventFilterGroup(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('efgid', 'nam', 'sitid', 'ord', 'maxshow', 'enabled', 'active', 'events_filters', 'max_sequences')
    efgid = sgqlc.types.Field(String, graphql_name='efgid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    maxshow = sgqlc.types.Field(Int, graphql_name='maxshow')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    active = sgqlc.types.Field(Boolean, graphql_name='active')
    events_filters = sgqlc.types.Field(sgqlc.types.list_of(EventFilter), graphql_name='eventsFilters')
    max_sequences = sgqlc.types.Field('MaxSequences', graphql_name='maxSequences')


class EventFilterGroupLegacy(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('egid', 'sitid', 'settings')
    egid = sgqlc.types.Field(String, graphql_name='egid')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    settings = sgqlc.types.Field('EventFilterGroupSettings', graphql_name='settings', args=sgqlc.types.ArgDict((
        ('did', sgqlc.types.Arg(Int, graphql_name='did', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
))
    )


class EventFilterGroupSettings(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('egid', 'did', 'nam', 'enabled', 'active')
    egid = sgqlc.types.Field(String, graphql_name='egid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    active = sgqlc.types.Field(Boolean, graphql_name='active')


class EventFilterGroupWithEventIds(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('egid', 'sitid', 'event_ids_by_sport', 'event_ids_by_filter')
    egid = sgqlc.types.Field(String, graphql_name='egid')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    event_ids_by_sport = sgqlc.types.Field(sgqlc.types.list_of('EventIdsBySport'), graphql_name='eventIdsBySport', args=sgqlc.types.ArgDict((
        ('did', sgqlc.types.Arg(Int, graphql_name='did', default=None)),
))
    )
    event_ids_by_filter = sgqlc.types.Field(sgqlc.types.list_of('eventIdsByFilter'), graphql_name='eventIdsByFilter', args=sgqlc.types.ArgDict((
        ('did', sgqlc.types.Arg(Int, graphql_name='did', default=None)),
))
    )


class EventFilterGroupWithEvents(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('egid', 'events_by_sport', 'events_by_filter', 'max_sequences')
    egid = sgqlc.types.Field(String, graphql_name='egid')
    events_by_sport = sgqlc.types.Field(sgqlc.types.list_of('EventsBySport'), graphql_name='eventsBySport')
    events_by_filter = sgqlc.types.Field(sgqlc.types.list_of('EventsByFilter'), graphql_name='eventsByFilter')
    max_sequences = sgqlc.types.Field('MaxSequences', graphql_name='maxSequences')


class EventGroup(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('egid', 'nam', 'alias', 'lid', 'eid', 'disord', 'ic', 'sdt', 'edt', 'parentname', 'parentid')
    egid = sgqlc.types.Field(Int, graphql_name='egid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    disord = sgqlc.types.Field(Int, graphql_name='disord')
    ic = sgqlc.types.Field(Boolean, graphql_name='ic')
    sdt = sgqlc.types.Field(Float, graphql_name='sdt')
    edt = sgqlc.types.Field(Float, graphql_name='edt')
    parentname = sgqlc.types.Field(String, graphql_name='parentname')
    parentid = sgqlc.types.Field(Int, graphql_name='parentid')


class EventGroupBySeason(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('egid', 'nam', 'alias', 'ceg', 'seid', 'disord', 'sdt', 'edt', 'eids', 'mtids', 'hl')
    egid = sgqlc.types.Field(Int, graphql_name='egid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    ceg = sgqlc.types.Field(Int, graphql_name='ceg')
    seid = sgqlc.types.Field(Int, graphql_name='seid')
    disord = sgqlc.types.Field(Int, graphql_name='disord')
    sdt = sgqlc.types.Field(Float, graphql_name='sdt')
    edt = sgqlc.types.Field(Float, graphql_name='edt')
    eids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='eids')
    mtids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='mtids')
    hl = sgqlc.types.Field(Boolean, graphql_name='hl', args=sgqlc.types.ArgDict((
        ('catid', sgqlc.types.Arg(Int, graphql_name='catid', default=None)),
))
    )


class EventIdsBySport(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('spid', 'mtid', 'eids')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')
    eids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='eids')


class EventIdsSlugInfo(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('ceid', 'leid')
    ceid = sgqlc.types.Field(Int, graphql_name='ceid')
    leid = sgqlc.types.Field(Int, graphql_name='leid')


class EventInfoByParticipant(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('partid', 'eid', 'events', 'events_by_participant')
    partid = sgqlc.types.Field(Int, graphql_name='partid')
    eid = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='eid')
    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events', args=sgqlc.types.ArgDict((
        ('es', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='es', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('limit_date', sgqlc.types.Arg(Float, graphql_name='limitDate', default=None)),
))
    )
    events_by_participant = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='eventsByParticipant', args=sgqlc.types.ArgDict((
        ('es', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='es', default=None)),
        ('sort', sgqlc.types.Arg(sgqlc.types.non_null(SortInput), graphql_name='sort', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
        ('limit_date', sgqlc.types.Arg(Float, graphql_name='limitDate', default=None)),
))
    )


class EventLocation(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('eid', 'lat', 'lon', 'add', 'cou', 'sta', 'ven', 'cit', 'zcode', 'att', 'fo')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    lat = sgqlc.types.Field(Float, graphql_name='lat')
    lon = sgqlc.types.Field(Float, graphql_name='lon')
    add = sgqlc.types.Field(String, graphql_name='add')
    cou = sgqlc.types.Field(String, graphql_name='cou')
    sta = sgqlc.types.Field(String, graphql_name='sta')
    ven = sgqlc.types.Field(String, graphql_name='ven')
    cit = sgqlc.types.Field(String, graphql_name='cit')
    zcode = sgqlc.types.Field(String, graphql_name='zcode')
    att = sgqlc.types.Field(Int, graphql_name='att')
    fo = sgqlc.types.Field(String, graphql_name='fo')


class EventMarketLine(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtid', 'eid', 'act', 'maxsequence')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    maxsequence = sgqlc.types.Field(Float, graphql_name='maxsequence')


class EventMarkets(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtids',)
    mtids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='mtids')


class EventRegion(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('available', 'active')
    available = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='available')
    active = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='active')


class EventRoster(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('erid', 'eid', 'sid', 'pid', 'partid', 'act', 'sequence', 'ilu', 'luo', 'roster', 'statistics_by_groups')
    erid = sgqlc.types.Field(Int, graphql_name='erid')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    sid = sgqlc.types.Field(Int, graphql_name='sid')
    pid = sgqlc.types.Field(Int, graphql_name='pid')
    partid = sgqlc.types.Field(Int, graphql_name='partid')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    sequence = sgqlc.types.Field(Int, graphql_name='sequence')
    ilu = sgqlc.types.Field(Boolean, graphql_name='ilu')
    luo = sgqlc.types.Field(Int, graphql_name='luo')
    roster = sgqlc.types.Field('Player', graphql_name='roster')
    statistics_by_groups = sgqlc.types.Field(sgqlc.types.list_of('StatisticByGroup'), graphql_name='statisticsByGroups', args=sgqlc.types.ArgDict((
        ('statistic_group', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='statisticGroup', default=None)),
        ('identities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='identities', default=None)),
        ('eids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eids', default=None)),
        ('tmids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='tmids', default=None)),
        ('partids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partids', default=None)),
        ('seids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='seids', default=None)),
        ('ent', sgqlc.types.Arg(sgqlc.types.list_of(ENT), graphql_name='ent', default=None)),
))
    )


class EventTag(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('id', 'link', 'tag', 'eid')
    id = sgqlc.types.Field(Int, graphql_name='ID')
    link = sgqlc.types.Field(String, graphql_name='link')
    tag = sgqlc.types.Field('Tag', graphql_name='tag')
    eid = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='eid')


class EventsByFilter(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('efid', 'spid', 'lids', 'sortmode', 'events')
    efid = sgqlc.types.Field(String, graphql_name='efid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    lids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='lids')
    sortmode = sgqlc.types.Field(String, graphql_name='sortmode')
    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events')


class EventsByParticipant(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('partid', 'events')
    partid = sgqlc.types.Field(Int, graphql_name='partid')
    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events')


class EventsBySport(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('spid', 'events')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events')


class EventsCarousel(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('event_filter_groups', 'sportbooks_by_category', 'max_sequences')
    event_filter_groups = sgqlc.types.Field(sgqlc.types.list_of(EventFilterGroup), graphql_name='eventFilterGroups')
    sportbooks_by_category = sgqlc.types.Field(sgqlc.types.list_of('SportbooksByCategory'), graphql_name='sportbooksByCategory')
    max_sequences = sgqlc.types.Field('MaxSequences', graphql_name='maxSequences')


class EventsWithMaxSequence(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('events', 'max_sequence')
    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events')
    max_sequence = sgqlc.types.Field(Float, graphql_name='maxSequence')


class EventsWithMaxSequences(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('events', 'max_sequences')
    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events')
    max_sequences = sgqlc.types.Field('MaxSequences', graphql_name='maxSequences')


class GroupedHistoryLine(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('history_line',)
    history_line = sgqlc.types.Field(sgqlc.types.list_of(JSON), graphql_name='historyLine', args=sgqlc.types.ArgDict((
        ('group_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='groupId', default=None)),
))
    )


class HistoryLine(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('tim', 'lines')
    tim = sgqlc.types.Field(Float, graphql_name='tim')
    lines = sgqlc.types.Field(sgqlc.types.list_of(JSON), graphql_name='lines')


class Hourly(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('time', 'utcdate', 'utctime', 'temp_c', 'temp_f', 'windspeed_miles', 'windspeed_kmph', 'winddir_degree', 'winddir16_point', 'weather_code', 'weather_icon_url', 'weather_desc', 'precip_mm', 'humidity', 'visibility', 'pressure', 'cloudcover', 'heat_index_c', 'heat_index_f', 'dew_point_c', 'dew_point_f', 'wind_chill_c', 'wind_chill_f', 'wind_gust_miles', 'wind_gust_kmph', 'feels_like_c', 'feels_like_f', 'chanceofrain', 'chanceofremdry', 'chanceofwindy', 'chanceofovercast', 'chanceofsunshine', 'chanceoffrost', 'chanceofhightemp', 'chanceoffog', 'chanceofsnow', 'chanceofthunder')
    time = sgqlc.types.Field(String, graphql_name='time')
    utcdate = sgqlc.types.Field(String, graphql_name='UTCdate')
    utctime = sgqlc.types.Field(String, graphql_name='UTCtime')
    temp_c = sgqlc.types.Field(String, graphql_name='tempC')
    temp_f = sgqlc.types.Field(String, graphql_name='tempF')
    windspeed_miles = sgqlc.types.Field(String, graphql_name='windspeedMiles')
    windspeed_kmph = sgqlc.types.Field(String, graphql_name='windspeedKmph')
    winddir_degree = sgqlc.types.Field(String, graphql_name='winddirDegree')
    winddir16_point = sgqlc.types.Field(String, graphql_name='winddir16Point')
    weather_code = sgqlc.types.Field(String, graphql_name='weatherCode')
    weather_icon_url = sgqlc.types.Field(sgqlc.types.list_of('Value'), graphql_name='weatherIconUrl')
    weather_desc = sgqlc.types.Field(sgqlc.types.list_of('Value'), graphql_name='weatherDesc')
    precip_mm = sgqlc.types.Field(String, graphql_name='precipMM')
    humidity = sgqlc.types.Field(String, graphql_name='humidity')
    visibility = sgqlc.types.Field(String, graphql_name='visibility')
    pressure = sgqlc.types.Field(String, graphql_name='pressure')
    cloudcover = sgqlc.types.Field(String, graphql_name='cloudcover')
    heat_index_c = sgqlc.types.Field(String, graphql_name='HeatIndexC')
    heat_index_f = sgqlc.types.Field(String, graphql_name='HeatIndexF')
    dew_point_c = sgqlc.types.Field(String, graphql_name='DewPointC')
    dew_point_f = sgqlc.types.Field(String, graphql_name='DewPointF')
    wind_chill_c = sgqlc.types.Field(String, graphql_name='WindChillC')
    wind_chill_f = sgqlc.types.Field(String, graphql_name='WindChillF')
    wind_gust_miles = sgqlc.types.Field(String, graphql_name='WindGustMiles')
    wind_gust_kmph = sgqlc.types.Field(String, graphql_name='WindGustKmph')
    feels_like_c = sgqlc.types.Field(String, graphql_name='FeelsLikeC')
    feels_like_f = sgqlc.types.Field(String, graphql_name='FeelsLikeF')
    chanceofrain = sgqlc.types.Field(String, graphql_name='chanceofrain')
    chanceofremdry = sgqlc.types.Field(String, graphql_name='chanceofremdry')
    chanceofwindy = sgqlc.types.Field(String, graphql_name='chanceofwindy')
    chanceofovercast = sgqlc.types.Field(String, graphql_name='chanceofovercast')
    chanceofsunshine = sgqlc.types.Field(String, graphql_name='chanceofsunshine')
    chanceoffrost = sgqlc.types.Field(String, graphql_name='chanceoffrost')
    chanceofhightemp = sgqlc.types.Field(String, graphql_name='chanceofhightemp')
    chanceoffog = sgqlc.types.Field(String, graphql_name='chanceoffog')
    chanceofsnow = sgqlc.types.Field(String, graphql_name='chanceofsnow')
    chanceofthunder = sgqlc.types.Field(String, graphql_name='chanceofthunder')


class Image(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('id', 'filename', 'title', 'description', 'tags', 'sizes', 'updated_at', 'created_at')
    id = sgqlc.types.Field(String, graphql_name='id')
    filename = sgqlc.types.Field(String, graphql_name='filename')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')
    sizes = sgqlc.types.Field('Size', graphql_name='sizes')
    updated_at = sgqlc.types.Field(Float, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(Float, graphql_name='createdAt')


class InjuryResponse(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('pid', 'tmid', 'seid', 'typ', 'stt', 'loc', 'det', 'side', 'retdt', 'disch', 'hl', 'not_', 'newstim', 'newsdate', 'team_roster_player', 'prio')
    pid = sgqlc.types.Field(Int, graphql_name='pid')
    tmid = sgqlc.types.Field(Int, graphql_name='tmid')
    seid = sgqlc.types.Field(Int, graphql_name='seid')
    typ = sgqlc.types.Field(String, graphql_name='typ')
    stt = sgqlc.types.Field(String, graphql_name='stt')
    loc = sgqlc.types.Field(String, graphql_name='loc')
    det = sgqlc.types.Field(String, graphql_name='det')
    side = sgqlc.types.Field(String, graphql_name='side')
    retdt = sgqlc.types.Field(Float, graphql_name='retdt')
    disch = sgqlc.types.Field(Boolean, graphql_name='disch')
    hl = sgqlc.types.Field(String, graphql_name='hl')
    not_ = sgqlc.types.Field(String, graphql_name='not')
    newstim = sgqlc.types.Field(Float, graphql_name='newstim')
    newsdate = sgqlc.types.Field(Float, graphql_name='newsdate')
    team_roster_player = sgqlc.types.Field('TeamRosterPlayer', graphql_name='teamRosterPlayer')
    prio = sgqlc.types.Field(Int, graphql_name='prio')


class League(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('lid', 'nam', 'rid', 'spid', 'sn', 'lurl')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    rid = sgqlc.types.Field(Int, graphql_name='rid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    sn = sgqlc.types.Field(String, graphql_name='sn')
    lurl = sgqlc.types.Field(String, graphql_name='lurl')


class LeagueCatalog(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('did', 'lid', 'nam', 'rid', 'spid', 'sn', 'region', 'settings', 'path')
    did = sgqlc.types.Field(Int, graphql_name='did')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    rid = sgqlc.types.Field(Int, graphql_name='rid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    sn = sgqlc.types.Field(String, graphql_name='sn')
    region = sgqlc.types.Field('RegionLeague', graphql_name='region')
    settings = sgqlc.types.Field('LeagueSettings', graphql_name='settings')
    path = sgqlc.types.Field(String, graphql_name='path')


class LeagueHierarchy(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('team_id', 'season_id', 'league_id', 'conference', 'division')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    season_id = sgqlc.types.Field(Int, graphql_name='seasonId')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    conference = sgqlc.types.Field(Conference, graphql_name='conference')
    division = sgqlc.types.Field(Division, graphql_name='division')


class LeagueMarket(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('lid', 'mtid')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')


class LeagueSetting(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('lid', 'sitid', 'did', 'enabled', 'alias', 'rotation', 'ord', 'shortnamealias', 'shortnamebreakpoint', 'matchupline', '_is_custom', '_is_favorite', '_is_default_favorite')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    rotation = sgqlc.types.Field(Boolean, graphql_name='rotation')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    shortnamealias = sgqlc.types.Field(String, graphql_name='shortnamealias')
    shortnamebreakpoint = sgqlc.types.Field(String, graphql_name='shortnamebreakpoint')
    matchupline = sgqlc.types.Field(Boolean, graphql_name='matchupline')
    _is_custom = sgqlc.types.Field(Boolean, graphql_name='_isCustom')
    _is_favorite = sgqlc.types.Field(Boolean, graphql_name='_isFavorite')
    _is_default_favorite = sgqlc.types.Field(Boolean, graphql_name='_isDefaultFavorite')


class LeagueSettings(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('enabled', 'alias', 'ord', 'shortnamealias')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    shortnamealias = sgqlc.types.Field(String, graphql_name='shortnamealias')


class LeagueV2(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('lid', 'nam', 'rid', 'spid', 'market_type', 'sport', 'sn', 'enabled', 'alias', 'rotation', 'sitid', 'did', 'region', 'lurl', 'settings')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    rid = sgqlc.types.Field(Int, graphql_name='rid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    market_type = sgqlc.types.Field('MarketTypeWithSettings', graphql_name='marketType')
    sport = sgqlc.types.Field('Sport', graphql_name='sport')
    sn = sgqlc.types.Field(String, graphql_name='sn')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    rotation = sgqlc.types.Field(Boolean, graphql_name='rotation')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    region = sgqlc.types.Field('Region', graphql_name='region')
    lurl = sgqlc.types.Field(String, graphql_name='lurl')
    settings = sgqlc.types.Field(LeagueSetting, graphql_name='settings', args=sgqlc.types.ArgDict((
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
        ('merge', sgqlc.types.Arg(Boolean, graphql_name='merge', default=None)),
))
    )


class LeagueWithSettings(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('lid', 'nam', 'rid', 'spid', 'did', 'sn', 'lurl', 'market_type', 'region', 'settings', 'sport')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    rid = sgqlc.types.Field(Int, graphql_name='rid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    sn = sgqlc.types.Field(String, graphql_name='sn')
    lurl = sgqlc.types.Field(String, graphql_name='lurl')
    market_type = sgqlc.types.Field('MarketTypeWithSettings', graphql_name='marketType')
    region = sgqlc.types.Field('Region', graphql_name='region')
    settings = sgqlc.types.Field(LeagueSetting, graphql_name='settings')
    sport = sgqlc.types.Field('Sport', graphql_name='sport')


class LeagueWithSettingsV2(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('lid', 'nam', 'rid', 'spid', 'did', 'lurl', 'sn', 'market_type', 'region', 'settings')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    rid = sgqlc.types.Field(Int, graphql_name='rid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    lurl = sgqlc.types.Field(String, graphql_name='lurl')
    sn = sgqlc.types.Field(String, graphql_name='sn')
    market_type = sgqlc.types.Field('MarketTypeWithSettings', graphql_name='marketType')
    region = sgqlc.types.Field('RegionLeagueV2', graphql_name='region')
    settings = sgqlc.types.Field(LeagueSetting, graphql_name='settings')


class LeaguesAndRegionsBySport(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('sitid', 'did', 'sports')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    sports = sgqlc.types.Field(sgqlc.types.list_of('SportsWithRegions'), graphql_name='sports')


class LeaguesWithEventGroups(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('lid', 'nam', 'sn', 'enabled', 'alias', 'rotation', 'domain_ord', 'default_ord', 'shortnamealias', 'shortnamebreakpoint', 'matchupline', 'lurl', 'event_groups_by_league')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    sn = sgqlc.types.Field(String, graphql_name='sn')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    rotation = sgqlc.types.Field(Boolean, graphql_name='rotation')
    domain_ord = sgqlc.types.Field(Int, graphql_name='domainOrd')
    default_ord = sgqlc.types.Field(Int, graphql_name='defaultOrd')
    shortnamealias = sgqlc.types.Field(String, graphql_name='shortnamealias')
    shortnamebreakpoint = sgqlc.types.Field(String, graphql_name='shortnamebreakpoint')
    matchupline = sgqlc.types.Field(Boolean, graphql_name='matchupline')
    lurl = sgqlc.types.Field(String, graphql_name='lurl')
    event_groups_by_league = sgqlc.types.Field(sgqlc.types.list_of(EventGroup), graphql_name='eventGroupsByLeague')


class MainAffiliate(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('nam', 'enabled')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')


class MarketType(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtid', 'spid', 'nam', 'des')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    des = sgqlc.types.Field(String, graphql_name='des')


class MarketTypeGroup(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtgid', 'spid', 'nam')
    mtgid = sgqlc.types.Field(Int, graphql_name='mtgid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    nam = sgqlc.types.Field(String, graphql_name='nam')


class MarketTypeGroupFiltered(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtgid', 'ord', 'spid', 'nam', 'alias', 'mtids')
    mtgid = sgqlc.types.Field(Int, graphql_name='mtgid')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    mtids = sgqlc.types.Field(sgqlc.types.list_of('MarketTypeWithSettings'), graphql_name='mtids')


class MarketTypeGroupSetting(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('sitid', 'mtgid', 'did', 'enabled', 'ord', 'alias', 'url', 'active', '_is_custom', '_is_favorite', '_is_default_favorite')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    mtgid = sgqlc.types.Field(Int, graphql_name='mtgid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    url = sgqlc.types.Field(String, graphql_name='url')
    active = sgqlc.types.Field(Boolean, graphql_name='active')
    _is_custom = sgqlc.types.Field(Boolean, graphql_name='_isCustom')
    _is_favorite = sgqlc.types.Field(Boolean, graphql_name='_isFavorite')
    _is_default_favorite = sgqlc.types.Field(Boolean, graphql_name='_isDefaultFavorite')


class MarketTypeGroupWithMarketTypes(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtgid', 'mtids')
    mtgid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mtgid')
    mtids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarketTypesByMarketTypeGroup')), graphql_name='mtids')


class MarketTypeGroupWithSettings(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtgid', 'spid', 'nam', 'sitid', 'did', 'market_types', 'settings')
    mtgid = sgqlc.types.Field(Int, graphql_name='mtgid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    market_types = sgqlc.types.Field(sgqlc.types.list_of('MarketTypeWithSettings'), graphql_name='marketTypes')
    settings = sgqlc.types.Field(MarketTypeGroupSetting, graphql_name='settings')


class MarketTypeSetting(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtid', 'spid', 'sitid', 'did', 'enabled', 'alias', 'url', 'sort', 'template', 'format', 'layout', '_is_custom')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    url = sgqlc.types.Field(String, graphql_name='url')
    sort = sgqlc.types.Field(String, graphql_name='sort')
    template = sgqlc.types.Field(String, graphql_name='template')
    format = sgqlc.types.Field(String, graphql_name='format')
    layout = sgqlc.types.Field(String, graphql_name='layout')
    _is_custom = sgqlc.types.Field(Boolean, graphql_name='_isCustom')


class MarketTypeWithSettings(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtid', 'ord', 'spid', 'mtgid', 'nam', 'des', 'format', 'layout', 'settings')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    mtgid = sgqlc.types.Field(Int, graphql_name='mtgid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    des = sgqlc.types.Field(String, graphql_name='des')
    format = sgqlc.types.Field(String, graphql_name='format')
    layout = sgqlc.types.Field(String, graphql_name='layout')
    settings = sgqlc.types.Field(MarketTypeSetting, graphql_name='settings')


class MarketTypesByMarketTypeGroup(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mtid', 'ord')
    mtid = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mtid')
    ord = sgqlc.types.Field(Int, graphql_name='ord')


class MatchupDates(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('dates',)
    dates = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='dates')


class MatchupEvents(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('events',)
    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events')


class MatchupId(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('eid',)
    eid = sgqlc.types.Field(Int, graphql_name='eid')


class MaxSequence(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('max_sequence',)
    max_sequence = sgqlc.types.Field(Float, graphql_name='maxSequence')


class MaxSequences(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('events_max_sequence', 'scores_max_sequence', 'lines_max_sequence', 'statistics_max_sequence', 'statistics_by_groups_max_sequence', 'consensus_max_sequence', 'plays_max_sequence')
    events_max_sequence = sgqlc.types.Field(Float, graphql_name='eventsMaxSequence')
    scores_max_sequence = sgqlc.types.Field(Float, graphql_name='scoresMaxSequence')
    lines_max_sequence = sgqlc.types.Field(Float, graphql_name='linesMaxSequence')
    statistics_max_sequence = sgqlc.types.Field(Float, graphql_name='statisticsMaxSequence')
    statistics_by_groups_max_sequence = sgqlc.types.Field(Float, graphql_name='statisticsByGroupsMaxSequence')
    consensus_max_sequence = sgqlc.types.Field(Float, graphql_name='consensusMaxSequence')
    plays_max_sequence = sgqlc.types.Field(Float, graphql_name='playsMaxSequence')


class MenuOption(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mid', 'sitid', 'mbid', 'parentlink', 'level', 'settings', 'submenuoptions')
    mid = sgqlc.types.Field(String, graphql_name='mid')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    mbid = sgqlc.types.Field(Int, graphql_name='mbid')
    parentlink = sgqlc.types.Field(String, graphql_name='parentlink')
    level = sgqlc.types.Field(Int, graphql_name='level')
    settings = sgqlc.types.Field('MenuOptionSetting', graphql_name='settings', args=sgqlc.types.ArgDict((
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
        ('merge', sgqlc.types.Arg(Boolean, graphql_name='merge', default=None)),
))
    )
    submenuoptions = sgqlc.types.Field(sgqlc.types.list_of('MenuOption'), graphql_name='submenuoptions')


class MenuOptionSetting(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('mid', 'did', 'title', 'url', 'iconurl', 'showicon', 'showtext', 'enabled', 'ord')
    mid = sgqlc.types.Field(String, graphql_name='mid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    title = sgqlc.types.Field(String, graphql_name='title')
    url = sgqlc.types.Field(String, graphql_name='url')
    iconurl = sgqlc.types.Field(String, graphql_name='iconurl')
    showicon = sgqlc.types.Field(String, graphql_name='showicon')
    showtext = sgqlc.types.Field(String, graphql_name='showtext')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    ord = sgqlc.types.Field(Int, graphql_name='ord')


class Month(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('index', 'name', 'avg_min_temp', 'avg_min_temp__f', 'abs_max_temp', 'abs_max_temp__f', 'avg_daily_rainfall')
    index = sgqlc.types.Field(String, graphql_name='index')
    name = sgqlc.types.Field(String, graphql_name='name')
    avg_min_temp = sgqlc.types.Field(String, graphql_name='avgMinTemp')
    avg_min_temp__f = sgqlc.types.Field(String, graphql_name='avgMinTemp_F')
    abs_max_temp = sgqlc.types.Field(String, graphql_name='absMaxTemp')
    abs_max_temp__f = sgqlc.types.Field(String, graphql_name='absMaxTemp_F')
    avg_daily_rainfall = sgqlc.types.Field(String, graphql_name='avgDailyRainfall')


class MultipleResult(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('search_event', 'search_sport', 'search_league')
    search_event = sgqlc.types.Field(sgqlc.types.list_of(EventCatalog), graphql_name='searchEvent')
    search_sport = sgqlc.types.Field(sgqlc.types.list_of('SportCatalog'), graphql_name='searchSport')
    search_league = sgqlc.types.Field(sgqlc.types.list_of(LeagueCatalog), graphql_name='searchLeague')


class New(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('hl', 'not_', 'anly', 'prio', 'inid', 'pid', 'seid', 'act', 'tim', 'date')
    hl = sgqlc.types.Field(String, graphql_name='hl')
    not_ = sgqlc.types.Field(String, graphql_name='not')
    anly = sgqlc.types.Field(String, graphql_name='anly')
    prio = sgqlc.types.Field(Int, graphql_name='prio')
    inid = sgqlc.types.Field(Int, graphql_name='inid')
    pid = sgqlc.types.Field(Int, graphql_name='pid')
    seid = sgqlc.types.Field(Int, graphql_name='seid')
    act = sgqlc.types.Field(String, graphql_name='act')
    tim = sgqlc.types.Field(Float, graphql_name='tim')
    date = sgqlc.types.Field(Float, graphql_name='date')


class OddFormat(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('id', 'dcp', 'np', 'dep', 'tim', 'act')
    id = sgqlc.types.Field(Int, graphql_name='id')
    dcp = sgqlc.types.Field(Float, graphql_name='dcp')
    np = sgqlc.types.Field(Int, graphql_name='np')
    dep = sgqlc.types.Field(Int, graphql_name='dep')
    tim = sgqlc.types.Field(Float, graphql_name='tim')
    act = sgqlc.types.Field(Boolean, graphql_name='act')


class Participant(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('partid', 'eid', 'ptid', 'psid', 'partbeid', 'act', 'stt', 'rot', 'ih', 'sbrid', 'sppil', 'sppic', 'tr', 'starting_pitcher', 'source', 'stats_identity', 'statistics_by_groups', 'eventrosters')
    partid = sgqlc.types.Field(Int, graphql_name='partid')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    ptid = sgqlc.types.Field(Int, graphql_name='ptid')
    psid = sgqlc.types.Field(Int, graphql_name='psid')
    partbeid = sgqlc.types.Field(Int, graphql_name='partbeid')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    stt = sgqlc.types.Field(String, graphql_name='stt')
    rot = sgqlc.types.Field(Int, graphql_name='rot')
    ih = sgqlc.types.Field(Boolean, graphql_name='ih')
    sbrid = sgqlc.types.Field(Int, graphql_name='sbrid')
    sppil = sgqlc.types.Field(String, graphql_name='sppil')
    sppic = sgqlc.types.Field(Boolean, graphql_name='sppic')
    tr = sgqlc.types.Field(Int, graphql_name='tr')
    starting_pitcher = sgqlc.types.Field('Player', graphql_name='startingPitcher')
    source = sgqlc.types.Field('Source', graphql_name='source')
    stats_identity = sgqlc.types.Field(sgqlc.types.list_of('StatisticByGroup'), graphql_name='statsIdentity')
    statistics_by_groups = sgqlc.types.Field(sgqlc.types.list_of('StatisticByGroup'), graphql_name='statisticsByGroups', args=sgqlc.types.ArgDict((
        ('statistic_group', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='statisticGroup', default=None)),
        ('identities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='identities', default=None)),
        ('eids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eids', default=None)),
        ('tmids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='tmids', default=None)),
        ('partids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partids', default=None)),
        ('seids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='seids', default=None)),
        ('ent', sgqlc.types.Arg(sgqlc.types.list_of(ENT), graphql_name='ent', default=None)),
))
    )
    eventrosters = sgqlc.types.Field(sgqlc.types.list_of(EventRoster), graphql_name='eventrosters')


class ParticipantByEvent(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('partid', 'eid', 'ptid', 'act', 'psid', 'rot', 'ih', 'tr', 'sbrid', 'sppil', 'sppic', 'sppid', 'partbeid', 'seid')
    partid = sgqlc.types.Field(Int, graphql_name='partid')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    ptid = sgqlc.types.Field(Int, graphql_name='ptid')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    psid = sgqlc.types.Field(Int, graphql_name='psid')
    rot = sgqlc.types.Field(Int, graphql_name='rot')
    ih = sgqlc.types.Field(Boolean, graphql_name='ih')
    tr = sgqlc.types.Field(Int, graphql_name='tr')
    sbrid = sgqlc.types.Field(Int, graphql_name='sbrid')
    sppil = sgqlc.types.Field(String, graphql_name='sppil')
    sppic = sgqlc.types.Field(Boolean, graphql_name='sppic')
    sppid = sgqlc.types.Field(Int, graphql_name='sppid')
    partbeid = sgqlc.types.Field(Int, graphql_name='partbeid')
    seid = sgqlc.types.Field(Int, graphql_name='seid')


class ParticipantGroup(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('partgid', 'nam', 'lid', 'act', 'stt', 'participants')
    partgid = sgqlc.types.Field(Int, graphql_name='partgid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    stt = sgqlc.types.Field(Int, graphql_name='stt')
    participants = sgqlc.types.Field(sgqlc.types.list_of(Participant), graphql_name='participants')


class Play(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('eid', 'sqid', 'siid', 'gid', 'nam', 'val', 'tim', 'sequence')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    sqid = sgqlc.types.Field(Int, graphql_name='sqid')
    siid = sgqlc.types.Field(Int, graphql_name='siid')
    gid = sgqlc.types.Field(Int, graphql_name='gid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    val = sgqlc.types.Field(String, graphql_name='val')
    tim = sgqlc.types.Field(Float, graphql_name='tim')
    sequence = sgqlc.types.Field(Int, graphql_name='sequence')


class Player(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('pid', 'fn', 'lnam', 'cit', 'sta', 'cou', 'act', 'stt', 'hei', 'wei', 'bd', 'sch', 'dy', 'hsurl')
    pid = sgqlc.types.Field(Int, graphql_name='pid')
    fn = sgqlc.types.Field(String, graphql_name='fn')
    lnam = sgqlc.types.Field(String, graphql_name='lnam')
    cit = sgqlc.types.Field(String, graphql_name='cit')
    sta = sgqlc.types.Field(String, graphql_name='sta')
    cou = sgqlc.types.Field(String, graphql_name='cou')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    stt = sgqlc.types.Field(String, graphql_name='stt')
    hei = sgqlc.types.Field(Int, graphql_name='hei')
    wei = sgqlc.types.Field(Int, graphql_name='wei')
    bd = sgqlc.types.Field(Float, graphql_name='bd')
    sch = sgqlc.types.Field(String, graphql_name='sch')
    dy = sgqlc.types.Field(Float, graphql_name='dy')
    hsurl = sgqlc.types.Field(String, graphql_name='hsurl')


class PlaysWithMaxSequence(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('plays', 'max_sequence')
    plays = sgqlc.types.Field(sgqlc.types.list_of(Play), graphql_name='plays')
    max_sequence = sgqlc.types.Field(Float, graphql_name='maxSequence')


class Position(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('id', 'spid', 'nam', 'sn')
    id = sgqlc.types.Field(Int, graphql_name='id')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    sn = sgqlc.types.Field(String, graphql_name='sn')


class Query(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('my_hash', 'player', 'players', 'team', 'teams', 'division_teams', 'season_teams', 'team_rosters', 'league_hierarchy', 'participant', 'participants', 'participant_by_event', 'events_info_by_participant', 'matchups', 'last_matchups_by_participants', 'get_event_roster_by_events', 'head_to_head_events', 'next_events_by_participant', 'event_filter_groups', 'events', 'events_by_sport', 'events_by_sport_v2', 'events_by_date_deprecate', 'events_by_date', 'events_by_date_new', 'events_by_date_by_league_group', 'event_markets', 'events_by_league_group', 'events_v2', 'events_by_event_group', 'events_by_event_group_v2', 'nearest_season_events', 'leagues_with_events', 'events_region_by_sport', 'events_dates_count', 'events_dates_count_summary', 'calendar_events_by_event_group', 'calendar_events_by_event_group_v2', 'get_updated_events', 'sports_with_live_events', 'event_groups_by_leagues', 'event_groups_by_sport', 'events_by_team_id', 'related_events', 'events_location', 'upcoming_events', 'upcoming_events_new', 'get_top_events_by_sportsbook', 'get_event_ids_by_slug', 'league_setting', 'leagues_setting', 'league_settings_v2', 'league_markets', 'leagues_with_settings', 'get_leagues_with_settings_v2', 'league', 'leagues', 'leagues_by_id', 'sport_setting', 'sport_settings_v2', 'get_sports_with_settings_v2', 'sport', 'sports', 'get_leagues_and_regions_by_sport', 'conferences', 'divisions', 'region', 'regions', 'regions_by_sport', 'scores', 'get_updated_scores', 'statistic', 'statistics', 'get_updated_statistics', 'market_type', 'market_types', 'outright_market_types', 'market_types_by_id', 'current_lines', 'best_lines', 'get_updated_current_lines', 'get_current_lines_group_by_event_market', 'opening_lines', 'consensus', 'updated_consensus', 'consensus_history', 'weather', 'week_weather_forecast', 'event_group_by_event', 'event_groups_by_league', 'events_groups_by_season', 'get_event_tags', 'get_sportsbook_bonus_lists', 'betting_options', 'betting_options_by_event', 'bet_slip_info', 'market_type_group', 'market_type_groups_filtered', 'market_type_groups', 'market_type_groups_with_market_types', 'market_type_groups_by_id', 'max_sequences', 'formats', 'sportsbook_setting', 'sportsbook', 'sportsbooks', 'sportsbooks_by_category', 'categories', 'images', 'history_lines', 'line_history', 'menu_option', 'menu_options', 'search_event', 'multiple_search', 'domains', 'plays', 'plays_v2', 'updated_plays', 'sportbooks_by_category', 'statistics_by_groups', 'statistics_by_event', 'statistics_by_season', 'team_statistics', 'statistics_betting_odds_trends', 'statistics_umpire', 'top_performers', 'get_active_event_filter_groups', 'events_by_event_filter_group', 'event_filter_group_with_event_ids', 'events_carousel', 'live_lines', 'injuries', 'news')
    my_hash = sgqlc.types.Field(Boolean, graphql_name='myHash')
    player = sgqlc.types.Field(Player, graphql_name='player', args=sgqlc.types.ArgDict((
        ('pid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='pid', default=None)),
        ('fn', sgqlc.types.Arg(String, graphql_name='fn', default=None)),
        ('lnam', sgqlc.types.Arg(String, graphql_name='lnam', default=None)),
))
    )
    players = sgqlc.types.Field(sgqlc.types.list_of(Player), graphql_name='players', args=sgqlc.types.ArgDict((
        ('pid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='pid', default=None)),
        ('fn', sgqlc.types.Arg(String, graphql_name='fn', default=None)),
        ('lnam', sgqlc.types.Arg(String, graphql_name='lnam', default=None)),
))
    )
    team = sgqlc.types.Field('Team', graphql_name='team', args=sgqlc.types.ArgDict((
        ('tmid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='tmid', default=None)),
        ('nam', sgqlc.types.Arg(String, graphql_name='nam', default=None)),
        ('seid', sgqlc.types.Arg(Int, graphql_name='seid', default=None)),
        ('senam', sgqlc.types.Arg(String, graphql_name='senam', default=None)),
        ('lid', sgqlc.types.Arg(Int, graphql_name='lid', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.list_of('Team'), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('tmid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='tmid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('seid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='seid', default=None)),
        ('nam', sgqlc.types.Arg(String, graphql_name='nam', default=None)),
        ('act', sgqlc.types.Arg(Boolean, graphql_name='act', default=None)),
        ('divids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='divids', default=None)),
        ('conids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='conids', default=None)),
        ('istmlhrchy', sgqlc.types.Arg(Boolean, graphql_name='istmlhrchy', default=None)),
        ('is_special', sgqlc.types.Arg(Boolean, graphql_name='isSpecial', default=None)),
))
    )
    division_teams = sgqlc.types.Field(sgqlc.types.list_of('Team'), graphql_name='divisionTeams', args=sgqlc.types.ArgDict((
        ('divid', sgqlc.types.Arg(Int, graphql_name='divid', default=None)),
        ('divname', sgqlc.types.Arg(String, graphql_name='divname', default=None)),
        ('seid', sgqlc.types.Arg(Int, graphql_name='seid', default=None)),
        ('act', sgqlc.types.Arg(Boolean, graphql_name='act', default=None)),
))
    )
    season_teams = sgqlc.types.Field(sgqlc.types.list_of('TeamByLeague'), graphql_name='seasonTeams', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='lid', default=None)),
))
    )
    team_rosters = sgqlc.types.Field(sgqlc.types.list_of('TeamRoster'), graphql_name='teamRosters', args=sgqlc.types.ArgDict((
        ('tmid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='tmid', default=None)),
        ('seid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='seid', default=None)),
        ('pid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='pid', default=None)),
        ('act', sgqlc.types.Arg(Boolean, graphql_name='act', default=None)),
        ('all', sgqlc.types.Arg(Boolean, graphql_name='all', default=None)),
))
    )
    league_hierarchy = sgqlc.types.Field(sgqlc.types.list_of(LeagueHierarchy), graphql_name='leagueHierarchy', args=sgqlc.types.ArgDict((
        ('conference_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='conferenceIds', default=None)),
        ('division_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='divisionIds', default=None)),
        ('league_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='leagueIds', default=None)),
        ('event_date', sgqlc.types.Arg(Float, graphql_name='eventDate', default=None)),
))
    )
    participant = sgqlc.types.Field(Participant, graphql_name='participant', args=sgqlc.types.ArgDict((
        ('partid', sgqlc.types.Arg(Int, graphql_name='partid', default=None)),
        ('eid', sgqlc.types.Arg(Int, graphql_name='eid', default=None)),
        ('ptid', sgqlc.types.Arg(Int, graphql_name='ptid', default=None)),
))
    )
    participants = sgqlc.types.Field(sgqlc.types.list_of(Participant), graphql_name='participants', args=sgqlc.types.ArgDict((
        ('partid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partid', default=None)),
        ('eid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eid', default=None)),
        ('ptid', sgqlc.types.Arg(Int, graphql_name='ptid', default=None)),
))
    )
    participant_by_event = sgqlc.types.Field(sgqlc.types.list_of(ParticipantByEvent), graphql_name='participantByEvent', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('ptid', sgqlc.types.Arg(Int, graphql_name='ptid', default=None)),
        ('seid', sgqlc.types.Arg(Int, graphql_name='seid', default=None)),
))
    )
    events_info_by_participant = sgqlc.types.Field(sgqlc.types.list_of(EventInfoByParticipant), graphql_name='eventsInfoByParticipant', args=sgqlc.types.ArgDict((
        ('partid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partid', default=None)),
        ('tmid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='tmid', default=None)),
        ('ptid', sgqlc.types.Arg(Int, graphql_name='ptid', default=None)),
        ('seid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='seid', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
))
    )
    matchups = sgqlc.types.Field(sgqlc.types.list_of(MatchupId), graphql_name='matchups', args=sgqlc.types.ArgDict((
        ('participant_id1', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='participantId1', default=None)),
        ('participant_id2', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='participantId2', default=None)),
        ('home_participant_id', sgqlc.types.Arg(Int, graphql_name='homeParticipantId', default=None)),
))
    )
    last_matchups_by_participants = sgqlc.types.Field(MatchupEvents, graphql_name='lastMatchupsByParticipants', args=sgqlc.types.ArgDict((
        ('participant_id1', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='participantId1', default=None)),
        ('participant_id2', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='participantId2', default=None)),
        ('home_participant_id', sgqlc.types.Arg(Int, graphql_name='homeParticipantId', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('mtid', sgqlc.types.Arg(Int, graphql_name='mtid', default=None)),
))
    )
    get_event_roster_by_events = sgqlc.types.Field(sgqlc.types.list_of(EventRoster), graphql_name='getEventRosterByEvents', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
))
    )
    head_to_head_events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='headToHeadEvents', args=sgqlc.types.ArgDict((
        ('participant_id1', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='participantId1', default=None)),
        ('participant_id2', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='participantId2', default=None)),
        ('home_participant_id', sgqlc.types.Arg(Int, graphql_name='homeParticipantId', default=None)),
        ('seid', sgqlc.types.Arg(Int, graphql_name='seid', default=None)),
        ('es', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='es', default=None)),
        ('sort', sgqlc.types.Arg(sgqlc.types.non_null(SortInput), graphql_name='sort', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
        ('limit_date', sgqlc.types.Arg(Float, graphql_name='limitDate', default=None)),
        ('season_group', sgqlc.types.Arg(sgqlc.types.list_of(SEASONGROUP), graphql_name='seasonGroup', default=None)),
))
    )
    next_events_by_participant = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='nextEventsByParticipant', args=sgqlc.types.ArgDict((
        ('start_date', sgqlc.types.Arg(Float, graphql_name='startDate', default=None)),
        ('partid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='partid', default=None)),
        ('seid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='seid', default=None)),
        ('es', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='es', default=None)),
        ('time_limit', sgqlc.types.Arg(Int, graphql_name='timeLimit', default=None)),
))
    )
    event_filter_groups = sgqlc.types.Field(sgqlc.types.list_of(EventFilterGroup), graphql_name='eventFilterGroups', args=sgqlc.types.ArgDict((
        ('efgids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='efgids', default=None)),
        ('sitid', sgqlc.types.Arg(Int, graphql_name='sitid', default=None)),
        ('time_zone_offset', sgqlc.types.Arg(Float, graphql_name='timeZoneOffset', default=None)),
        ('startdate', sgqlc.types.Arg(Float, graphql_name='startdate', default=None)),
        ('show_live', sgqlc.types.Arg(ShowLive, graphql_name='showLive', default=None)),
        ('mtid', sgqlc.types.Arg(Int, graphql_name='mtid', default=None)),
        ('active', sgqlc.types.Arg(Boolean, graphql_name='active', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
        ('use_exact_start_date', sgqlc.types.Arg(Boolean, graphql_name='useExactStartDate', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('hours_range', sgqlc.types.Arg(Int, graphql_name='hoursRange', default=None)),
        ('market_types', sgqlc.types.Arg(sgqlc.types.list_of(EventFilterGroupMarketTypeSetting), graphql_name='marketTypes', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
))
    )
    events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='events', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(Int, graphql_name='rid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('market_type_format', sgqlc.types.Arg(String, graphql_name='marketTypeFormat', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('distinct', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='distinct', default=None)),
        ('type', sgqlc.types.Arg(TypeInput, graphql_name='type', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('group', sgqlc.types.Arg(GroupInput, graphql_name='group', default=None)),
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
        ('es', sgqlc.types.Arg(String, graphql_name='es', default=None)),
))
    )
    events_by_sport = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='eventsBySport', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('market_type_format', sgqlc.types.Arg(String, graphql_name='marketTypeFormat', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('start_date', sgqlc.types.Arg(Float, graphql_name='startDate', default=None)),
        ('hours_range', sgqlc.types.Arg(Int, graphql_name='hoursRange', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Int, graphql_name='timezoneOffset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
))
    )
    events_by_sport_v2 = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='eventsBySportV2', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('market_type_format', sgqlc.types.Arg(String, graphql_name='marketTypeFormat', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('start_date', sgqlc.types.Arg(Float, graphql_name='startDate', default=None)),
        ('hours_range', sgqlc.types.Arg(Int, graphql_name='hoursRange', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Int, graphql_name='timezoneOffset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
))
    )
    events_by_date_deprecate = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='eventsByDateDeprecate', args=sgqlc.types.ArgDict((
        ('start_date', sgqlc.types.Arg(Float, graphql_name='startDate', default=None)),
        ('hours_range', sgqlc.types.Arg(Int, graphql_name='hoursRange', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Float, graphql_name='timezoneOffset', default=None)),
        ('egid', sgqlc.types.Arg(Int, graphql_name='egid', default=None)),
        ('eid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('rid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('nof', sgqlc.types.Arg(Boolean, graphql_name='nof', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('market_type_format', sgqlc.types.Arg(String, graphql_name='marketTypeFormat', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('provider_acount_opener', sgqlc.types.Arg(Int, graphql_name='providerAcountOpener', default=None)),
        ('get_all_in_event_group', sgqlc.types.Arg(Boolean, graphql_name='getAllInEventGroup', default=None)),
        ('show_live', sgqlc.types.Arg(ShowLive, graphql_name='showLive', default=None)),
        ('eventtoshow', sgqlc.types.Arg(Int, graphql_name='eventtoshow', default=None)),
        ('include_all_events', sgqlc.types.Arg(Boolean, graphql_name='includeAllEvents', default=None)),
        ('domain_id', sgqlc.types.Arg(Int, graphql_name='domainId', default=None)),
        ('events_with_ranked_participants', sgqlc.types.Arg(Boolean, graphql_name='eventsWithRankedParticipants', default=None)),
        ('only_ranked', sgqlc.types.Arg(Boolean, graphql_name='onlyRanked', default=None)),
        ('conference_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='conferenceIds', default=None)),
        ('division_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='divisionIds', default=None)),
        ('es', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='es', default=None)),
        ('trunc_date', sgqlc.types.Arg(Boolean, graphql_name='truncDate', default=None)),
))
    )
    events_by_date = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='eventsByDate', args=sgqlc.types.ArgDict((
        ('start_date', sgqlc.types.Arg(Float, graphql_name='startDate', default=None)),
        ('hours_range', sgqlc.types.Arg(Int, graphql_name='hoursRange', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Float, graphql_name='timezoneOffset', default=None)),
        ('egid', sgqlc.types.Arg(Int, graphql_name='egid', default=None)),
        ('eid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('rid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('nof', sgqlc.types.Arg(Boolean, graphql_name='nof', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('market_type_format', sgqlc.types.Arg(String, graphql_name='marketTypeFormat', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('provider_acount_opener', sgqlc.types.Arg(Int, graphql_name='providerAcountOpener', default=None)),
        ('get_all_in_event_group', sgqlc.types.Arg(Boolean, graphql_name='getAllInEventGroup', default=None)),
        ('show_live', sgqlc.types.Arg(ShowLive, graphql_name='showLive', default=None)),
        ('eventtoshow', sgqlc.types.Arg(Int, graphql_name='eventtoshow', default=None)),
        ('include_all_events', sgqlc.types.Arg(Boolean, graphql_name='includeAllEvents', default=None)),
        ('domain_id', sgqlc.types.Arg(Int, graphql_name='domainId', default=None)),
        ('events_with_ranked_participants', sgqlc.types.Arg(Boolean, graphql_name='eventsWithRankedParticipants', default=None)),
        ('only_ranked', sgqlc.types.Arg(Boolean, graphql_name='onlyRanked', default=None)),
        ('conference_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='conferenceIds', default=None)),
        ('division_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='divisionIds', default=None)),
        ('es', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='es', default=None)),
        ('trunc_date', sgqlc.types.Arg(Boolean, graphql_name='truncDate', default=None)),
))
    )
    events_by_date_new = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='eventsByDateNew', args=sgqlc.types.ArgDict((
        ('start_date', sgqlc.types.Arg(Float, graphql_name='startDate', default=None)),
        ('hours_range', sgqlc.types.Arg(Int, graphql_name='hoursRange', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('fast_forward', sgqlc.types.Arg(Boolean, graphql_name='fastForward', default=None)),
        ('fast_forward_offset', sgqlc.types.Arg(Int, graphql_name='fastForwardOffset', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('only_ranked', sgqlc.types.Arg(Boolean, graphql_name='onlyRanked', default=None)),
        ('conference_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='conferenceIds', default=None)),
        ('division_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='divisionIds', default=None)),
        ('es', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='es', default=None)),
        ('spids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spids', default=None)),
        ('rids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rids', default=None)),
))
    )
    events_by_date_by_league_group = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='eventsByDateByLeagueGroup', args=sgqlc.types.ArgDict((
        ('league_groups', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(LeagueGroup)), graphql_name='leagueGroups', default=None)),
        ('start_date', sgqlc.types.Arg(Float, graphql_name='startDate', default=None)),
        ('hours_range', sgqlc.types.Arg(Int, graphql_name='hoursRange', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Float, graphql_name='timezoneOffset', default=None)),
        ('egid', sgqlc.types.Arg(Int, graphql_name='egid', default=None)),
        ('rid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('nof', sgqlc.types.Arg(Boolean, graphql_name='nof', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('market_type_format', sgqlc.types.Arg(String, graphql_name='marketTypeFormat', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('provider_acount_opener', sgqlc.types.Arg(Int, graphql_name='providerAcountOpener', default=None)),
        ('get_all_in_event_group', sgqlc.types.Arg(Boolean, graphql_name='getAllInEventGroup', default=None)),
        ('es', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='es', default=None)),
))
    )
    event_markets = sgqlc.types.Field(EventMarkets, graphql_name='eventMarkets', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(Int, graphql_name='eid', default=None)),
))
    )
    events_by_league_group = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='eventsByLeagueGroup', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eid', default=None)),
        ('league_groups', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(LeagueGroup)), graphql_name='leagueGroups', default=None)),
        ('rid', sgqlc.types.Arg(Int, graphql_name='rid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('market_type_format', sgqlc.types.Arg(String, graphql_name='marketTypeFormat', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('distinct', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='distinct', default=None)),
        ('type', sgqlc.types.Arg(TypeInput, graphql_name='type', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('group', sgqlc.types.Arg(GroupInput, graphql_name='group', default=None)),
        ('provider_acount_opener', sgqlc.types.Arg(Int, graphql_name='providerAcountOpener', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('es', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='es', default=None)),
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
))
    )
    events_v2 = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='eventsV2', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(Int, graphql_name='rid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('market_type_format', sgqlc.types.Arg(String, graphql_name='marketTypeFormat', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('distinct', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='distinct', default=None)),
        ('type', sgqlc.types.Arg(TypeInput, graphql_name='type', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('group', sgqlc.types.Arg(GroupInput, graphql_name='group', default=None)),
        ('provider_acount_opener', sgqlc.types.Arg(Int, graphql_name='providerAcountOpener', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('domain_id', sgqlc.types.Arg(Int, graphql_name='domainId', default=None)),
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
))
    )
    events_by_event_group = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='eventsByEventGroup', args=sgqlc.types.ArgDict((
        ('egid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='egid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='mtid', default=None)),
        ('seid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='seid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
))
    )
    events_by_event_group_v2 = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='eventsByEventGroupV2', args=sgqlc.types.ArgDict((
        ('egid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='egid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='mtid', default=None)),
        ('seid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='seid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('provider_acount_opener', sgqlc.types.Arg(Int, graphql_name='providerAcountOpener', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('only_ranked', sgqlc.types.Arg(Boolean, graphql_name='onlyRanked', default=None)),
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
        ('conference_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='conferenceIds', default=None)),
        ('division_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='divisionIds', default=None)),
))
    )
    nearest_season_events = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='nearestSeasonEvents', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(Int, graphql_name='lid', default=None)),
        ('mtid', sgqlc.types.Arg(Int, graphql_name='mtid', default=None)),
        ('seid', sgqlc.types.Arg(Int, graphql_name='seid', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Float, graphql_name='timezoneOffset', default=None)),
        ('provider_acount_opener', sgqlc.types.Arg(Int, graphql_name='providerAcountOpener', default=None)),
        ('es', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='es', default=None)),
))
    )
    leagues_with_events = sgqlc.types.Field(sgqlc.types.list_of(LeagueWithSettings), graphql_name='leaguesWithEvents', args=sgqlc.types.ArgDict((
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Float, graphql_name='timezoneOffset', default=None)),
        ('league_filter', sgqlc.types.Arg(sgqlc.types.non_null(LeagueFilter), graphql_name='leagueFilter', default=None)),
))
    )
    events_region_by_sport = sgqlc.types.Field(EventRegion, graphql_name='eventsRegionBySport', args=sgqlc.types.ArgDict((
        ('spid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='spid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
))
    )
    events_dates_count = sgqlc.types.Field(sgqlc.types.list_of(EventDateCount), graphql_name='eventsDatesCount', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('spid', sgqlc.types.Arg(Int, graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(Int, graphql_name='rid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('mtid', sgqlc.types.Arg(Int, graphql_name='mtid', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('group', sgqlc.types.Arg(GroupInput, graphql_name='group', default=None)),
        ('es', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='es', default=None)),
))
    )
    events_dates_count_summary = sgqlc.types.Field(sgqlc.types.list_of(EventDateCount), graphql_name='eventsDatesCountSummary', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('spid', sgqlc.types.Arg(Int, graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(Int, graphql_name='rid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('mtid', sgqlc.types.Arg(Int, graphql_name='mtid', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('group', sgqlc.types.Arg(GroupInput, graphql_name='group', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Float, graphql_name='timezoneOffset', default=None)),
))
    )
    calendar_events_by_event_group = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='calendarEventsByEventGroup', args=sgqlc.types.ArgDict((
        ('egid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='egid', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('lid', sgqlc.types.Arg(Int, graphql_name='lid', default=None)),
        ('spid', sgqlc.types.Arg(Int, graphql_name='spid', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
))
    )
    calendar_events_by_event_group_v2 = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='calendarEventsByEventGroupV2', args=sgqlc.types.ArgDict((
        ('egid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='egid', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('lid', sgqlc.types.Arg(Int, graphql_name='lid', default=None)),
        ('spid', sgqlc.types.Arg(Int, graphql_name='spid', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
))
    )
    get_updated_events = sgqlc.types.Field(EventsWithMaxSequence, graphql_name='getUpdatedEvents', args=sgqlc.types.ArgDict((
        ('event_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eventIds', default=None)),
        ('sequence', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sequence', default=None)),
))
    )
    sports_with_live_events = sgqlc.types.Field(sgqlc.types.list_of('Sports'), graphql_name='sportsWithLiveEvents', args=sgqlc.types.ArgDict((
        ('days', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='days', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='spid', default=None)),
))
    )
    event_groups_by_leagues = sgqlc.types.Field(sgqlc.types.list_of(EventGroup), graphql_name='eventGroupsByLeagues', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='lid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
))
    )
    event_groups_by_sport = sgqlc.types.Field(sgqlc.types.list_of(EventGroup), graphql_name='eventGroupsBySport', args=sgqlc.types.ArgDict((
        ('spid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='spid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('rid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rid', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Int, graphql_name='timezoneOffset', default=None)),
        ('exact_date', sgqlc.types.Arg(Boolean, graphql_name='exactDate', default=None)),
))
    )
    events_by_team_id = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='eventsByTeamId', args=sgqlc.types.ArgDict((
        ('tmid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='tmid', default=None)),
        ('seid', sgqlc.types.Arg(Int, graphql_name='seid', default=None)),
        ('start_date', sgqlc.types.Arg(Float, graphql_name='startDate', default=None)),
        ('hours_range', sgqlc.types.Arg(Int, graphql_name='hoursRange', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Float, graphql_name='timezoneOffset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
))
    )
    related_events = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='relatedEvents', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='eid', default=None)),
        ('timezone_offset', sgqlc.types.Arg(Float, graphql_name='timezoneOffset', default=None)),
        ('group_by', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='groupBy', default=None)),
))
    )
    events_location = sgqlc.types.Field(sgqlc.types.list_of(EventLocation), graphql_name='eventsLocation', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='eid', default=None)),
))
    )
    upcoming_events = sgqlc.types.Field(sgqlc.types.list_of(Event), graphql_name='upcomingEvents', args=sgqlc.types.ArgDict((
        ('lids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='lids', default=None)),
        ('start_date', sgqlc.types.Arg(Float, graphql_name='startDate', default=None)),
        ('hours_range', sgqlc.types.Arg(Float, graphql_name='hoursRange', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('location', sgqlc.types.Arg(GeolocationIntput, graphql_name='location', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('participant_id', sgqlc.types.Arg(Int, graphql_name='participantId', default=None)),
        ('seid', sgqlc.types.Arg(Int, graphql_name='seid', default=None)),
))
    )
    upcoming_events_new = sgqlc.types.Field(sgqlc.types.list_of(EventsByParticipant), graphql_name='upcomingEventsNew', args=sgqlc.types.ArgDict((
        ('lids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='lids', default=None)),
        ('participant_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='participantIds', default=None)),
        ('seid', sgqlc.types.Arg(Int, graphql_name='seid', default=None)),
        ('limit_by_participant', sgqlc.types.Arg(Int, graphql_name='limitByParticipant', default=None)),
        ('start_date', sgqlc.types.Arg(Float, graphql_name='startDate', default=None)),
        ('hours_range', sgqlc.types.Arg(Float, graphql_name='hoursRange', default=None)),
        ('show_empty_events', sgqlc.types.Arg(Boolean, graphql_name='showEmptyEvents', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
))
    )
    get_top_events_by_sportsbook = sgqlc.types.Field(EventsWithMaxSequences, graphql_name='getTopEventsBySportsbook', args=sgqlc.types.ArgDict((
        ('start_date', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='startDate', default=None)),
        ('sbid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='sbid', default=None)),
        ('top_games_limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='topGamesLimit', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('hours_range', sgqlc.types.Arg(Int, graphql_name='hoursRange', default=None)),
))
    )
    get_event_ids_by_slug = sgqlc.types.Field(EventIdsSlugInfo, graphql_name='getEventIdsBySlug', args=sgqlc.types.ArgDict((
        ('slg', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slg', default=None)),
        ('act_tim', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='actTim', default=None)),
))
    )
    league_setting = sgqlc.types.Field(LeagueSetting, graphql_name='leagueSetting', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='lid', default=None)),
))
    )
    leagues_setting = sgqlc.types.Field(sgqlc.types.list_of(LeagueSetting), graphql_name='leaguesSetting', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(Int, graphql_name='lid', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
        ('alias', sgqlc.types.Arg(String, graphql_name='alias', default=None)),
        ('rotation', sgqlc.types.Arg(Boolean, graphql_name='rotation', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
))
    )
    league_settings_v2 = sgqlc.types.Field(sgqlc.types.list_of(LeagueV2), graphql_name='leagueSettingsV2', args=sgqlc.types.ArgDict((
        ('spid', sgqlc.types.Arg(Int, graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(Int, graphql_name='rid', default=None)),
        ('sitid', sgqlc.types.Arg(Int, graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(Int, graphql_name='did', default=None)),
        ('merge', sgqlc.types.Arg(Boolean, graphql_name='merge', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
))
    )
    league_markets = sgqlc.types.Field(sgqlc.types.list_of(LeagueMarket), graphql_name='leagueMarkets', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
))
    )
    leagues_with_settings = sgqlc.types.Field(sgqlc.types.list_of(LeagueWithSettings), graphql_name='leaguesWithSettings', args=sgqlc.types.ArgDict((
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
))
    )
    get_leagues_with_settings_v2 = sgqlc.types.Field(sgqlc.types.list_of(LeagueWithSettingsV2), graphql_name='getLeaguesWithSettingsV2', args=sgqlc.types.ArgDict((
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
))
    )
    league = sgqlc.types.Field(LeagueWithSettings, graphql_name='league', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='lid', default=None)),
))
    )
    leagues = sgqlc.types.Field(sgqlc.types.list_of(LeagueWithSettings), graphql_name='leagues', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('spid', sgqlc.types.Arg(Int, graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(Int, graphql_name='rid', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
        ('alias', sgqlc.types.Arg(String, graphql_name='alias', default=None)),
        ('rotation', sgqlc.types.Arg(Boolean, graphql_name='rotation', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('distinct', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='distinct', default=None)),
))
    )
    leagues_by_id = sgqlc.types.Field(sgqlc.types.list_of(League), graphql_name='leaguesById', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='lid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('rid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rid', default=None)),
))
    )
    sport_setting = sgqlc.types.Field('SportSetting', graphql_name='sportSetting', args=sgqlc.types.ArgDict((
        ('spid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='spid', default=None)),
        ('sitid', sgqlc.types.Arg(String, graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(String, graphql_name='did', default=None)),
))
    )
    sport_settings_v2 = sgqlc.types.Field(sgqlc.types.list_of('SportV2'), graphql_name='sportSettingsV2', args=sgqlc.types.ArgDict((
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
))
    )
    get_sports_with_settings_v2 = sgqlc.types.Field(sgqlc.types.list_of('SportWithSettings'), graphql_name='getSportsWithSettingsV2', args=sgqlc.types.ArgDict((
        ('spids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spids', default=None)),
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
))
    )
    sport = sgqlc.types.Field('Sport', graphql_name='sport', args=sgqlc.types.ArgDict((
        ('spid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='spid', default=None)),
))
    )
    sports = sgqlc.types.Field(sgqlc.types.list_of('Sport'), graphql_name='sports', args=sgqlc.types.ArgDict((
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
        ('alias', sgqlc.types.Arg(String, graphql_name='alias', default=None)),
        ('mode', sgqlc.types.Arg(String, graphql_name='mode', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    get_leagues_and_regions_by_sport = sgqlc.types.Field(sgqlc.types.list_of(LeaguesAndRegionsBySport), graphql_name='getLeaguesAndRegionsBySport', args=sgqlc.types.ArgDict((
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
        ('sport_enabled', sgqlc.types.Arg(Boolean, graphql_name='sportEnabled', default=None)),
        ('league_enabled', sgqlc.types.Arg(Boolean, graphql_name='leagueEnabled', default=None)),
))
    )
    conferences = sgqlc.types.Field(sgqlc.types.list_of(Conference), graphql_name='conferences', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
))
    )
    divisions = sgqlc.types.Field(sgqlc.types.list_of(Division), graphql_name='divisions', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='ids', default=None)),
))
    )
    region = sgqlc.types.Field('Region', graphql_name='region', args=sgqlc.types.ArgDict((
        ('rid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='rid', default=None)),
))
    )
    regions = sgqlc.types.Field(sgqlc.types.list_of('Region'), graphql_name='regions', args=sgqlc.types.ArgDict((
        ('rid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='rid', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    regions_by_sport = sgqlc.types.Field('RegionsBySport', graphql_name='regionsBySport', args=sgqlc.types.ArgDict((
        ('spid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='spid', default=None)),
        ('dt', sgqlc.types.Arg(InputQueryFloat, graphql_name='dt', default=None)),
        ('mtid', sgqlc.types.Arg(Int, graphql_name='mtid', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
))
    )
    scores = sgqlc.types.Field(sgqlc.types.list_of('Score'), graphql_name='scores', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('partid', sgqlc.types.Arg(Int, graphql_name='partid', default=None)),
        ('pn', sgqlc.types.Arg(Int, graphql_name='pn', default=None)),
))
    )
    get_updated_scores = sgqlc.types.Field('ScoreWithMaxSequence', graphql_name='getUpdatedScores', args=sgqlc.types.ArgDict((
        ('event_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eventIds', default=None)),
        ('sequence', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sequence', default=None)),
))
    )
    statistic = sgqlc.types.Field('Statistic', graphql_name='statistic', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='eid', default=None)),
        ('partid', sgqlc.types.Arg(Int, graphql_name='partid', default=None)),
        ('pid', sgqlc.types.Arg(Int, graphql_name='pid', default=None)),
        ('typ', sgqlc.types.Arg(String, graphql_name='typ', default=None)),
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
))
    )
    statistics = sgqlc.types.Field(sgqlc.types.list_of('Statistic'), graphql_name='statistics', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('partid', sgqlc.types.Arg(Int, graphql_name='partid', default=None)),
        ('pid', sgqlc.types.Arg(Int, graphql_name='pid', default=None)),
        ('typ', sgqlc.types.Arg(String, graphql_name='typ', default=None)),
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
))
    )
    get_updated_statistics = sgqlc.types.Field('StatisticWithMaxSequence', graphql_name='getUpdatedStatistics', args=sgqlc.types.ArgDict((
        ('event_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eventIds', default=None)),
        ('sequence', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='sequence', default=None)),
        ('sgid', sgqlc.types.Arg(Int, graphql_name='sgid', default=None)),
))
    )
    market_type = sgqlc.types.Field(MarketTypeWithSettings, graphql_name='marketType', args=sgqlc.types.ArgDict((
        ('mtid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='mtid', default=None)),
        ('spid', sgqlc.types.Arg(Int, graphql_name='spid', default=None)),
))
    )
    market_types = sgqlc.types.Field(sgqlc.types.list_of(MarketTypeWithSettings), graphql_name='marketTypes', args=sgqlc.types.ArgDict((
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('sitid', sgqlc.types.Arg(String, graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(String, graphql_name='did', default=None)),
        ('merge', sgqlc.types.Arg(Boolean, graphql_name='merge', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
))
    )
    outright_market_types = sgqlc.types.Field(sgqlc.types.list_of(MarketTypeWithSettings), graphql_name='outrightMarketTypes', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='lid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='spid', default=None)),
        ('dt', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dt', default=None)),
        ('hl', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='hl', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
))
    )
    market_types_by_id = sgqlc.types.Field(sgqlc.types.list_of(MarketType), graphql_name='marketTypesById', args=sgqlc.types.ArgDict((
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
))
    )
    current_lines = sgqlc.types.Field(sgqlc.types.list_of(JSON), graphql_name='currentLines', args=sgqlc.types.ArgDict((
        ('catid', sgqlc.types.Arg(Int, graphql_name='catid', default=None)),
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('boid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='boid', default=None)),
        ('partid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partid', default=None)),
        ('sbid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='sbid', default=None)),
        ('paid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='paid', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('distinct', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='distinct', default=None)),
        ('group', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='group', default=None)),
        ('market_type_format', sgqlc.types.Arg(String, graphql_name='marketTypeFormat', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('need_sbid', sgqlc.types.Arg(Boolean, graphql_name='needSbid', default=None)),
))
    )
    best_lines = sgqlc.types.Field(sgqlc.types.list_of(BestLine), graphql_name='bestLines', args=sgqlc.types.ArgDict((
        ('catid', sgqlc.types.Arg(Int, graphql_name='catid', default=None)),
        ('paid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='paid', default=None)),
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
))
    )
    get_updated_current_lines = sgqlc.types.Field(CurrentLinesWithMaxSequence, graphql_name='getUpdatedCurrentLines', args=sgqlc.types.ArgDict((
        ('event_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eventIds', default=None)),
        ('sequence', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='sequence', default=None)),
        ('mtid', sgqlc.types.Arg(Int, graphql_name='mtid', default=None)),
))
    )
    get_current_lines_group_by_event_market = sgqlc.types.Field(sgqlc.types.list_of(EventMarketLine), graphql_name='getCurrentLinesGroupByEventMarket', args=sgqlc.types.ArgDict((
        ('sequence', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='sequence', default=None)),
        ('sequence_range', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sequenceRange', default=None)),
))
    )
    opening_lines = sgqlc.types.Field(sgqlc.types.list_of(JSON), graphql_name='openingLines', args=sgqlc.types.ArgDict((
        ('catid', sgqlc.types.Arg(Int, graphql_name='catid', default=None)),
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='mtid', default=None)),
        ('market_type_format', sgqlc.types.Arg(String, graphql_name='marketTypeFormat', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('paid', sgqlc.types.Arg(Int, graphql_name='paid', default=None)),
))
    )
    consensus = sgqlc.types.Field(sgqlc.types.list_of(Consensus), graphql_name='consensus', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('sequence', sgqlc.types.Arg(Int, graphql_name='sequence', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
))
    )
    updated_consensus = sgqlc.types.Field(ConsensusWithMaxSequence, graphql_name='updatedConsensus', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('sequence', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sequence', default=None)),
))
    )
    consensus_history = sgqlc.types.Field(sgqlc.types.list_of(Consensus), graphql_name='consensusHistory', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('sort_by', sgqlc.types.Arg(String, graphql_name='sortBy', default=None)),
        ('order', sgqlc.types.Arg(String, graphql_name='order', default=None)),
))
    )
    weather = sgqlc.types.Field(sgqlc.types.list_of('WeatherOutput'), graphql_name='weather', args=sgqlc.types.ArgDict((
        ('cities', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(LocationInput)), graphql_name='cities', default=None)),
        ('number_of_days', sgqlc.types.Arg(Int, graphql_name='numberOfDays', default=None)),
        ('ti', sgqlc.types.Arg(Int, graphql_name='ti', default=None)),
))
    )
    week_weather_forecast = sgqlc.types.Field(sgqlc.types.list_of('weekWeatherOutput'), graphql_name='weekWeatherForecast', args=sgqlc.types.ArgDict((
        ('place', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='place', default=None)),
        ('dt', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dt', default=None)),
))
    )
    event_group_by_event = sgqlc.types.Field(sgqlc.types.list_of(EventGroup), graphql_name='eventGroupByEvent', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
))
    )
    event_groups_by_league = sgqlc.types.Field(sgqlc.types.list_of(EventGroup), graphql_name='eventGroupsByLeague', args=sgqlc.types.ArgDict((
        ('lid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='lid', default=None)),
        ('hl', sgqlc.types.Arg(Boolean, graphql_name='hl', default=None)),
        ('ic', sgqlc.types.Arg(Boolean, graphql_name='ic', default=None)),
        ('dt', sgqlc.types.Arg(RangeInput, graphql_name='dt', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
))
    )
    events_groups_by_season = sgqlc.types.Field(sgqlc.types.list_of(EventGroupBySeason), graphql_name='eventsGroupsBySeason', args=sgqlc.types.ArgDict((
        ('seids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='seids', default=None)),
        ('timezone_offset', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='timezoneOffset', default=None)),
))
    )
    get_event_tags = sgqlc.types.Field(sgqlc.types.list_of(EventTag), graphql_name='getEventTags', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='eid', default=None)),
))
    )
    get_sportsbook_bonus_lists = sgqlc.types.Field(sgqlc.types.list_of('SportsbookBonusList'), graphql_name='getSportsbookBonusLists', args=sgqlc.types.ArgDict((
        ('catid', sgqlc.types.Arg(Int, graphql_name='catid', default=None)),
))
    )
    betting_options = sgqlc.types.Field(sgqlc.types.list_of(BettingOption), graphql_name='bettingOptions', args=sgqlc.types.ArgDict((
        ('boid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='boid', default=None)),
))
    )
    betting_options_by_event = sgqlc.types.Field(sgqlc.types.list_of(EventBettingOption), graphql_name='bettingOptionsByEvent', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(Int, graphql_name='mtid', default=None)),
))
    )
    bet_slip_info = sgqlc.types.Field(BetSlipInfo, graphql_name='betSlipInfo', args=sgqlc.types.ArgDict((
        ('bet_slip_args', sgqlc.types.Arg(sgqlc.types.list_of(BetSlipArgs), graphql_name='betSlipArgs', default=None)),
        ('market_type_layout', sgqlc.types.Arg(MarketTypeLayout, graphql_name='marketTypeLayout', default=None)),
))
    )
    market_type_group = sgqlc.types.Field(MarketTypeGroupWithSettings, graphql_name='marketTypeGroup', args=sgqlc.types.ArgDict((
        ('mtgid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='mtgid', default=None)),
        ('spid', sgqlc.types.Arg(Int, graphql_name='spid', default=None)),
))
    )
    market_type_groups_filtered = sgqlc.types.Field(sgqlc.types.list_of(MarketTypeGroupFiltered), graphql_name='marketTypeGroupsFiltered', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(Int, graphql_name='eid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='spid', default=None)),
        ('nam', sgqlc.types.Arg(String, graphql_name='nam', default=None)),
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
        ('sam', sgqlc.types.Arg(Boolean, graphql_name='sam', default=None)),
        ('mtgid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtgid', default=None)),
))
    )
    market_type_groups = sgqlc.types.Field(sgqlc.types.list_of(MarketTypeGroupWithSettings), graphql_name='marketTypeGroups', args=sgqlc.types.ArgDict((
        ('mtgid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtgid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(Int, graphql_name='did', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('merge', sgqlc.types.Arg(Boolean, graphql_name='merge', default=None)),
))
    )
    market_type_groups_with_market_types = sgqlc.types.Field(sgqlc.types.list_of(MarketTypeGroupWithMarketTypes), graphql_name='marketTypeGroupsWithMarketTypes', args=sgqlc.types.ArgDict((
        ('mtgid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtgid', default=None)),
))
    )
    market_type_groups_by_id = sgqlc.types.Field(sgqlc.types.list_of(MarketTypeGroup), graphql_name='marketTypeGroupsById', args=sgqlc.types.ArgDict((
        ('mtgid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtgid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='spid', default=None)),
))
    )
    max_sequences = sgqlc.types.Field(MaxSequences, graphql_name='maxSequences')
    formats = sgqlc.types.Field(sgqlc.types.list_of(OddFormat), graphql_name='formats', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('dcp', sgqlc.types.Arg(Float, graphql_name='dcp', default=None)),
        ('np', sgqlc.types.Arg(Int, graphql_name='np', default=None)),
        ('dep', sgqlc.types.Arg(Int, graphql_name='dep', default=None)),
))
    )
    sportsbook_setting = sgqlc.types.Field('SportsbookSetting', graphql_name='sportsbookSetting', args=sgqlc.types.ArgDict((
        ('sbid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sbid', default=None)),
))
    )
    sportsbook = sgqlc.types.Field('Sportsbook', graphql_name='sportsbook', args=sgqlc.types.ArgDict((
        ('sbid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sbid', default=None)),
))
    )
    sportsbooks = sgqlc.types.Field(sgqlc.types.list_of('Sportsbook'), graphql_name='sportsbooks', args=sgqlc.types.ArgDict((
        ('sitid', sgqlc.types.Arg(Int, graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(Int, graphql_name='did', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
        ('sbids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='sbids', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    sportsbooks_by_category = sgqlc.types.Field(sgqlc.types.list_of('SportsbooksByCategory'), graphql_name='sportsbooksByCategory', args=sgqlc.types.ArgDict((
        ('catid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='catid', default=None)),
))
    )
    categories = sgqlc.types.Field(sgqlc.types.list_of(Category), graphql_name='categories', args=sgqlc.types.ArgDict((
        ('sitid', sgqlc.types.Arg(Int, graphql_name='sitid', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
))
    )
    images = sgqlc.types.Field(sgqlc.types.list_of(Image), graphql_name='images', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
))
    )
    history_lines = sgqlc.types.Field(GroupedHistoryLine, graphql_name='historyLines', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='mtid', default=None)),
        ('paid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='paid', default=None)),
        ('partid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partid', default=None)),
        ('boid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='boid', default=None)),
))
    )
    line_history = sgqlc.types.Field(sgqlc.types.list_of(HistoryLine), graphql_name='lineHistory', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='mtid', default=None)),
        ('paid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='paid', default=None)),
        ('partid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partid', default=None)),
        ('boid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='boid', default=None)),
))
    )
    menu_option = sgqlc.types.Field(MenuOption, graphql_name='menuOption', args=sgqlc.types.ArgDict((
        ('mid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='mid', default=None)),
))
    )
    menu_options = sgqlc.types.Field(sgqlc.types.list_of(MenuOption), graphql_name='menuOptions', args=sgqlc.types.ArgDict((
        ('sitid', sgqlc.types.Arg(Int, graphql_name='sitid', default=None)),
        ('mid', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mid', default=None)),
        ('mbid', sgqlc.types.Arg(Int, graphql_name='mbid', default=None)),
        ('level', sgqlc.types.Arg(Int, graphql_name='level', default=None)),
))
    )
    search_event = sgqlc.types.Field(sgqlc.types.list_of(EventCatalog), graphql_name='searchEvent', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='query', default=None)),
))
    )
    multiple_search = sgqlc.types.Field(MultipleResult, graphql_name='multipleSearch', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='query', default=None)),
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
))
    )
    domains = sgqlc.types.Field(sgqlc.types.list_of(Domain), graphql_name='domains', args=sgqlc.types.ArgDict((
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
))
    )
    plays = sgqlc.types.Field(sgqlc.types.list_of(Play), graphql_name='plays', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('pgid', sgqlc.types.Arg(Int, graphql_name='pgid', default=None)),
        ('limit_last_seq', sgqlc.types.Arg(Int, graphql_name='limitLastSeq', default=None)),
        ('pgid_when_finished', sgqlc.types.Arg(Int, graphql_name='pgidWhenFinished', default=None)),
))
    )
    plays_v2 = sgqlc.types.Field(PlaysWithMaxSequence, graphql_name='playsV2', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('sequence', sgqlc.types.Arg(Int, graphql_name='sequence', default=None)),
        ('pgid', sgqlc.types.Arg(Int, graphql_name='pgid', default=None)),
        ('limit_last_seq', sgqlc.types.Arg(Int, graphql_name='limitLastSeq', default=None)),
))
    )
    updated_plays = sgqlc.types.Field(PlaysWithMaxSequence, graphql_name='updatedPlays', args=sgqlc.types.ArgDict((
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('sequence', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sequence', default=None)),
        ('pgid', sgqlc.types.Arg(Int, graphql_name='pgid', default=None)),
))
    )
    sportbooks_by_category = sgqlc.types.Field(sgqlc.types.list_of('SportbooksByCategory'), graphql_name='sportbooksByCategory', args=sgqlc.types.ArgDict((
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
        ('cid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='cid', default=None)),
        ('spid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='spid', default=None)),
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
        ('sort_with', sgqlc.types.Arg(Boolean, graphql_name='sortWith', default=None)),
        ('famid', sgqlc.types.Arg(Int, graphql_name='famid', default=None)),
))
    )
    statistics_by_groups = sgqlc.types.Field(sgqlc.types.list_of('StatisticByGroup'), graphql_name='statisticsByGroups', args=sgqlc.types.ArgDict((
        ('statistic_group', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='statisticGroup', default=None)),
        ('team_by_league_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='teamByLeagueIds', default=None)),
        ('participant_by_event_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='participantByEventIds', default=None)),
        ('identities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='identities', default=None)),
        ('eids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eids', default=None)),
        ('tmids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='tmids', default=None)),
        ('partids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partids', default=None)),
        ('seids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='seids', default=None)),
        ('ent', sgqlc.types.Arg(sgqlc.types.list_of(ENT), graphql_name='ent', default=None)),
))
    )
    statistics_by_event = sgqlc.types.Field(sgqlc.types.list_of('StatisticByGroup'), graphql_name='statisticsByEvent', args=sgqlc.types.ArgDict((
        ('eids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eids', default=None)),
        ('idtys', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='idtys', default=None)),
        ('grps', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='grps', default=None)),
        ('stats', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='stats', default=None)),
        ('entrids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='entrids', default=None)),
        ('entgids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='entgids', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('order_by', sgqlc.types.Arg(SortInput, graphql_name='orderBy', default=None)),
))
    )
    statistics_by_season = sgqlc.types.Field(sgqlc.types.list_of('StatisticByGroup'), graphql_name='statisticsBySeason', args=sgqlc.types.ArgDict((
        ('seid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='seid', default=None)),
        ('idty', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='idty', default=None)),
        ('grp', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='grp', default=None)),
        ('stat', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='stat', default=None)),
        ('entrid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='entrid', default=None)),
        ('entgid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='entgid', default=None)),
))
    )
    team_statistics = sgqlc.types.Field(sgqlc.types.list_of('StatisticByGroup'), graphql_name='teamStatistics', args=sgqlc.types.ArgDict((
        ('statistic_group', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='statisticGroup', default=None)),
        ('team_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='teamIds', default=None)),
        ('season_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='seasonIds', default=None)),
))
    )
    statistics_betting_odds_trends = sgqlc.types.Field(sgqlc.types.list_of('Trends'), graphql_name='statisticsBettingOddsTrends', args=sgqlc.types.ArgDict((
        ('participant_by_event_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='participantByEventIds', default=None)),
        ('ws', sgqlc.types.Arg(String, graphql_name='ws', default=None)),
        ('ls', sgqlc.types.Arg(String, graphql_name='ls', default=None)),
))
    )
    statistics_umpire = sgqlc.types.Field(sgqlc.types.list_of('StatisticByGroup'), graphql_name='statisticsUmpire', args=sgqlc.types.ArgDict((
        ('event_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='eventId', default=None)),
        ('season_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='seasonId', default=None)),
))
    )
    top_performers = sgqlc.types.Field('TopPerformer', graphql_name='topPerformers', args=sgqlc.types.ArgDict((
        ('spid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='spid', default=None)),
        ('stgnam', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='stgnam', default=None)),
        ('seid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='seid', default=None)),
        ('tmids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='tmids', default=None)),
        ('idty', sgqlc.types.Arg(sgqlc.types.non_null(TopPerformerIdentity), graphql_name='idty', default=None)),
))
    )
    get_active_event_filter_groups = sgqlc.types.Field(sgqlc.types.list_of(EventFilterGroupLegacy), graphql_name='getActiveEventFilterGroups', args=sgqlc.types.ArgDict((
        ('egid', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='egid', default=None)),
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
))
    )
    events_by_event_filter_group = sgqlc.types.Field(EventFilterGroupWithEvents, graphql_name='eventsByEventFilterGroup', args=sgqlc.types.ArgDict((
        ('egid', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='egid', default=None)),
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
        ('did', sgqlc.types.Arg(Int, graphql_name='did', default=None)),
        ('mtid', sgqlc.types.Arg(Int, graphql_name='mtid', default=None)),
))
    )
    event_filter_group_with_event_ids = sgqlc.types.Field(EventFilterGroupWithEventIds, graphql_name='eventFilterGroupWithEventIds', args=sgqlc.types.ArgDict((
        ('egid', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='egid', default=None)),
        ('did', sgqlc.types.Arg(Int, graphql_name='did', default=None)),
        ('sitid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='sitid', default=None)),
))
    )
    events_carousel = sgqlc.types.Field(EventsCarousel, graphql_name='eventsCarousel', args=sgqlc.types.ArgDict((
        ('sportbooks_by_category_args', sgqlc.types.Arg(SportbooksByCategoryArgs, graphql_name='sportbooksByCategoryArgs', default=None)),
        ('event_filter_groups_args', sgqlc.types.Arg(EventFilterGroupsArgs, graphql_name='eventFilterGroupsArgs', default=None)),
))
    )
    live_lines = sgqlc.types.Field(sgqlc.types.list_of(JSON), graphql_name='liveLines', args=sgqlc.types.ArgDict((
        ('catid', sgqlc.types.Arg(Int, graphql_name='catid', default=None)),
        ('eid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='eid', default=None)),
        ('mtid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='mtid', default=None)),
        ('sbid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='sbid', default=None)),
        ('partid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partid', default=None)),
        ('paid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='paid', default=None)),
        ('boid', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='boid', default=None)),
        ('market_type_layout', sgqlc.types.Arg(String, graphql_name='marketTypeLayout', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('distinct', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='distinct', default=None)),
        ('need_sbid', sgqlc.types.Arg(Boolean, graphql_name='needSbid', default=None)),
))
    )
    injuries = sgqlc.types.Field(sgqlc.types.list_of(InjuryResponse), graphql_name='injuries', args=sgqlc.types.ArgDict((
        ('tmid', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='tmid', default=None)),
        ('seid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='seid', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
        ('eventdate', sgqlc.types.Arg(Float, graphql_name='eventdate', default=None)),
))
    )
    news = sgqlc.types.Field(sgqlc.types.list_of(New), graphql_name='news', args=sgqlc.types.ArgDict((
        ('pids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Float)), graphql_name='pids', default=None)),
        ('seid', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='seid', default=None)),
        ('sort', sgqlc.types.Arg(SortInput, graphql_name='sort', default=None)),
))
    )


class Region(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('rid', 'nam', 'sn')
    rid = sgqlc.types.Field(Int, graphql_name='rid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    sn = sgqlc.types.Field(String, graphql_name='sn')


class RegionLeague(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('nam', 'sn')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    sn = sgqlc.types.Field(String, graphql_name='sn')


class RegionLeagueV2(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('nam', 'rid', 'sn')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    rid = sgqlc.types.Field(Int, graphql_name='rid')
    sn = sgqlc.types.Field(String, graphql_name='sn')


class RegionWithLeagues(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('rid', 'nam', 'sn', 'leagues')
    rid = sgqlc.types.Field(Int, graphql_name='rid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    sn = sgqlc.types.Field(String, graphql_name='sn')
    leagues = sgqlc.types.Field(sgqlc.types.list_of(LeaguesWithEventGroups), graphql_name='leagues')


class RegionsBySport(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('active', 'available')
    active = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='active')
    available = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='available')


class Request(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('type', 'query')
    type = sgqlc.types.Field(String, graphql_name='type')
    query = sgqlc.types.Field(String, graphql_name='query')


class Score(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('eid', 'partid', 'pn', 'val', 'sequence')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    partid = sgqlc.types.Field(Int, graphql_name='partid')
    pn = sgqlc.types.Field(Int, graphql_name='pn')
    val = sgqlc.types.Field(String, graphql_name='val')
    sequence = sgqlc.types.Field(Int, graphql_name='sequence')


class ScoreWithMaxSequence(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('scores', 'max_sequence')
    scores = sgqlc.types.Field(sgqlc.types.list_of(Score), graphql_name='scores')
    max_sequence = sgqlc.types.Field(Float, graphql_name='maxSequence')


class SearchParticipant(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('nam', 'lnam', 'fn', 'nn', 'sn', 'abbr')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    lnam = sgqlc.types.Field(String, graphql_name='lnam')
    fn = sgqlc.types.Field(String, graphql_name='fn')
    nn = sgqlc.types.Field(String, graphql_name='nn')
    sn = sgqlc.types.Field(String, graphql_name='sn')
    abbr = sgqlc.types.Field(String, graphql_name='abbr')


class Size(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('original', 'thumb', 'xs', 'sm', 'md', 'lg')
    original = sgqlc.types.Field(String, graphql_name='original')
    thumb = sgqlc.types.Field(String, graphql_name='thumb')
    xs = sgqlc.types.Field(String, graphql_name='xs')
    sm = sgqlc.types.Field(String, graphql_name='sm')
    md = sgqlc.types.Field(String, graphql_name='md')
    lg = sgqlc.types.Field(String, graphql_name='lg')


class Sport(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('spid', 'nam', 'settings')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    settings = sgqlc.types.Field('SportSetting', graphql_name='settings')


class SportCatalog(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('did', 'spid', 'nam', 'settings', 'path')
    did = sgqlc.types.Field(Int, graphql_name='did')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    settings = sgqlc.types.Field('SportSettings', graphql_name='settings')
    path = sgqlc.types.Field(String, graphql_name='path')


class SportSetting(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('spid', 'sitid', 'did', 'enabled', 'alias', 'mode', 'ord', 'nav', 'mtid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    mode = sgqlc.types.Field(String, graphql_name='mode')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    nav = sgqlc.types.Field(String, graphql_name='nav')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')


class SportSettings(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('enabled', 'alias', 'ord')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    ord = sgqlc.types.Field(Int, graphql_name='ord')


class SportSettingsV2(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('spid', 'act', 'enabled', 'alias', 'mode', 'nav', 'mtid', 'ord', '_is_custom', '_is_favorite')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    mode = sgqlc.types.Field(String, graphql_name='mode')
    nav = sgqlc.types.Field(String, graphql_name='nav')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    _is_custom = sgqlc.types.Field(Boolean, graphql_name='_isCustom')
    _is_favorite = sgqlc.types.Field(Boolean, graphql_name='_isFavorite')


class SportV2(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('spid', 'nam', 'sport_has_custom_league_settings', 'sport_has_custom_market_type_settings', 'sport_has_custom_market_type_group_settings', 'settings')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    sport_has_custom_league_settings = sgqlc.types.Field(Customized, graphql_name='sportHasCustomLeagueSettings', args=sgqlc.types.ArgDict((
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
))
    )
    sport_has_custom_market_type_settings = sgqlc.types.Field(Customized, graphql_name='sportHasCustomMarketTypeSettings', args=sgqlc.types.ArgDict((
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
))
    )
    sport_has_custom_market_type_group_settings = sgqlc.types.Field(Customized, graphql_name='sportHasCustomMarketTypeGroupSettings', args=sgqlc.types.ArgDict((
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
))
    )
    settings = sgqlc.types.Field(SportSetting, graphql_name='settings', args=sgqlc.types.ArgDict((
        ('did', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='did', default=None)),
        ('merge', sgqlc.types.Arg(Boolean, graphql_name='merge', default=None)),
))
    )


class SportWithSettings(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('spid', 'nam', 'act', 'settings')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    settings = sgqlc.types.Field(SportSettingsV2, graphql_name='settings')


class SportbooksByCategory(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('cid', 'afid', 'shortafid', 'safid', 'category_name', 'affiliate_url', 'main_affiliate', 'enabled', 'sportsbooksadmin')
    cid = sgqlc.types.Field(Int, graphql_name='cid')
    afid = sgqlc.types.Field(String, graphql_name='afid')
    shortafid = sgqlc.types.Field(String, graphql_name='shortafid')
    safid = sgqlc.types.Field(String, graphql_name='safid')
    category_name = sgqlc.types.Field(String, graphql_name='categoryName')
    affiliate_url = sgqlc.types.Field(String, graphql_name='affiliateURL')
    main_affiliate = sgqlc.types.Field(MainAffiliate, graphql_name='mainAffiliate')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    sportsbooksadmin = sgqlc.types.Field('Sportsbook', graphql_name='sportsbooksadmin')


class Sports(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('spids',)
    spids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='spids')


class SportsWithRegions(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('spid', 'nam', 'alias', 'enabled', 'nav', 'mode', 'domain_ord', 'default_ord', 'regions')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    nav = sgqlc.types.Field(String, graphql_name='nav')
    mode = sgqlc.types.Field(String, graphql_name='mode')
    domain_ord = sgqlc.types.Field(Int, graphql_name='domainOrd')
    default_ord = sgqlc.types.Field(Int, graphql_name='defaultOrd')
    regions = sgqlc.types.Field(sgqlc.types.list_of(RegionWithLeagues), graphql_name='regions')


class Sportsbook(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('sbid', 'paid', 'nam', 'iid', 'pre', 'suf', 'afid', 'settings', 'image')
    sbid = sgqlc.types.Field(Int, graphql_name='sbid')
    paid = sgqlc.types.Field(Int, graphql_name='paid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    iid = sgqlc.types.Field(String, graphql_name='iid')
    pre = sgqlc.types.Field(String, graphql_name='pre')
    suf = sgqlc.types.Field(String, graphql_name='suf')
    afid = sgqlc.types.Field(String, graphql_name='afid')
    settings = sgqlc.types.Field('SportsbookSetting', graphql_name='settings', args=sgqlc.types.ArgDict((
        ('did', sgqlc.types.Arg(Int, graphql_name='did', default=None)),
        ('sitid', sgqlc.types.Arg(Int, graphql_name='sitid', default=None)),
        ('spid', sgqlc.types.Arg(Int, graphql_name='spid', default=None)),
        ('cid', sgqlc.types.Arg(Int, graphql_name='cid', default=None)),
        ('merge', sgqlc.types.Arg(Boolean, graphql_name='merge', default=None)),
))
    )
    image = sgqlc.types.Field(Image, graphql_name='image')


class SportsbookBonus(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('id', 'title', 'subtitle', 'tag', 'sportsbook', 'regions')
    id = sgqlc.types.Field(Int, graphql_name='ID')
    title = sgqlc.types.Field(String, graphql_name='title')
    subtitle = sgqlc.types.Field(String, graphql_name='subtitle')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    sportsbook = sgqlc.types.Field(CMSSportsbook, graphql_name='sportsbook')
    regions = sgqlc.types.Field(sgqlc.types.list_of(CMSRegion), graphql_name='regions')


class SportsbookBonusList(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('id', 'name', 'sportsbook_bonuses')
    id = sgqlc.types.Field(Int, graphql_name='ID')
    name = sgqlc.types.Field(String, graphql_name='name')
    sportsbook_bonuses = sgqlc.types.Field(sgqlc.types.list_of(SportsbookBonus), graphql_name='sportsbookBonuses')


class SportsbookSetting(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('sbid', 'sitid', 'did', 'spid', 'cid', 'ord', 'enabled', 'alias')
    sbid = sgqlc.types.Field(Int, graphql_name='sbid')
    sitid = sgqlc.types.Field(Int, graphql_name='sitid')
    did = sgqlc.types.Field(Int, graphql_name='did')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    cid = sgqlc.types.Field(Int, graphql_name='cid')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    alias = sgqlc.types.Field(String, graphql_name='alias')


class SportsbooksByCategory(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('sbid', 'catid', 'affiliate', 'prefix', 'suffix', 'enabled', 'ord', 'paid', 'nam', 'iid', 'image')
    sbid = sgqlc.types.Field(Int, graphql_name='sbid')
    catid = sgqlc.types.Field(Int, graphql_name='catid')
    affiliate = sgqlc.types.Field(String, graphql_name='affiliate')
    prefix = sgqlc.types.Field(String, graphql_name='prefix')
    suffix = sgqlc.types.Field(String, graphql_name='suffix')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    ord = sgqlc.types.Field(Int, graphql_name='ord')
    paid = sgqlc.types.Field(Int, graphql_name='paid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    iid = sgqlc.types.Field(String, graphql_name='iid')
    image = sgqlc.types.Field(Image, graphql_name='image')


class Statistic(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('typ', 'eid', 'partid', 'pid', 'nam', 'val', 'player', 'siid', 'sequence')
    typ = sgqlc.types.Field(String, graphql_name='typ')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    partid = sgqlc.types.Field(Int, graphql_name='partid')
    pid = sgqlc.types.Field(Int, graphql_name='pid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    val = sgqlc.types.Field(String, graphql_name='val')
    player = sgqlc.types.Field(Player, graphql_name='player')
    siid = sgqlc.types.Field(Float, graphql_name='siid')
    sequence = sgqlc.types.Field(Float, graphql_name='sequence')


class StatisticByGroup(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('ent', 'grp', 'stat', 'tim', 'val', 'sequence', 'valid', 'entid', 'gid', 'statid', 'entgid', 'idty', 'entrid', 'sctim', 'eid', 'partbeid', 'partid', 'pid', 'seid', 'lid', 'tmid', 'tmblid', 'partname', 'partabbreviation', 'partshortname', 'pfn', 'pln', 'stgnam')
    ent = sgqlc.types.Field(String, graphql_name='ent')
    grp = sgqlc.types.Field(String, graphql_name='grp')
    stat = sgqlc.types.Field(String, graphql_name='stat')
    tim = sgqlc.types.Field(Float, graphql_name='tim')
    val = sgqlc.types.Field(String, graphql_name='val')
    sequence = sgqlc.types.Field(Float, graphql_name='sequence')
    valid = sgqlc.types.Field(Int, graphql_name='valid')
    entid = sgqlc.types.Field(Int, graphql_name='entid')
    gid = sgqlc.types.Field(Int, graphql_name='gid')
    statid = sgqlc.types.Field(Int, graphql_name='statid')
    entgid = sgqlc.types.Field(Int, graphql_name='entgid')
    idty = sgqlc.types.Field(String, graphql_name='idty')
    entrid = sgqlc.types.Field(Int, graphql_name='entrid')
    sctim = sgqlc.types.Field(Float, graphql_name='sctim')
    eid = sgqlc.types.Field(Int, graphql_name='eid')
    partbeid = sgqlc.types.Field(Int, graphql_name='partbeid')
    partid = sgqlc.types.Field(Int, graphql_name='partid')
    pid = sgqlc.types.Field(Int, graphql_name='pid')
    seid = sgqlc.types.Field(Int, graphql_name='seid')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    tmid = sgqlc.types.Field(Int, graphql_name='tmid')
    tmblid = sgqlc.types.Field(Int, graphql_name='tmblid')
    partname = sgqlc.types.Field(String, graphql_name='partname')
    partabbreviation = sgqlc.types.Field(String, graphql_name='partabbreviation')
    partshortname = sgqlc.types.Field(String, graphql_name='partshortname')
    pfn = sgqlc.types.Field(String, graphql_name='pfn')
    pln = sgqlc.types.Field(String, graphql_name='pln')
    stgnam = sgqlc.types.Field(String, graphql_name='stgnam')


class StatisticWithMaxSequence(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('statistics', 'max_sequence')
    statistics = sgqlc.types.Field(sgqlc.types.list_of(Statistic), graphql_name='statistics')
    max_sequence = sgqlc.types.Field(Float, graphql_name='maxSequence')


class Tag(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('name', 'background_color', 'text_color', 'dot_color')
    name = sgqlc.types.Field(String, graphql_name='name')
    background_color = sgqlc.types.Field(String, graphql_name='backgroundColor')
    text_color = sgqlc.types.Field(String, graphql_name='textColor')
    dot_color = sgqlc.types.Field(String, graphql_name='dotColor')


class Team(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('tmid', 'lid', 'nam', 'tmblid', 'nn', 'sn', 'abbr', 'cit', 'sta', 'cou', 'act', 'stt', 'ven', 'seid', 'senam', 'conid', 'roster', 'statistics', 'divid', 'divname', 'hasteamstats', 'conname', 'imageurl', 'statistics_by_groups', 'statistics_by_season', 'social_networks', 'league_hierarchy', 'partid')
    tmid = sgqlc.types.Field(Int, graphql_name='tmid')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    nam = sgqlc.types.Field(String, graphql_name='nam')
    tmblid = sgqlc.types.Field(Int, graphql_name='tmblid')
    nn = sgqlc.types.Field(String, graphql_name='nn')
    sn = sgqlc.types.Field(String, graphql_name='sn')
    abbr = sgqlc.types.Field(String, graphql_name='abbr')
    cit = sgqlc.types.Field(String, graphql_name='cit')
    sta = sgqlc.types.Field(String, graphql_name='sta')
    cou = sgqlc.types.Field(String, graphql_name='cou')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    stt = sgqlc.types.Field(String, graphql_name='stt')
    ven = sgqlc.types.Field(String, graphql_name='ven')
    seid = sgqlc.types.Field(Int, graphql_name='seid')
    senam = sgqlc.types.Field(String, graphql_name='senam')
    conid = sgqlc.types.Field(Int, graphql_name='conid')
    roster = sgqlc.types.Field(sgqlc.types.list_of('TeamRoster'), graphql_name='roster', args=sgqlc.types.ArgDict((
        ('seid', sgqlc.types.Arg(Int, graphql_name='seid', default=None)),
        ('all', sgqlc.types.Arg(Boolean, graphql_name='all', default=None)),
))
    )
    statistics = sgqlc.types.Field(sgqlc.types.list_of(StatisticByGroup), graphql_name='statistics', args=sgqlc.types.ArgDict((
        ('statistic_group', sgqlc.types.Arg(String, graphql_name='statisticGroup', default=None)),
))
    )
    divid = sgqlc.types.Field(Int, graphql_name='divid')
    divname = sgqlc.types.Field(String, graphql_name='divname')
    hasteamstats = sgqlc.types.Field(Boolean, graphql_name='hasteamstats')
    conname = sgqlc.types.Field(String, graphql_name='conname')
    imageurl = sgqlc.types.Field(String, graphql_name='imageurl')
    statistics_by_groups = sgqlc.types.Field(sgqlc.types.list_of(StatisticByGroup), graphql_name='statisticsByGroups', args=sgqlc.types.ArgDict((
        ('statistic_group', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='statisticGroup', default=None)),
        ('identities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='identities', default=None)),
        ('eids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='eids', default=None)),
        ('tmids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='tmids', default=None)),
        ('partids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='partids', default=None)),
        ('seids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='seids', default=None)),
        ('ent', sgqlc.types.Arg(sgqlc.types.list_of(ENT), graphql_name='ent', default=None)),
))
    )
    statistics_by_season = sgqlc.types.Field(sgqlc.types.list_of(StatisticByGroup), graphql_name='statisticsBySeason', args=sgqlc.types.ArgDict((
        ('statistic_group', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='statisticGroup', default=None)),
        ('grp', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='grp', default=None)),
        ('stat', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='stat', default=None)),
        ('idty', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='idty', default=None)),
))
    )
    social_networks = sgqlc.types.Field(sgqlc.types.list_of('TeamSocialNetwork'), graphql_name='socialNetworks')
    league_hierarchy = sgqlc.types.Field(sgqlc.types.list_of(LeagueHierarchy), graphql_name='leagueHierarchy')
    partid = sgqlc.types.Field(Int, graphql_name='partid')


class TeamByLeague(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('tmid', 'lid', 'seid', 'senam', 'act', 'tmblid', 'conid', 'conname', 'divid', 'divname', 'event_groups')
    tmid = sgqlc.types.Field(Int, graphql_name='tmid')
    lid = sgqlc.types.Field(Int, graphql_name='lid')
    seid = sgqlc.types.Field(Int, graphql_name='seid')
    senam = sgqlc.types.Field(String, graphql_name='senam')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    tmblid = sgqlc.types.Field(Int, graphql_name='tmblid')
    conid = sgqlc.types.Field(Int, graphql_name='conid')
    conname = sgqlc.types.Field(String, graphql_name='conname')
    divid = sgqlc.types.Field(Int, graphql_name='divid')
    divname = sgqlc.types.Field(String, graphql_name='divname')
    event_groups = sgqlc.types.Field(sgqlc.types.list_of(EventGroupBySeason), graphql_name='eventGroups', args=sgqlc.types.ArgDict((
        ('timezone_offset', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='timezoneOffset', default=None)),
))
    )


class TeamRoster(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('pid', 'seid', 'act', 'pnum', 'ppid', 'ppnam', 'ppsn', 'depth_chart', 'player')
    pid = sgqlc.types.Field(Int, graphql_name='pid')
    seid = sgqlc.types.Field(Int, graphql_name='seid')
    act = sgqlc.types.Field(Boolean, graphql_name='act')
    pnum = sgqlc.types.Field(Int, graphql_name='pnum')
    ppid = sgqlc.types.Field(Int, graphql_name='ppid')
    ppnam = sgqlc.types.Field(String, graphql_name='ppnam')
    ppsn = sgqlc.types.Field(String, graphql_name='ppsn')
    depth_chart = sgqlc.types.Field(sgqlc.types.list_of(DepthChart), graphql_name='depthChart', args=sgqlc.types.ArgDict((
        ('type_of_season', sgqlc.types.Arg(String, graphql_name='typeOfSeason', default=None)),
))
    )
    player = sgqlc.types.Field(Player, graphql_name='player')


class TeamRosterPlayer(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('team_roster', 'player')
    team_roster = sgqlc.types.Field(TeamRoster, graphql_name='teamRoster')
    player = sgqlc.types.Field(Player, graphql_name='player')


class TeamSocialNetwork(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('network', 'account')
    network = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='network')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')


class TopPerformer(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('top_rosters', 'statistics')
    top_rosters = sgqlc.types.Field(sgqlc.types.list_of('TopPerformerRoster'), graphql_name='topRosters')
    statistics = sgqlc.types.Field(sgqlc.types.list_of(StatisticByGroup), graphql_name='statistics')


class TopPerformerRoster(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('team_roster', 'player')
    team_roster = sgqlc.types.Field(TeamRoster, graphql_name='teamRoster')
    player = sgqlc.types.Field(Player, graphql_name='player')


class Trends(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('vltext', 'vln', 'partbeid', 'identity')
    vltext = sgqlc.types.Field(String, graphql_name='vltext')
    vln = sgqlc.types.Field(String, graphql_name='vln')
    partbeid = sgqlc.types.Field(Int, graphql_name='partbeid')
    identity = sgqlc.types.Field(String, graphql_name='identity')


class Value(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('value',)
    value = sgqlc.types.Field(String, graphql_name='value')


class Weather(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('date', 'astronomy', 'maxtemp_c', 'maxtemp_f', 'mintemp_c', 'mintemp_f', 'total_snow_cm', 'sun_hour', 'uv_index', 'hourly')
    date = sgqlc.types.Field(String, graphql_name='date')
    astronomy = sgqlc.types.Field(sgqlc.types.list_of(Astronomy), graphql_name='astronomy')
    maxtemp_c = sgqlc.types.Field(String, graphql_name='maxtempC')
    maxtemp_f = sgqlc.types.Field(String, graphql_name='maxtempF')
    mintemp_c = sgqlc.types.Field(String, graphql_name='mintempC')
    mintemp_f = sgqlc.types.Field(String, graphql_name='mintempF')
    total_snow_cm = sgqlc.types.Field(String, graphql_name='totalSnow_cm')
    sun_hour = sgqlc.types.Field(String, graphql_name='sunHour')
    uv_index = sgqlc.types.Field(String, graphql_name='uvIndex')
    hourly = sgqlc.types.Field(sgqlc.types.list_of(Hourly), graphql_name='hourly')


class WeatherOutput(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('location', 'request', 'current_condition', 'weather', 'climate_averages')
    location = sgqlc.types.Field(String, graphql_name='location')
    request = sgqlc.types.Field(sgqlc.types.list_of(Request), graphql_name='request')
    current_condition = sgqlc.types.Field(sgqlc.types.list_of(CurrentCondition), graphql_name='current_condition')
    weather = sgqlc.types.Field(sgqlc.types.list_of(Weather), graphql_name='weather')
    climate_averages = sgqlc.types.Field(sgqlc.types.list_of('ClimateAverages'), graphql_name='ClimateAverages')


class eventIdsByFilter(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('efid', 'spid', 'mtid', 'eids', 'lids', 'sortmode')
    efid = sgqlc.types.Field(String, graphql_name='efid')
    spid = sgqlc.types.Field(Int, graphql_name='spid')
    mtid = sgqlc.types.Field(Int, graphql_name='mtid')
    eids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='eids')
    lids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='lids')
    sortmode = sgqlc.types.Field(String, graphql_name='sortmode')


class weekWeatherOutput(sgqlc.types.Type):
    __schema__ = sbr_schema_march_2021
    __field_names__ = ('location', 'date', 'avg_day_forecast', 'day_forecast', 'night_forecast')
    location = sgqlc.types.Field(String, graphql_name='location')
    date = sgqlc.types.Field(String, graphql_name='date')
    avg_day_forecast = sgqlc.types.Field(Hourly, graphql_name='avgDayForecast')
    day_forecast = sgqlc.types.Field(Hourly, graphql_name='dayForecast')
    night_forecast = sgqlc.types.Field(Hourly, graphql_name='nightForecast')



########################################################################
# Unions
########################################################################
class Source(sgqlc.types.Union):
    __schema__ = sbr_schema_march_2021
    __types__ = (Team, Player, ParticipantGroup)



########################################################################
# Schema Entry Points
########################################################################
sbr_schema_march_2021.query_type = Query
sbr_schema_march_2021.mutation_type = None
sbr_schema_march_2021.subscription_type = None

