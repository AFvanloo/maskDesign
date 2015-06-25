


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>maskDesign/chipclass.py at master · AFvanloo/maskDesign</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="AFvanloo/maskDesign" name="twitter:title" /><meta content="maskDesign - A set of python modules for designing microwave chips in GDSII format, and for putting them on a mask. Outputs GDS file. It is built around the gdsCAD module" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/8058326?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/8058326?v=3&amp;s=400" property="og:image" /><meta content="AFvanloo/maskDesign" property="og:title" /><meta content="https://github.com/AFvanloo/maskDesign" property="og:url" /><meta content="maskDesign - A set of python modules for designing microwave chips in GDSII format, and for putting them on a mask. Outputs GDS file. It is built around the gdsCAD module" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/ODA1ODMyNjplY2I5MGE2ZTE1ZDRjNTJlYTEwM2NjMjk3ZjQ3MWFlMjo3OTY4ODhhYzY4NmMxOWViMDNiYjA1NjFlMWU2MTUzNWFjY2ExYzFkY2JkZmRmNjAwMzFjZTQwNDM3ZGE4ZjMw--b600e8025c91491d9845ab7ad84a69d294af0b34">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

        <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="527FA043:734E:25BD780:558C527A" name="octolytics-dimension-request_id" /><meta content="8058326" name="octolytics-actor-id" /><meta content="AFvanloo" name="octolytics-actor-login" /><meta content="e309098a878efa3d3c6d4552a3750094270373a864ba1ed7440737e7df986501" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged In">
    <meta name="is-dotcom" content="true">
      <meta name="hostname" content="github.com">
    <meta name="user-login" content="AFvanloo">

      <link rel="icon" sizes="any" mask href="https://assets-cdn.github.com/pinned-octocat.svg">
      <meta name="theme-color" content="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="/LulsaRYo+wJv7nl+oyfKL/Q6GqZ+jxBxI7cP8mcTzkwocZHK3zsReC+RX/ea5o7hw/Ai3UH3wVVKHQO3KoStQ==" name="csrf-token" />

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github/index-4157068649cead58a7dd42dc9c0f2dc5b01bcc77921bc077b357e48be23aa237.css" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github2/index-995ecf21c04e24a47aab268c68fec9b019971e4ed3ea1c970c284585425993a6.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="e34f04b609325fc3eca1306d15633709">

      
  <meta name="description" content="maskDesign - A set of python modules for designing microwave chips in GDSII format, and for putting them on a mask. Outputs GDS file. It is built around the gdsCAD module">
  <meta name="go-import" content="github.com/AFvanloo/maskDesign git https://github.com/AFvanloo/maskDesign.git">

  <meta content="8058326" name="octolytics-dimension-user_id" /><meta content="AFvanloo" name="octolytics-dimension-user_login" /><meta content="23136478" name="octolytics-dimension-repository_id" /><meta content="AFvanloo/maskDesign" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="23136478" name="octolytics-dimension-repository_network_root_id" /><meta content="AFvanloo/maskDesign" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/AFvanloo/maskDesign/commits/master.atom" rel="alternate" title="Recent Commits to maskDesign:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production linux vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      


        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/AFvanloo/maskDesign/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/AFvanloo/maskDesign/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <label class="js-chromeless-input-container form-control">
    <div class="scope-badge">This repository</div>
    <input type="text"
      class="js-site-search-focus js-site-search-field is-clearable chromeless-input"
      data-hotkey="s"
      name="q"
      placeholder="Search"
      data-global-scope-placeholder="Search GitHub"
      data-repo-scope-placeholder="Search"
      tabindex="1"
      autocapitalize="off">
  </label>
</form>
      </div>

      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item">
      <span class="js-socket-channel js-updatable-content"
        data-channel="notification-changed:AFvanloo"
        data-url="/notifications/header">
      <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
          <span class="mail-status all-read"></span>
          <span class="octicon octicon-inbox"></span>
</a>  </span>

  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new..."
       data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus left"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>


  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="AFvanloo/maskDesign">This repository</span>
  </div>
    <a class="dropdown-item" href="/AFvanloo/maskDesign/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>
    <a class="dropdown-item" href="/AFvanloo/maskDesign/settings/collaboration" data-ga-click="Header, create new collaborator">
      New collaborator
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-s js-menu-target" href="/AFvanloo"
       aria-label="View profile and more"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@AFvanloo" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/8058326?v=3&amp;s=40" width="20" />
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu dropdown-menu-sw">
        <div class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">AFvanloo</strong>
        </div>
        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/AFvanloo" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a>
        <a class="dropdown-item" href="/stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
        <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>
        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a>

        <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="6yHOKLKFOpcrZveE56cAXcEFsQdocj2PUkfhrRspq1NofWaWGQ3rlDQYkPlrfeoS/BZc2W580/J2xYVD7sKdxw==" /></div>
          <button class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>

        

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">

        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="OwBOvYkLlQAA6KM8pJzL7tJhbEnENxxJMntLNDoGTJE5Q4zenOoPRa2FyzTa0AID724vNwJogWYXx/8uxmFUaw==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="23136478" />

      <div class="select-menu js-menu-container js-select-menu">
        <a href="/AFvanloo/maskDesign/subscription"
          class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
          data-ga-click="Repository, click Watch settings, action:blob#show">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Unwatch
          </span>
        </a>
        <a class="social-count js-social-count" href="/AFvanloo/maskDesign/watchers">
          3
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/AFvanloo/maskDesign/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="GMC0VPWUeEHGyDqj0DBlQttNj2KhnJ7H/QDRB3XR6Dgg+iQ091s6n+nUHFhAfUFXfmc398YAZ1SbZtm3XkSNPQ==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar AFvanloo/maskDesign"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/AFvanloo/maskDesign/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/AFvanloo/maskDesign/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="YB/30XLy3OojmobjcD5qQdFvWoadhtA1B/j2l0u8m4YfKwJNn9asThmKVOGGSOSSeIOi5EZV99XfiuwD73tmqQ==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star AFvanloo/maskDesign"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/AFvanloo/maskDesign/stargazers">
          0
        </a>
</form>  </div>

  </li>

        <li>
          <form accept-charset="UTF-8" action="/AFvanloo/maskDesign/fork" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="+FCG0aO1RyyCLokTAuuwhgXuBkdi1NTkN7cL+EpOyk2SwKjFMDUjEwqi9Pgex6NmdR6aayUOaugNzuwk2QPL6Q==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of AFvanloo/maskDesign to your account"
                aria-label="Fork your own copy of AFvanloo/maskDesign to your account">
              <span class="octicon octicon-repo-forked"></span>
              Fork
            </button>
            <a href="/AFvanloo/maskDesign/network" class="social-count">0</a>
</form>        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/AFvanloo" class="url fn" itemprop="url" rel="author"><span itemprop="title">AFvanloo</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/AFvanloo/maskDesign" data-pjax="#js-repo-pjax-container">maskDesign</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/AFvanloo/maskDesign/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/AFvanloo/maskDesign" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /AFvanloo/maskDesign">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/AFvanloo/maskDesign/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /AFvanloo/maskDesign/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/AFvanloo/maskDesign/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /AFvanloo/maskDesign/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/AFvanloo/maskDesign/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /AFvanloo/maskDesign/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/AFvanloo/maskDesign/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /AFvanloo/maskDesign/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/AFvanloo/maskDesign/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /AFvanloo/maskDesign/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>
  </ul>


    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Settings">
        <a href="/AFvanloo/maskDesign/settings" aria-label="Settings" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_settings /AFvanloo/maskDesign/settings">
          <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>
</nav>

              <div class="only-with-full-nav">
                  
<div class="js-clone-url clone-url open"
  data-protocol-type="http">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/AFvanloo/maskDesign.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="js-clone-url clone-url "
  data-protocol-type="ssh">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:AFvanloo/maskDesign.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="js-clone-url clone-url "
  data-protocol-type="subversion">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/AFvanloo/maskDesign" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<div class="clone-options">You can clone with
  <form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=http&amp;protocol_type=push" class="inline-form js-clone-selector-form is-enabled" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="bDRHLcVw+KScP8ggvhk7aS9froi3+rxKoPT4ToUkpd5qaU1KX/d7+9NI2QIU9C3amdOreNIldmj16rnMilO40Q==" /></div><button class="btn-link js-clone-selector" data-protocol="http" type="submit">HTTPS</button></form>, <form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push" class="inline-form js-clone-selector-form is-enabled" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="BbsxgJQmE/+GvIJkSQOpC18b5sEQgZyJ2q87z7RZchPiBDkV0rVR1HICOO29mwXG7pOv98nmD93Xkf5nwhkwGA==" /></div><button class="btn-link js-clone-selector" data-protocol="ssh" type="submit">SSH</button></form>, or <form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push" class="inline-form js-clone-selector-form is-enabled" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Itl8nBPNDrWpc3RTUPmyzcR0eEHJdwG0JNHx3RTFo6gXMqhbCsyTyV+fAhzsjZ4kcFOsJoKCxH3EiE0nst/12A==" /></div><button class="btn-link js-clone-selector" data-protocol="subversion" type="submit">Subversion</button></form>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</div>




                <a href="/AFvanloo/maskDesign/archive/master.zip"
                   class="btn btn-sm sidebar-button"
                   aria-label="Download the contents of AFvanloo/maskDesign as a zip file"
                   title="Download the contents of AFvanloo/maskDesign as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>

          

<a href="/AFvanloo/maskDesign/blob/23bee8af695b24c2928a82ba04425c49e7872ca9/chipclass.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:32e9c3b992658671561f98a5c324116c -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/AFvanloo/maskDesign/blob/master/chipclass.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <form accept-charset="UTF-8" action="/AFvanloo/maskDesign/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="TvAH3EFRMbtAf5A2lxhYbtX+q2O/iiTfY6qvMDMzHpCh43hBzLW6PwapXPyPa8afJUtjMC4FJDdT/9f0xISJhg==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="chipclass.py">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/AFvanloo/maskDesign/find/master"
          class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/AFvanloo/maskDesign" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">maskDesign</span></a></span></span><span class="separator">/</span><strong class="final-path">chipclass.py</strong>
  </div>
</div>

<include-fragment class="commit commit-loader file-history-tease" src="/AFvanloo/maskDesign/contributors/master/chipclass.py">
  <div class="file-history-tease-header">
    Fetching contributors&hellip;
  </div>

  <div class="participation">
    <p class="loader-loading"><img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
    <p class="loader-error">Cannot retrieve contributors at this time</p>
  </div>
</include-fragment>
<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/AFvanloo/maskDesign/raw/master/chipclass.py" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/AFvanloo/maskDesign/blame/master/chipclass.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/AFvanloo/maskDesign/commits/master/chipclass.py" class="btn btn-sm " rel="nofollow">History</a>
      </div>


            <form accept-charset="UTF-8" action="/AFvanloo/maskDesign/edit/master/chipclass.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="DQha2vUCBYCP/w65I5x5bNUMWDKoaH0BD+xJJ98IoO3T9wnM6bH3hhbupAGdlmRV9pItKLrfib/QKYGTLNhrug==" /></div>
              <button class="octicon-btn tooltipped tooltipped-n" type="submit" aria-label="Edit this file" data-hotkey="e" data-disable-with>
                <span class="octicon octicon-pencil"></span>
              </button>
</form>
          <form accept-charset="UTF-8" action="/AFvanloo/maskDesign/delete/master/chipclass.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="AZqLQ98MiH7OvQknTMZXybpHqgdtTHhvwxeop0Io5KBD/XL+EMBVN8jaDzL4Rf1qEBbTIRBhdPqPZ0XOF1hJxw==" /></div>
            <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-n" type="submit" aria-label="Delete this file" data-disable-with>
              <span class="octicon octicon-trashcan"></span>
            </button>
</form>    </div>

    <div class="file-info">
        2052 lines (1611 sloc)
        <span class="file-info-divider"></span>
      75.012 kB
    </div>
  </div>
  
  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> maskDesign <span class="pl-k">as</span> md</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> gdsCAD <span class="pl-k">as</span> cad</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> numpy <span class="pl-k">as</span> np</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> defaultParms <span class="pl-k">as</span> dpars</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>loading chipClass<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#Units are nm, so to use um, multiply by 1000</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">um <span class="pl-k">=</span> <span class="pl-c1">1e3</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">mm <span class="pl-k">=</span> <span class="pl-c1">1e6</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#default border and launcher configuration options:</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">borderTagList, offCenters <span class="pl-k">=</span> dpars.dLists()</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#Default component design values</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">defaults <span class="pl-k">=</span> dpars.dPars()</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Sample</span>:</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">border</span>, <span class="pl-smi">launcherConfig</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>A<span class="pl-pds">&#39;</span></span>, <span class="pl-smi">launcherPositions</span><span class="pl-k">=</span>[],</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">alignPos</span><span class="pl-k">=</span>[], <span class="pl-smi">label</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-smi">borderGap</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">labelPos</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">labelFontSize</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">posRes</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-smi">a1</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">b1</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Calling constructor</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The border (default set to 2) refers to the default border sizes and</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        launcher configurations:</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            1: 7*2mm</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            2: 7*4.3mm</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            3: 7*6.6mm</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The LauncherConfig determines the locations of the launchers</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            &#39;A&#39;  1 launchers left/right, and 3 on top and bottom</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            &#39;B&#39;  2 launchers left/right, and 2 on top and bottom</span></td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            &#39;C&#39;  16 port design: 4 launchers on each side. Only for chipsize 3</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            </span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The launcherlist refers to which launchers to put, clockwise from the</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        left center</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        alignPositions refers to which alignment marks to draw, clockwise from</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the left upper corner</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the &#39;posRes&#39; option refers to positive resist chips. This will change the border sizes</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#TODO Default Values: hardcode or config file?</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fileName <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>test0123.gds<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.label <span class="pl-k">=</span> label</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.labelPos <span class="pl-k">=</span> labelPos</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.lambdahalf65 <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>lambdahalf65<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Sample border Options</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.borders <span class="pl-k">=</span> borderTagList[border]</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.borderTag <span class="pl-k">=</span> border</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.posRes <span class="pl-k">=</span> posRes</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.posResEdge <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>posResEdge<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.offCenters <span class="pl-k">=</span> offCenters</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> borderGap <span class="pl-k">==</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.borderGap <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>borderGap<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.borderGap <span class="pl-k">=</span> borderGap</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#launcher options</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.launcherPositions <span class="pl-k">=</span> launcherPositions</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.launcherConfig <span class="pl-k">=</span> launcherConfig</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.launchwidth <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>launcherWidth<span class="pl-pds">&#39;</span></span>] </td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.launcherWlen <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>launcherWideLen<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.launcherTlen <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>launcherTaperLen<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Alignment mark options</span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.alignPos <span class="pl-k">=</span> alignPos</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#line options</span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> a1 <span class="pl-k">==</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.a1 <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>centerConductor<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.a1 <span class="pl-k">=</span> a1</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> b1 <span class="pl-k">==</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.b1 <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>CPWGap<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.b1 <span class="pl-k">=</span> b1</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.abr <span class="pl-k">=</span> <span class="pl-v">self</span>.b1<span class="pl-k">/</span><span class="pl-v">self</span>.a1</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rbend <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>minimumRadius<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Transmon options</span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.transmonShape <span class="pl-k">=</span> (<span class="pl-c1">300</span><span class="pl-k">*</span>um, <span class="pl-c1">150</span><span class="pl-k">*</span>um)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#gapCoupler Options</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gapSize <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>gapCouplerSize<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#fingerCoupler options</span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerTaperLen <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>fingerTaperLen<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerCenterLen <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>fingerCenterLen<span class="pl-pds">&#39;</span></span>] <span class="pl-c">#Length of center part</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerLen <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>fingerLen<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerThick <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>fingerThick<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerGapWidth <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>fingerGapWidth<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerGapHeight <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>fingerGapHeight<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Airbridge Options</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridgeLenX <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>ABbridgeLenX<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridgeLenY <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>ABbridgeLenY<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.footerLen <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>ABfooterLen<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.reflowGap <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>ABreflowGap<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.irGap <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>ABirGap<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.ABlayers <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>ABlayers<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#CPW bridge options</span></td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridgeDistance <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>ABdistance<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridgeStart <span class="pl-k">=</span> defaults[ <span class="pl-s"><span class="pl-pds">&#39;</span>ABstart<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridgeEnd <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>ABend<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">       </td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#label Font</span></td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.labelFont <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>labelFont<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> labelFontSize <span class="pl-k">==</span> <span class="pl-c1">None</span>: <span class="pl-v">self</span>.labelFontSize <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>labelFontSize<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>: <span class="pl-v">self</span>.labelFontSize <span class="pl-k">=</span> labelFontSize</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Bounding boxes for avoiding overlaps are kept in a np.array</span></td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bbox <span class="pl-k">=</span> np.array([]) <span class="pl-c">#TODO Not yet implemented</span></td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#A 6.5 Lambda/2 resonator is 2*4670um long</span></td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">        lambhalf65 <span class="pl-k">=</span> <span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-c1">4670</span><span class="pl-k">*</span>um</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#keeping track of present components:</span></td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.resonators <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.wiggles <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.transmonBoxes <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.cornerTransmonBoxes <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerCouplers <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gapCouplers <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.airbridges <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.CPWs <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.arcs <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.doubleArcs <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.slines <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.jlines <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.texts <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.tapers <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.crossArrays <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerCaps <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.chargeLines <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gateEnds <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fluxLines <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.thinTennas <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.newname <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Start Constructing the Sample</span></td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>border type is <span class="pl-pds">&#39;</span></span>, border </td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> (border <span class="pl-k">&lt;</span> <span class="pl-c1">1</span>) <span class="pl-k">or</span> (border <span class="pl-k">&gt;</span> <span class="pl-c1">7</span>):</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> <span class="pl-c1">Exception</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Choose border between 1 and 4<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#If using python 3, replace with following line</span></td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#raise Exception(&#39;Choose border between 1 and 4&#39;)</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Initialize actual Sample</span></td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.initSample()</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">initSample</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Construct a sample layout with borders</span></td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Topcell and Layout:</span></td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.topCell <span class="pl-k">=</span> cad.core.Cell(<span class="pl-s"><span class="pl-pds">&#39;</span>TOP<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.layout <span class="pl-k">=</span> cad.core.Layout(<span class="pl-s"><span class="pl-pds">&#39;</span>SAMPLE<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Put units to nm to allow fine spacing of object origins</span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.layout.unit <span class="pl-k">=</span> <span class="pl-c1">1e-9</span></td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#borders and alignment markers</span></td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.border1 <span class="pl-k">=</span> Border(<span class="pl-v">self</span>)</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#add label</span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.addText(<span class="pl-v">self</span>.label, <span class="pl-smi">placeInfo</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.labelPos)</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#add Launchers</span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>in initSample, center is <span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.a1</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.addLaunchers()</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#========================sampleX wrappers for objects===========================</span></td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addCPW</span>(<span class="pl-smi">self</span>, <span class="pl-smi">leng</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">bridges</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">bridgeDistance</span><span class="pl-k">=</span> <span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">bridgeStart</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">bridgeEnd</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">closeA</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">closeB</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">flip</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        add a CPW line</span></td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Input the length in nm</span></td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        PlaceInfo can be either a location or the connector of an object.</span></td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Examples:</span></td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            (x, y)</span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            &#39;launcher1.connect&#39;</span></td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        if Bridges is set to true, airbridges are created as well, with optional </span></td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        entries for an initial and final span without airbriges.</span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        If you need more control, keep bridges set to off and add them</span></td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        separately</span></td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        If closeA or closeB is set to true, a rectangle is drawn at that end of</span></td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the CPW to close it.</span></td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Flip is used when connecting to a component situated to the right of the</span></td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        CPW. By default flip is off, meaning a CPW is added to a component on</span></td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        its left</span></td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Default values</span></td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> bridgeDistance <span class="pl-k">==</span> <span class="pl-c1">None</span>: bridgeDistance <span class="pl-k">=</span> <span class="pl-v">self</span>.bridgeDistance</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> bridgeStart <span class="pl-k">==</span> <span class="pl-c1">None</span>: bridgeStart <span class="pl-k">=</span> <span class="pl-v">self</span>.bridgeStart</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> bridgeEnd <span class="pl-k">==</span> <span class="pl-c1">None</span>: bridgeEnd <span class="pl-k">=</span> <span class="pl-v">self</span>.bridgeEnd</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Keep track of the number of lines</span></td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.CPWs <span class="pl-k">+=</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>, name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>CPW<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.CPWs), CPW(<span class="pl-v">self</span>,leng, placeInfo, bridges,</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">            bridgeDistance, bridgeStart, bridgeEnd, closeA, closeB, flip, rot))</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addArc</span>(<span class="pl-smi">self</span>, <span class="pl-smi">initAngle</span>, <span class="pl-smi">degrees</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">flip</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">rbend</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Wrapper for Arc:</span></td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        rbend is set to 100um by default. initAngle is the initial angle at</span></td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        which the bend starts, similar to in the unit circle. </span></td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        </span></td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        degrees is the amount angle between start and end</span></td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The flip option is used when placeInfo is a connector. In that case,</span></td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        flip toggles which side of the arc connects to the given connector</span></td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Default values</span></td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> rbend <span class="pl-k">==</span> <span class="pl-c1">None</span>: rbend <span class="pl-k">=</span> <span class="pl-v">self</span>.rbend</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>adding an Arc<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.arcs <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#create launchers according to the list &#39;launcherpositions&#39;</span></td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>, name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>arc<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.arcs), Arc(<span class="pl-v">self</span>, initAngle, degrees,</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">            placeInfo, flip, rbend, rot))</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#    def addResonator(self, freq, xspan, nwiggle, transmons = [&#39;luru&#39;], caps =</span></td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#    [&#39;f3f3&#39;], xOffset=0,</span></td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#            yOffset=0, skew=0, rot=0):</span></td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        &#39;&#39;&#39;</span></td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        Add a resonator, including transmons and capacitors</span></td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        Not all options can be entered via this function. They are however all</span></td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        available as attributes to the resonator class. </span></td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        Change the attributes you want to change, </span></td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        leng denotes the total length you want</span></td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        xspan is the horizontal (or vertical if rotated) distance between start</span></td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        and end point</span></td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        xOffset and its Y variant displace the wiggles compared to the</span></td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        start coordinates of the structure</span></td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        &#39;&#39;&#39;</span></td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        </span></td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        self.resonators += 1</span></td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        setattr(self, &#39;wiggle&#39;+str(self.wiggles), Wiggle(self,nWiggle, leng,</span></td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#            xspan, placeInfo, xOffset, yOffset, skew, rot))</span></td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addDoubleArc</span>(<span class="pl-smi">self</span>, <span class="pl-smi">dx</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">rbend</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">flip</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Wrapper for Arc:</span></td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        rbend is set to 100um by default. initAngle is the initial angle at</span></td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        which the bend starts, similar to in the unit circle. </span></td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        </span></td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        degrees is the amount angle between start and end</span></td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The flip option is used to toggle if the component should be added from</span></td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the top or from below</span></td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        addArc has no rotation variable, since the same functionality is reached</span></td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        by changing initAngle</span></td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Default values</span></td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> rbend <span class="pl-k">==</span> <span class="pl-c1">None</span>: rbend <span class="pl-k">=</span> <span class="pl-v">self</span>.rbend</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.doubleArcs <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#create launchers according to the list &#39;launcherpositions&#39;</span></td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>doubleArc<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.doubleArcs), DoubleArc(<span class="pl-v">self</span>, dx,</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">            placeInfo, rbend, flip, rot))</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addWiggle</span>(<span class="pl-smi">self</span>, <span class="pl-smi">nWiggle</span>, <span class="pl-smi">leng</span>, <span class="pl-smi">xspan</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">xOffset</span><span class="pl-k">=</span><span class="pl-c1">0</span>,</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">yOffset</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">skew</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">rbend</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">bridges</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-smi">closeA</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-smi">closeB</span> <span class="pl-k">=</span></td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">False</span>, <span class="pl-smi">flip</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a wiggly CPW</span></td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        leng denotes the total length you want</span></td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        xspan is the horizontal (or vertical if rotated) distance between start</span></td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        and end point</span></td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        xOffset and its Y variant displace the wiggles compared to the</span></td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        start coordinates of the structure</span></td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Set closeA or closeB to True if the wiggle needs to be closed at these</span></td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        endpoints</span></td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> rbend <span class="pl-k">==</span> <span class="pl-c1">None</span>: rbend <span class="pl-k">=</span> <span class="pl-v">self</span>.rbend</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.wiggles <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>wiggle<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.wiggles), Wiggle(<span class="pl-v">self</span>,nWiggle, leng,</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">            xspan, placeInfo, xOffset, yOffset, skew, rbend, bridges, closeA,</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">            closeB, flip, rot))</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addSLine</span>(<span class="pl-smi">self</span>, <span class="pl-smi">yspan</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">rbend</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">reflect</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">flip</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">enter</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-smi">exit</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-smi">bridges</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>,  <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add an Sline (90 degree arc + CPW + 90 arc</span></td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#default value</span></td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> rbend <span class="pl-k">==</span> <span class="pl-c1">None</span>: rbend <span class="pl-k">=</span> <span class="pl-v">self</span>.rbend</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.slines <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>sLine<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.slines), SLine(<span class="pl-v">self</span>, yspan, placeInfo,</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">            rbend, reflect, flip, enter, exit, bridges, rot))</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addJLine</span>(<span class="pl-smi">self</span>, <span class="pl-smi">totLen</span>, <span class="pl-smi">xspan</span>, <span class="pl-smi">yspan</span>, <span class="pl-smi">nWiggles</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">offsets</span>,</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">rbend</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">bridges</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a JLine to the sample, primarily as testresonators coupled to a</span></td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        feedLine</span></td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Inputs: </span></td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        totLen = total length of the resonator, determining its frequency</span></td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        xspan = length of horizontal line at the top</span></td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        yspan = vertical length of the resonator</span></td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        nWiggles = number of wiggles in the line</span></td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        placeInfo = location information, either a tuple of coordinates, or an</span></td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        object connector (as a string)</span></td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        offsets = offsets compared to the placeInfo connector</span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#default value</span></td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> rbend <span class="pl-k">==</span> <span class="pl-c1">None</span>: rbend <span class="pl-k">=</span> <span class="pl-v">self</span>.rbend</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.jlines <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>JLine<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.jlines), JLine(<span class="pl-v">self</span>, totLen, xspan,</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">            yspan, nWiggles, placeInfo, offsets, rbend, bridges, rot))</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addGapCoupler</span>(<span class="pl-smi">self</span>, <span class="pl-smi">gapSize</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">extralen</span><span class="pl-k">=</span><span class="pl-c1">0</span>,<span class="pl-smi">flip</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a gap Coupler. </span></td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        By default, the gap coupler is only as long as the gap. If you would</span></td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        like it longer, just add a nonzero extralen.</span></td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        For placeInfo, input either a tuple of coordinates:</span></td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            (x, y)</span></td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        or a string containing what you want to connect it to, for example:</span></td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            CPW1.connectB</span></td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gapCouplers <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>gapCoupler<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.gapCouplers),</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">                GapCoupler(<span class="pl-v">self</span>,gapSize, placeInfo, extralen, flip, rot))</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addTransmonBox</span>(<span class="pl-smi">self</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">shape</span><span class="pl-k">=</span>(<span class="pl-c1">300</span><span class="pl-k">*</span>um, <span class="pl-c1">150</span><span class="pl-k">*</span>um), <span class="pl-smi">offset</span><span class="pl-k">=</span>(<span class="pl-c1">300</span><span class="pl-k">*</span>um,<span class="pl-c1">0</span>), <span class="pl-smi">almarks</span> <span class="pl-k">=</span> [<span class="pl-c1">2</span>,<span class="pl-c1">2</span>],</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">flip</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a TransmonBox. </span></td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The offset is an offset compared to placeInfo, such that the transmonbox</span></td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        can be connected directly to the connector of a CPW or Wiggle</span></td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The offset is ignored when the placeInfo provided is a tuple with</span></td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        coordinates rather than a string to a connector</span></td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        if flip is set to true, the transmonbox is placed on the opposite side</span></td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        of the CPW</span></td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.transmonBoxes <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>transmonBox<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.transmonBoxes),</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">                TransmonBox(<span class="pl-v">self</span>, shape, placeInfo, offset, almarks, flip, rot))</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addCornerTransmonBox</span>(<span class="pl-smi">self</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">shape</span><span class="pl-k">=</span>(<span class="pl-c1">300</span><span class="pl-k">*</span>um, <span class="pl-c1">150</span><span class="pl-k">*</span>um), <span class="pl-smi">offset</span><span class="pl-k">=</span>(<span class="pl-c1">0</span><span class="pl-k">*</span>um,<span class="pl-c1">0</span>),<span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a TransmonBox. </span></td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        shape = width, height.</span></td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The offset is an offset compared to placeInfo, and does not depend on</span></td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the rotation.</span></td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        </span></td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        PlaceInfo can be either of three things:</span></td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            - A string with connector info, eg &#39;CPW1.coords&#39; or &#39;wiggle.connectA&#39;</span></td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            - A list containing a horizontal and vertical CPW or wiggle, in that</span></td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line"><span class="pl-s">              order [horizonConnect, verticalConnect], upon whihc the</span></td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line"><span class="pl-s">              transmonBox will be placed in the corner</span></td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            - A tuple or list of coordinates (x, y)</span></td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        </span></td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The offset is ignored when the placeInfo provided is a tuple with</span></td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        coordinates rather than a string to a connector</span></td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        if corner is set to True, you get a cornerTransmonBox instead. In that</span></td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        case, options almarks and flip are ignored</span></td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.cornerTransmonBoxes <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>cornerTransmonBox<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.cornerTransmonBoxes),</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">                CornerTransmonBox(<span class="pl-v">self</span>, shape, placeInfo, offset, rot))</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addFingerCap</span>(<span class="pl-smi">self</span>, <span class="pl-smi">nFingers</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">fingerLen</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, </td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">fingerThick</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">gapHeight</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">gapWidth</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">flip</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a finger Capacitor. </span></td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The finger Capacitor has loads of options, but there are default values</span></td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        for almost all of them. Change any of them as you like, according to:</span></td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            addFingerCap(3, &lt;placeInfo&gt;, gapWidth = 1*um, taperLen = 75*um)</span></td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        for example</span></td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        For placeInfo, input either a tuple of coordinates:</span></td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            (x, y)</span></td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        or a string containing what you want to connect it to, for example:</span></td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            &#39;CPW1.connectB&#39;</span></td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Set the default Values</span></td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> fingerLen <span class="pl-k">==</span> <span class="pl-c1">None</span>: fingerLen <span class="pl-k">=</span> <span class="pl-v">self</span>.fingerLen</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> fingerThick <span class="pl-k">==</span> <span class="pl-c1">None</span>: fingerThick <span class="pl-k">=</span> <span class="pl-v">self</span>.fingerThick</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> gapHeight <span class="pl-k">==</span> <span class="pl-c1">None</span>: gapHeight <span class="pl-k">=</span> <span class="pl-v">self</span>.fingerGapHeight</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> gapWidth <span class="pl-k">==</span> <span class="pl-c1">None</span>: gapWidth <span class="pl-k">=</span> <span class="pl-v">self</span>.fingerGapWidth</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Build the finger coupler</span></td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerCaps <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>fingerCap<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.fingerCaps),</td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">                FingerCap(<span class="pl-v">self</span>,nFingers, placeInfo, fingerLen,</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">                fingerThick, gapHeight, gapWidth, <span class="pl-smi">flip</span><span class="pl-k">=</span>flip, <span class="pl-smi">rot</span><span class="pl-k">=</span>rot))</td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addFingerCoupler</span>(<span class="pl-smi">self</span>, <span class="pl-smi">nFingers</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">fingerLen</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, </td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">fingerThick</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">gapHeight</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">gapWidth</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">taperLen</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">centerLen</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">flip</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a finger Coupler. </span></td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The finger Coupler has loads of options, but there are default values</span></td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        for almost all of them. Change any of them as you like, according to:</span></td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            addFingerCoupler(3, &lt;placeInfo&gt;, gapWidth = 1*um, taperLen = 75*um)</span></td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        for example</span></td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        For placeInfo, input either a tuple of coordinates:</span></td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            (x, y)</span></td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        or a string containing what you want to connect it to, for example:</span></td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            &#39;CPW1.connectB&#39;</span></td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Set the default Values</span></td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> fingerLen <span class="pl-k">==</span> <span class="pl-c1">None</span>: fingerLen <span class="pl-k">=</span> <span class="pl-v">self</span>.fingerLen</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> fingerThick <span class="pl-k">==</span> <span class="pl-c1">None</span>: fingerThick <span class="pl-k">=</span> <span class="pl-v">self</span>.fingerThick</td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> gapHeight <span class="pl-k">==</span> <span class="pl-c1">None</span>: gapHeight <span class="pl-k">=</span> <span class="pl-v">self</span>.fingerGapHeight</td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> gapWidth <span class="pl-k">==</span> <span class="pl-c1">None</span>: gapWidth <span class="pl-k">=</span> <span class="pl-v">self</span>.fingerGapWidth</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> taperLen <span class="pl-k">==</span> <span class="pl-c1">None</span>: taperLen <span class="pl-k">=</span> <span class="pl-v">self</span>.fingerTaperLen</td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> centerLen <span class="pl-k">==</span> <span class="pl-c1">None</span>: centerLen <span class="pl-k">=</span> <span class="pl-v">self</span>.fingerCenterLen</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Build the finger coupler</span></td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerCouplers <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>fingerCoupler<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.fingerCouplers),</td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">                FingerCoupler(<span class="pl-v">self</span>,nFingers, placeInfo, fingerLen,</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">                fingerThick, gapHeight, gapWidth, taperLen, centerLen, flip, <span class="pl-smi">rot</span><span class="pl-k">=</span>rot))</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addAirbridge</span>(<span class="pl-smi">self</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">bridgeLenX</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">bridgeLenY</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">footerLen</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">irGap</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">reflowGap</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">layers</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">offset</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>),<span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        All options (except placeInfo and rot) are taken from the config dict,</span></td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Unless if specified otherwise by YOU!</span></td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Set the default Values</span></td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> bridgeLenX <span class="pl-k">==</span> <span class="pl-c1">None</span>:  bridgeLenX <span class="pl-k">=</span>  <span class="pl-v">self</span>.bridgeLenX</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> bridgeLenY <span class="pl-k">==</span> <span class="pl-c1">None</span>:  bridgeLenY <span class="pl-k">=</span>  <span class="pl-v">self</span>.bridgeLenY</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> footerLen <span class="pl-k">==</span> <span class="pl-c1">None</span>:   footerLen <span class="pl-k">=</span>  <span class="pl-v">self</span>.footerLen</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> irGap <span class="pl-k">==</span> <span class="pl-c1">None</span>:       irGap <span class="pl-k">=</span>  <span class="pl-v">self</span>.irGap</td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> reflowGap <span class="pl-k">==</span> <span class="pl-c1">None</span>:   reflowGap <span class="pl-k">=</span>  <span class="pl-v">self</span>.reflowGap</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> layers <span class="pl-k">==</span> <span class="pl-c1">None</span>:      layers <span class="pl-k">=</span>  <span class="pl-v">self</span>.ABlayers</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Build the finger coupler</span></td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.airbridges <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>airBridge<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.airbridges),</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">                Airbridge(<span class="pl-v">self</span>, placeInfo, bridgeLenX, bridgeLenY, footerLen, </td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">                    irGap, reflowGap, layers, offset, <span class="pl-smi">rot</span><span class="pl-k">=</span>rot))</td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addTaper</span>(<span class="pl-smi">self</span>, <span class="pl-smi">taperLen</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">startCenter</span>, <span class="pl-smi">endCenter</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">abr</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">flip</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-smi">noground</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a Taper</span></td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        define the total width of the center conductor at start (startCenter)</span></td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        and end (endCenter)</span></td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        placeInfo can be either a string for a connector, or a tuple or list of</span></td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        coordinates</span></td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#default variables</span></td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> abr <span class="pl-k">==</span> <span class="pl-c1">None</span>: abr <span class="pl-k">=</span> <span class="pl-v">self</span>.abr</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> endCenter <span class="pl-k">==</span> <span class="pl-c1">None</span>: endCenter <span class="pl-k">=</span> <span class="pl-v">self</span>.a1</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.tapers <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>taper<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.tapers),</td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">                Taper(<span class="pl-v">self</span>, taperLen, startCenter, endCenter, placeInfo,</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">                    <span class="pl-smi">abr</span><span class="pl-k">=</span><span class="pl-v">self</span>.abr, <span class="pl-smi">rot</span><span class="pl-k">=</span>rot, <span class="pl-smi">flip</span><span class="pl-k">=</span>flip, <span class="pl-smi">noground</span> <span class="pl-k">=</span> noground))</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addLauncher</span>(<span class="pl-smi">self</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">center</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">gap</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        add a single launcher</span></td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        For Launchers at standard positions at the borders, please use</span></td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        &#39;addLaunchers&#39; instead</span></td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>constructing Launchers<span class="pl-pds">&#39;</span></span> </td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#default options</span></td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> center <span class="pl-k">==</span> <span class="pl-c1">None</span>: center <span class="pl-k">=</span> <span class="pl-v">self</span>.a1</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> gap <span class="pl-k">==</span> <span class="pl-c1">None</span>: gap <span class="pl-k">=</span> <span class="pl-v">self</span>.b1</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#create launchers according to the list &#39;launcherpositions&#39;</span></td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>launcher<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(pos), Launcher(<span class="pl-v">self</span>, placeInfo, center, gap,</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-v">self</span>.rot))</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addLaunchers</span>(<span class="pl-smi">self</span>, <span class="pl-smi">center</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">gap</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Wrapper for Launcher:</span></td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Create Launcher objects with names according to their position</span></td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>constructing Launchers<span class="pl-pds">&#39;</span></span> </td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#default options</span></td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> center <span class="pl-k">==</span> <span class="pl-c1">None</span>: center <span class="pl-k">=</span> <span class="pl-v">self</span>.a1</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> gap <span class="pl-k">==</span> <span class="pl-c1">None</span>: gap <span class="pl-k">=</span> <span class="pl-v">self</span>.b1</td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>in addlaunchers, center is <span class="pl-pds">&#39;</span></span>, center</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#get the position list associated with the chosen configuration </span></td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.launcherLocations <span class="pl-k">=</span> <span class="pl-v">self</span>.launchPosList()</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#create launchers according to the list &#39;launcherpositions&#39;</span></td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line">        [<span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>launcher<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(pos), Launcher(<span class="pl-v">self</span>,pos, center, gap,</td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>)) <span class="pl-k">for</span> pos <span class="pl-k">in</span> <span class="pl-v">self</span>.launcherPositions]</td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line">   </td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">launchPosList</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        make a list of launcher positions and locations depending on the</span></td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        launcherConfig and border</span></td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Ugly implementation, feel free to efficify</span></td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#cast to string</span></td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.launcherConfig  <span class="pl-k">=</span> <span class="pl-c1">str</span>(<span class="pl-v">self</span>.launcherConfig)</td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Check for valid input</span></td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.launcherConfig.upper() <span class="pl-k">not</span> <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>A<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>B<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>C<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>D<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> <span class="pl-c1">Exception</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Launcherconfig must be either A, B, C or D<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#python 3 variant below</span></td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#raise Exception(&#39;Launcherconfig must be either A, B or C (case sensitive)&#39;)</span></td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide on launcher locations</span></td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line">        borX, borY <span class="pl-k">=</span> <span class="pl-v">self</span>.borders[<span class="pl-c1">0</span>]<span class="pl-k">/</span><span class="pl-c1">2.</span>,<span class="pl-v">self</span>.borders[<span class="pl-c1">1</span>]<span class="pl-k">/</span><span class="pl-c1">2.</span></td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line">        positions <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Get the offcenter locations depending on launcherconfig</span></td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line">        offs <span class="pl-k">=</span> <span class="pl-v">self</span>.offCenters[<span class="pl-v">self</span>.launcherConfig]</td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.launcherConfig <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>A<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># 8 launchers max, 1 left/right, 3 top/bottom</span></td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line">            positions.append([<span class="pl-k">-</span>borX,<span class="pl-c1">0</span>,<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line">            positions.extend([[<span class="pl-k">-</span>offs,borY,<span class="pl-k">-</span><span class="pl-c1">90</span>],[<span class="pl-c1">0</span>,borY,<span class="pl-k">-</span><span class="pl-c1">90</span>],[offs,borY,<span class="pl-k">-</span><span class="pl-c1">90</span>]])</td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line">            positions.append([borX,<span class="pl-c1">0</span>,<span class="pl-c1">180</span>])</td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line">            positions.extend([[offs,<span class="pl-k">-</span>borY,<span class="pl-c1">90</span>],[<span class="pl-c1">0</span>,<span class="pl-k">-</span>borY,<span class="pl-c1">90</span>],[<span class="pl-k">-</span>offs,<span class="pl-k">-</span>borY,<span class="pl-c1">90</span>]])</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.launcherConfig <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>B<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#check if its the right chipsize</span></td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.borderTag <span class="pl-k">&lt;</span> <span class="pl-c1">2</span> <span class="pl-k">or</span> <span class="pl-v">self</span>.borderTag <span class="pl-k">&gt;</span> <span class="pl-c1">4</span>:</td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">raise</span> <span class="pl-c1">Exception</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Configuration B should be used with chipsize 2 or 3<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#determine offCenterY</span></td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line">            offX, offY <span class="pl-k">=</span> offs[<span class="pl-c1">0</span>], offs[<span class="pl-v">self</span>.borderTag<span class="pl-k">-</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#populate position list</span></td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line">            positions.append([<span class="pl-k">-</span>borX, offY, <span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line">            positions.extend([[<span class="pl-k">-</span>offX, borY, <span class="pl-k">-</span><span class="pl-c1">90</span>],[offX, borY, <span class="pl-k">-</span><span class="pl-c1">90</span>]])</td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line">            positions.extend([[borX, offY, <span class="pl-c1">180</span>],[borX, <span class="pl-k">-</span>offY, <span class="pl-c1">180</span>]])</td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line">            positions.extend([[offX, <span class="pl-k">-</span>borY, <span class="pl-c1">90</span>],[<span class="pl-k">-</span>offX, <span class="pl-k">-</span>borY, <span class="pl-c1">90</span>]])</td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line">            positions.append([<span class="pl-k">-</span>borX, <span class="pl-k">-</span>offY, <span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.launcherConfig <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>C<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#first check if the border is 3:</span></td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.borderTag <span class="pl-k">!=</span> <span class="pl-c1">3</span>:</td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">raise</span> <span class="pl-c1">Exception</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Configuration C only works with bordersize 3<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">                <span class="pl-c">#Python 3 variant: raise Exception(&#39;Configuration 3 only works with bordersize 3&#39;)</span></td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">            offX1, offX2, offY1, offY2 <span class="pl-k">=</span> offs</td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">            positions.extend([[<span class="pl-k">-</span>borX, offY1, <span class="pl-c1">0</span>],[<span class="pl-k">-</span>borX, offY2, <span class="pl-c1">0</span>]])</td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">            positions.extend([[<span class="pl-k">-</span>offX2, borY,<span class="pl-k">-</span><span class="pl-c1">90</span>],[<span class="pl-k">-</span>offX1, borY,<span class="pl-k">-</span><span class="pl-c1">90</span>], </td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line">                [offX1, borY,<span class="pl-k">-</span><span class="pl-c1">90</span>], [offX2, borY,<span class="pl-k">-</span><span class="pl-c1">90</span>]])</td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line">            positions.extend([[borX, offY2, <span class="pl-c1">180</span>],[borX, offY1, <span class="pl-c1">180</span>], </td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line">                [borX, <span class="pl-k">-</span>offY1, <span class="pl-c1">180</span>], [borX, <span class="pl-k">-</span>offY2, <span class="pl-c1">180</span>]])</td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line">            positions.extend([[offX2, <span class="pl-k">-</span>borY, <span class="pl-c1">90</span>],[offX1, <span class="pl-k">-</span>borY, <span class="pl-c1">90</span>], </td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line">                [<span class="pl-k">-</span>offX1, <span class="pl-k">-</span>borY, <span class="pl-c1">90</span>], [<span class="pl-k">-</span>offX2, <span class="pl-k">-</span>borY, <span class="pl-c1">90</span>]])</td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">            positions.extend([[<span class="pl-k">-</span>borX, <span class="pl-k">-</span>offY2, <span class="pl-c1">0</span>],[<span class="pl-k">-</span>borX, <span class="pl-k">-</span>offY1, <span class="pl-c1">0</span>]])</td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.launcherConfig <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>D<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># 8 launchers max, 4 top/bottom</span></td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">            offX1, offX2 <span class="pl-k">=</span> offs</td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line">            positions.extend([[<span class="pl-k">-</span>offX1,borY,<span class="pl-k">-</span><span class="pl-c1">90</span>],[<span class="pl-k">-</span>offX2,borY,<span class="pl-k">-</span><span class="pl-c1">90</span>],[offX2,borY,<span class="pl-k">-</span><span class="pl-c1">90</span>],[offX1,borY,<span class="pl-k">-</span><span class="pl-c1">90</span>]])</td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line">            positions.extend([[offX1,<span class="pl-k">-</span>borY,<span class="pl-c1">90</span>],[offX2,<span class="pl-k">-</span>borY,<span class="pl-c1">90</span>],[<span class="pl-k">-</span>offX2,<span class="pl-k">-</span>borY,<span class="pl-c1">90</span>],[<span class="pl-k">-</span>offX1,<span class="pl-k">-</span>borY,<span class="pl-c1">90</span>]])</td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> positions    </td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addCrossArray</span>(<span class="pl-smi">self</span>, <span class="pl-smi">placeInfo</span>):</td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add alignment markers for e-beam at placeInfo</span></td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        At this moment, no options are given in the class (as I do not think</span></td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        they will be used), but they are available in the underlying function </span></td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        in maskDesign, feel free to add the options here too</span></td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.crossArrays <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>crossArray<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.crossArrays),</td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line">                CrossArray(<span class="pl-v">self</span>, placeInfo))</td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addText</span>(<span class="pl-smi">self</span>, <span class="pl-smi">text</span>, <span class="pl-smi">placeInfo</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">fontSize</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">font</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">layer</span><span class="pl-k">=</span><span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add labels to the chip</span></td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        If the coords are left to default, the text will be placed in the upper</span></td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        center of the chip</span></td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Chip labels go in layer 0, wafer Labels in layer 2</span></td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Different fonts are available (all Hershey fonts are available, as is a</span></td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        blockfont). Look at the gdsCAD documentation for details.</span></td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> font <span class="pl-k">==</span> <span class="pl-c1">None</span>: font <span class="pl-k">=</span> <span class="pl-v">self</span>.labelFont</td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> fontSize <span class="pl-k">==</span> <span class="pl-c1">None</span>: fontSize <span class="pl-k">=</span> <span class="pl-v">self</span>.labelFontSize</td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Determine some coordinates for the text</span></td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> placeInfo <span class="pl-k">==</span> <span class="pl-c1">None</span>: </td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line">            mtext <span class="pl-k">=</span> <span class="pl-c1">max</span>(text.split(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line">            x <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">len</span>(mtext)<span class="pl-k">*</span>fontSize<span class="pl-k">/</span><span class="pl-c1">4</span></td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line">            y <span class="pl-k">=</span> <span class="pl-v">self</span>.borders[<span class="pl-c1">1</span>]<span class="pl-k">/</span><span class="pl-c1">2</span> <span class="pl-k">-</span> fontSize</td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line">            placeInfo <span class="pl-k">=</span> (x,y)</td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.texts <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>text<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.texts), CText(<span class="pl-v">self</span>, text, fontSize,</td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">            placeInfo, font, rot, layer))</td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L676" class="blob-num js-line-number" data-line-number="676"></td>
        <td id="LC676" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L677" class="blob-num js-line-number" data-line-number="677"></td>
        <td id="LC677" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L678" class="blob-num js-line-number" data-line-number="678"></td>
        <td id="LC678" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L679" class="blob-num js-line-number" data-line-number="679"></td>
        <td id="LC679" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addChargeLine</span>(<span class="pl-smi">self</span>, <span class="pl-smi">placeInfoLaunch</span>, <span class="pl-smi">placeInfoTransmon</span>, <span class="pl-smi">gapLen</span><span class="pl-k">=</span><span class="pl-c1">25</span><span class="pl-k">*</span>um,</td>
      </tr>
      <tr>
        <td id="L680" class="blob-num js-line-number" data-line-number="680"></td>
        <td id="LC680" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">extraline</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">chargeOffset</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-smi">endrot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">startrot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L681" class="blob-num js-line-number" data-line-number="681"></td>
        <td id="LC681" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L682" class="blob-num js-line-number" data-line-number="682"></td>
        <td id="LC682" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a chargeLine from the Launcher connector to a transmon box</span></td>
      </tr>
      <tr>
        <td id="L683" class="blob-num js-line-number" data-line-number="683"></td>
        <td id="LC683" class="blob-code blob-code-inner js-file-line"><span class="pl-s">u</span></td>
      </tr>
      <tr>
        <td id="L684" class="blob-num js-line-number" data-line-number="684"></td>
        <td id="LC684" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Options:</span></td>
      </tr>
      <tr>
        <td id="L685" class="blob-num js-line-number" data-line-number="685"></td>
        <td id="LC685" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        gapLen: length of the gap</span></td>
      </tr>
      <tr>
        <td id="L686" class="blob-num js-line-number" data-line-number="686"></td>
        <td id="LC686" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        extraLine: CPW connected to the gap</span></td>
      </tr>
      <tr>
        <td id="L687" class="blob-num js-line-number" data-line-number="687"></td>
        <td id="LC687" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L688" class="blob-num js-line-number" data-line-number="688"></td>
        <td id="LC688" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        gapXoffset: shift the connection relative to the connection point</span></td>
      </tr>
      <tr>
        <td id="L689" class="blob-num js-line-number" data-line-number="689"></td>
        <td id="LC689" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L690" class="blob-num js-line-number" data-line-number="690"></td>
        <td id="LC690" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        endrot: rotation of the endpoint, including an arc: Specify if the last</span></td>
      </tr>
      <tr>
        <td id="L691" class="blob-num js-line-number" data-line-number="691"></td>
        <td id="LC691" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        turn is either left or right</span></td>
      </tr>
      <tr>
        <td id="L692" class="blob-num js-line-number" data-line-number="692"></td>
        <td id="LC692" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            so endrot = &#39;l&#39; or &#39;r&#39; or 0</span></td>
      </tr>
      <tr>
        <td id="L693" class="blob-num js-line-number" data-line-number="693"></td>
        <td id="LC693" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L694" class="blob-num js-line-number" data-line-number="694"></td>
        <td id="LC694" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        When connecting to coordinates rather than a Launcher, use startRot to get</span></td>
      </tr>
      <tr>
        <td id="L695" class="blob-num js-line-number" data-line-number="695"></td>
        <td id="LC695" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the correct initial rotation (its automatic from Objects)</span></td>
      </tr>
      <tr>
        <td id="L696" class="blob-num js-line-number" data-line-number="696"></td>
        <td id="LC696" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L697" class="blob-num js-line-number" data-line-number="697"></td>
        <td id="LC697" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L698" class="blob-num js-line-number" data-line-number="698"></td>
        <td id="LC698" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L699" class="blob-num js-line-number" data-line-number="699"></td>
        <td id="LC699" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.chargeLines <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L700" class="blob-num js-line-number" data-line-number="700"></td>
        <td id="LC700" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>chargeLine<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.chargeLines),</td>
      </tr>
      <tr>
        <td id="L701" class="blob-num js-line-number" data-line-number="701"></td>
        <td id="LC701" class="blob-code blob-code-inner js-file-line">                ChargeLine(<span class="pl-v">self</span>, placeInfoLaunch, placeInfoTransmon, gapLen,</td>
      </tr>
      <tr>
        <td id="L702" class="blob-num js-line-number" data-line-number="702"></td>
        <td id="LC702" class="blob-code blob-code-inner js-file-line">                    extraline, chargeOffset, endrot, startrot))</td>
      </tr>
      <tr>
        <td id="L703" class="blob-num js-line-number" data-line-number="703"></td>
        <td id="LC703" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L704" class="blob-num js-line-number" data-line-number="704"></td>
        <td id="LC704" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L705" class="blob-num js-line-number" data-line-number="705"></td>
        <td id="LC705" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L706" class="blob-num js-line-number" data-line-number="706"></td>
        <td id="LC706" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addFluxLine</span>(<span class="pl-smi">self</span>, <span class="pl-smi">placeInfoLaunch</span>, <span class="pl-smi">placeInfoTransmon</span>, <span class="pl-smi">extraLine</span><span class="pl-k">=</span><span class="pl-c1">0</span>,</td>
      </tr>
      <tr>
        <td id="L707" class="blob-num js-line-number" data-line-number="707"></td>
        <td id="LC707" class="blob-code blob-code-inner js-file-line">         <span class="pl-smi">fluxGap</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">fluxLen</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">fluxOffset</span> <span class="pl-k">=</span> (<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-smi">endrot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">startrot</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">name</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L708" class="blob-num js-line-number" data-line-number="708"></td>
        <td id="LC708" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L709" class="blob-num js-line-number" data-line-number="709"></td>
        <td id="LC709" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a flux Line from the Launcher connector to a transmon box</span></td>
      </tr>
      <tr>
        <td id="L710" class="blob-num js-line-number" data-line-number="710"></td>
        <td id="LC710" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L711" class="blob-num js-line-number" data-line-number="711"></td>
        <td id="LC711" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        options:</span></td>
      </tr>
      <tr>
        <td id="L712" class="blob-num js-line-number" data-line-number="712"></td>
        <td id="LC712" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        fluxGap = gap for current to flow between fluxLine and transmonbox</span></td>
      </tr>
      <tr>
        <td id="L713" class="blob-num js-line-number" data-line-number="713"></td>
        <td id="LC713" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        fluxLen = Length of the structure</span></td>
      </tr>
      <tr>
        <td id="L714" class="blob-num js-line-number" data-line-number="714"></td>
        <td id="LC714" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        fluxOffset = offsets in the x and y direction compared to the transmon</span></td>
      </tr>
      <tr>
        <td id="L715" class="blob-num js-line-number" data-line-number="715"></td>
        <td id="LC715" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        box</span></td>
      </tr>
      <tr>
        <td id="L716" class="blob-num js-line-number" data-line-number="716"></td>
        <td id="LC716" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L717" class="blob-num js-line-number" data-line-number="717"></td>
        <td id="LC717" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        endrot: rotation of the endpoint, including an arc: Specify if the last</span></td>
      </tr>
      <tr>
        <td id="L718" class="blob-num js-line-number" data-line-number="718"></td>
        <td id="LC718" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        turn is either left or right</span></td>
      </tr>
      <tr>
        <td id="L719" class="blob-num js-line-number" data-line-number="719"></td>
        <td id="LC719" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            so endrot = &#39;l&#39; or &#39;r&#39; or 0</span></td>
      </tr>
      <tr>
        <td id="L720" class="blob-num js-line-number" data-line-number="720"></td>
        <td id="LC720" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L721" class="blob-num js-line-number" data-line-number="721"></td>
        <td id="LC721" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L722" class="blob-num js-line-number" data-line-number="722"></td>
        <td id="LC722" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        When connecting to coordinates rather than a Launcher, use startRot to get</span></td>
      </tr>
      <tr>
        <td id="L723" class="blob-num js-line-number" data-line-number="723"></td>
        <td id="LC723" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the correct initial rotation (its automatic from Objects)</span></td>
      </tr>
      <tr>
        <td id="L724" class="blob-num js-line-number" data-line-number="724"></td>
        <td id="LC724" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L725" class="blob-num js-line-number" data-line-number="725"></td>
        <td id="LC725" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L726" class="blob-num js-line-number" data-line-number="726"></td>
        <td id="LC726" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L727" class="blob-num js-line-number" data-line-number="727"></td>
        <td id="LC727" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> fluxGap <span class="pl-k">==</span> <span class="pl-c1">None</span>: fluxGap <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>fluxGap<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L728" class="blob-num js-line-number" data-line-number="728"></td>
        <td id="LC728" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> fluxLen <span class="pl-k">==</span> <span class="pl-c1">None</span>: fluxLen <span class="pl-k">=</span> defaults[<span class="pl-s"><span class="pl-pds">&#39;</span>fluxLen<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L729" class="blob-num js-line-number" data-line-number="729"></td>
        <td id="LC729" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L730" class="blob-num js-line-number" data-line-number="730"></td>
        <td id="LC730" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fluxLines <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L731" class="blob-num js-line-number" data-line-number="731"></td>
        <td id="LC731" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L732" class="blob-num js-line-number" data-line-number="732"></td>
        <td id="LC732" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>,  name <span class="pl-k">if</span> name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>fluxLine<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(<span class="pl-v">self</span>.fluxLines),</td>
      </tr>
      <tr>
        <td id="L733" class="blob-num js-line-number" data-line-number="733"></td>
        <td id="LC733" class="blob-code blob-code-inner js-file-line">                FluxLine(<span class="pl-v">self</span>, placeInfoLaunch, placeInfoTransmon, fluxGap,</td>
      </tr>
      <tr>
        <td id="L734" class="blob-num js-line-number" data-line-number="734"></td>
        <td id="LC734" class="blob-code blob-code-inner js-file-line">                    extraLine, fluxLen, fluxOffset, endrot, startrot))</td>
      </tr>
      <tr>
        <td id="L735" class="blob-num js-line-number" data-line-number="735"></td>
        <td id="LC735" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L736" class="blob-num js-line-number" data-line-number="736"></td>
        <td id="LC736" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L737" class="blob-num js-line-number" data-line-number="737"></td>
        <td id="LC737" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addThinTenna</span>(<span class="pl-smi">self</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">totLen</span>, <span class="pl-smi">thinLen</span>, <span class="pl-smi">thin</span><span class="pl-k">=</span><span class="pl-c1">2</span><span class="pl-k">*</span>um, <span class="pl-smi">tapLen</span><span class="pl-k">=</span><span class="pl-c1">100</span><span class="pl-k">*</span>um,</td>
      </tr>
      <tr>
        <td id="L738" class="blob-num js-line-number" data-line-number="738"></td>
        <td id="LC738" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">preLen</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>, <span class="pl-smi">a1</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">b1</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">flip</span><span class="pl-k">=</span><span class="pl-c1">False</span>,<span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L739" class="blob-num js-line-number" data-line-number="739"></td>
        <td id="LC739" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L740" class="blob-num js-line-number" data-line-number="740"></td>
        <td id="LC740" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L741" class="blob-num js-line-number" data-line-number="741"></td>
        <td id="LC741" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a thinline antenna</span></td>
      </tr>
      <tr>
        <td id="L742" class="blob-num js-line-number" data-line-number="742"></td>
        <td id="LC742" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L743" class="blob-num js-line-number" data-line-number="743"></td>
        <td id="LC743" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L744" class="blob-num js-line-number" data-line-number="744"></td>
        <td id="LC744" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> a1 <span class="pl-k">==</span> <span class="pl-c1">None</span>: a1 <span class="pl-k">=</span> <span class="pl-v">self</span>.a1</td>
      </tr>
      <tr>
        <td id="L745" class="blob-num js-line-number" data-line-number="745"></td>
        <td id="LC745" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> b1 <span class="pl-k">==</span> <span class="pl-c1">None</span>: b1 <span class="pl-k">=</span> <span class="pl-v">self</span>.b1</td>
      </tr>
      <tr>
        <td id="L746" class="blob-num js-line-number" data-line-number="746"></td>
        <td id="LC746" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L747" class="blob-num js-line-number" data-line-number="747"></td>
        <td id="LC747" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.thinTennas <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L748" class="blob-num js-line-number" data-line-number="748"></td>
        <td id="LC748" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L749" class="blob-num js-line-number" data-line-number="749"></td>
        <td id="LC749" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">setattr</span>(<span class="pl-v">self</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>thinTenna<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-v">self</span>.thinTennas), </td>
      </tr>
      <tr>
        <td id="L750" class="blob-num js-line-number" data-line-number="750"></td>
        <td id="LC750" class="blob-code blob-code-inner js-file-line">                ThinTenna(<span class="pl-v">self</span>, placeInfo, totLen, thinLen, thin, tapLen,</td>
      </tr>
      <tr>
        <td id="L751" class="blob-num js-line-number" data-line-number="751"></td>
        <td id="LC751" class="blob-code blob-code-inner js-file-line">                    preLen, a1, b1, flip, rot))</td>
      </tr>
      <tr>
        <td id="L752" class="blob-num js-line-number" data-line-number="752"></td>
        <td id="LC752" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L753" class="blob-num js-line-number" data-line-number="753"></td>
        <td id="LC753" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L754" class="blob-num js-line-number" data-line-number="754"></td>
        <td id="LC754" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L755" class="blob-num js-line-number" data-line-number="755"></td>
        <td id="LC755" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">route</span>(<span class="pl-smi">self</span>, <span class="pl-smi">placeInfo1</span>, <span class="pl-smi">placeInfo2</span>, <span class="pl-smi">rot1</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">endrot</span><span class="pl-k">=</span><span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L756" class="blob-num js-line-number" data-line-number="756"></td>
        <td id="LC756" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L757" class="blob-num js-line-number" data-line-number="757"></td>
        <td id="LC757" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Draw a CPW from coords1 to coords2</span></td>
      </tr>
      <tr>
        <td id="L758" class="blob-num js-line-number" data-line-number="758"></td>
        <td id="LC758" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L759" class="blob-num js-line-number" data-line-number="759"></td>
        <td id="LC759" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        This function assumes that the final rotation is the same as the initial</span></td>
      </tr>
      <tr>
        <td id="L760" class="blob-num js-line-number" data-line-number="760"></td>
        <td id="LC760" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        rotation</span></td>
      </tr>
      <tr>
        <td id="L761" class="blob-num js-line-number" data-line-number="761"></td>
        <td id="LC761" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L762" class="blob-num js-line-number" data-line-number="762"></td>
        <td id="LC762" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        In case placeInfo is a set of coordinates for component 1, the rotation</span></td>
      </tr>
      <tr>
        <td id="L763" class="blob-num js-line-number" data-line-number="763"></td>
        <td id="LC763" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        at the start can be given in as rot1 (in degrees)</span></td>
      </tr>
      <tr>
        <td id="L764" class="blob-num js-line-number" data-line-number="764"></td>
        <td id="LC764" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L765" class="blob-num js-line-number" data-line-number="765"></td>
        <td id="LC765" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        startrot is an optional starting rotation that can be used with</span></td>
      </tr>
      <tr>
        <td id="L766" class="blob-num js-line-number" data-line-number="766"></td>
        <td id="LC766" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        placeInfo1 being an object, but when the rotation needs to be different</span></td>
      </tr>
      <tr>
        <td id="L767" class="blob-num js-line-number" data-line-number="767"></td>
        <td id="LC767" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        from that objects rotation</span></td>
      </tr>
      <tr>
        <td id="L768" class="blob-num js-line-number" data-line-number="768"></td>
        <td id="LC768" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L769" class="blob-num js-line-number" data-line-number="769"></td>
        <td id="LC769" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L770" class="blob-num js-line-number" data-line-number="770"></td>
        <td id="LC770" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Get coordinates for placeInfo1</span></td>
      </tr>
      <tr>
        <td id="L771" class="blob-num js-line-number" data-line-number="771"></td>
        <td id="LC771" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo1) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L772" class="blob-num js-line-number" data-line-number="772"></td>
        <td id="LC772" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(<span class="pl-v">self</span>, placeInfo1.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L773" class="blob-num js-line-number" data-line-number="773"></td>
        <td id="LC773" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.startcoords <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo1.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L774" class="blob-num js-line-number" data-line-number="774"></td>
        <td id="LC774" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.startrot <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, <span class="pl-s"><span class="pl-pds">&#39;</span>rot<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L775" class="blob-num js-line-number" data-line-number="775"></td>
        <td id="LC775" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L776" class="blob-num js-line-number" data-line-number="776"></td>
        <td id="LC776" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.startcoords <span class="pl-k">=</span> placeInfo1</td>
      </tr>
      <tr>
        <td id="L777" class="blob-num js-line-number" data-line-number="777"></td>
        <td id="LC777" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.startrot <span class="pl-k">=</span> rot1 </td>
      </tr>
      <tr>
        <td id="L778" class="blob-num js-line-number" data-line-number="778"></td>
        <td id="LC778" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>startrot is <span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.startrot</td>
      </tr>
      <tr>
        <td id="L779" class="blob-num js-line-number" data-line-number="779"></td>
        <td id="LC779" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L780" class="blob-num js-line-number" data-line-number="780"></td>
        <td id="LC780" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Get coordinates for placeInfo2</span></td>
      </tr>
      <tr>
        <td id="L781" class="blob-num js-line-number" data-line-number="781"></td>
        <td id="LC781" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo2) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L782" class="blob-num js-line-number" data-line-number="782"></td>
        <td id="LC782" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(<span class="pl-v">self</span>, placeInfo2.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L783" class="blob-num js-line-number" data-line-number="783"></td>
        <td id="LC783" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.endcoords <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo2.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L784" class="blob-num js-line-number" data-line-number="784"></td>
        <td id="LC784" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L785" class="blob-num js-line-number" data-line-number="785"></td>
        <td id="LC785" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.endcoords <span class="pl-k">=</span> placeInfo2</td>
      </tr>
      <tr>
        <td id="L786" class="blob-num js-line-number" data-line-number="786"></td>
        <td id="LC786" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L787" class="blob-num js-line-number" data-line-number="787"></td>
        <td id="LC787" class="blob-code blob-code-inner js-file-line">        dx <span class="pl-k">=</span> <span class="pl-v">self</span>.endcoords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.startcoords[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L788" class="blob-num js-line-number" data-line-number="788"></td>
        <td id="LC788" class="blob-code blob-code-inner js-file-line">        dy <span class="pl-k">=</span> <span class="pl-v">self</span>.endcoords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.startcoords[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L789" class="blob-num js-line-number" data-line-number="789"></td>
        <td id="LC789" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L790" class="blob-num js-line-number" data-line-number="790"></td>
        <td id="LC790" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Re-express as an upgoing problem</span></td>
      </tr>
      <tr>
        <td id="L791" class="blob-num js-line-number" data-line-number="791"></td>
        <td id="LC791" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.startrot<span class="pl-k">%</span><span class="pl-c1">90</span> <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L792" class="blob-num js-line-number" data-line-number="792"></td>
        <td id="LC792" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Use only multiples of 90 degrees when connecting a flux or gateline<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L793" class="blob-num js-line-number" data-line-number="793"></td>
        <td id="LC793" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L794" class="blob-num js-line-number" data-line-number="794"></td>
        <td id="LC794" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.startrot <span class="pl-k">==</span> <span class="pl-c1">90</span>: <span class="pl-c">#nothing changes</span></td>
      </tr>
      <tr>
        <td id="L795" class="blob-num js-line-number" data-line-number="795"></td>
        <td id="LC795" class="blob-code blob-code-inner js-file-line">            tdx <span class="pl-k">=</span> dx</td>
      </tr>
      <tr>
        <td id="L796" class="blob-num js-line-number" data-line-number="796"></td>
        <td id="LC796" class="blob-code blob-code-inner js-file-line">            tdy <span class="pl-k">=</span> dy</td>
      </tr>
      <tr>
        <td id="L797" class="blob-num js-line-number" data-line-number="797"></td>
        <td id="LC797" class="blob-code blob-code-inner js-file-line">            rotBack <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L798" class="blob-num js-line-number" data-line-number="798"></td>
        <td id="LC798" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-v">self</span>.startrot <span class="pl-k">==</span> <span class="pl-c1">180</span>:</td>
      </tr>
      <tr>
        <td id="L799" class="blob-num js-line-number" data-line-number="799"></td>
        <td id="LC799" class="blob-code blob-code-inner js-file-line">            tdx <span class="pl-k">=</span> dy</td>
      </tr>
      <tr>
        <td id="L800" class="blob-num js-line-number" data-line-number="800"></td>
        <td id="LC800" class="blob-code blob-code-inner js-file-line">            tdy <span class="pl-k">=</span> <span class="pl-k">-</span>dx</td>
      </tr>
      <tr>
        <td id="L801" class="blob-num js-line-number" data-line-number="801"></td>
        <td id="LC801" class="blob-code blob-code-inner js-file-line">            rotBack <span class="pl-k">=</span> <span class="pl-c1">90</span></td>
      </tr>
      <tr>
        <td id="L802" class="blob-num js-line-number" data-line-number="802"></td>
        <td id="LC802" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-v">self</span>.startrot <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L803" class="blob-num js-line-number" data-line-number="803"></td>
        <td id="LC803" class="blob-code blob-code-inner js-file-line">            tdx <span class="pl-k">=</span> <span class="pl-k">-</span>dy</td>
      </tr>
      <tr>
        <td id="L804" class="blob-num js-line-number" data-line-number="804"></td>
        <td id="LC804" class="blob-code blob-code-inner js-file-line">            tdy <span class="pl-k">=</span> dx</td>
      </tr>
      <tr>
        <td id="L805" class="blob-num js-line-number" data-line-number="805"></td>
        <td id="LC805" class="blob-code blob-code-inner js-file-line">            rotBack <span class="pl-k">=</span> <span class="pl-c1">270</span></td>
      </tr>
      <tr>
        <td id="L806" class="blob-num js-line-number" data-line-number="806"></td>
        <td id="LC806" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-v">self</span>.startrot <span class="pl-k">==</span> <span class="pl-c1">270</span> <span class="pl-k">or</span> <span class="pl-k">-</span><span class="pl-c1">90</span>:</td>
      </tr>
      <tr>
        <td id="L807" class="blob-num js-line-number" data-line-number="807"></td>
        <td id="LC807" class="blob-code blob-code-inner js-file-line">            tdx <span class="pl-k">=</span> <span class="pl-k">-</span>dx</td>
      </tr>
      <tr>
        <td id="L808" class="blob-num js-line-number" data-line-number="808"></td>
        <td id="LC808" class="blob-code blob-code-inner js-file-line">            tdy <span class="pl-k">=</span> <span class="pl-k">-</span>dy</td>
      </tr>
      <tr>
        <td id="L809" class="blob-num js-line-number" data-line-number="809"></td>
        <td id="LC809" class="blob-code blob-code-inner js-file-line">            rotBack <span class="pl-k">=</span> <span class="pl-c1">180</span></td>
      </tr>
      <tr>
        <td id="L810" class="blob-num js-line-number" data-line-number="810"></td>
        <td id="LC810" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L811" class="blob-num js-line-number" data-line-number="811"></td>
        <td id="LC811" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>tdx, tdy are<span class="pl-pds">&#39;</span></span>, tdx, tdy</td>
      </tr>
      <tr>
        <td id="L812" class="blob-num js-line-number" data-line-number="812"></td>
        <td id="LC812" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L813" class="blob-num js-line-number" data-line-number="813"></td>
        <td id="LC813" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> endrot <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>l<span class="pl-pds">&#39;</span></span>: </td>
      </tr>
      <tr>
        <td id="L814" class="blob-num js-line-number" data-line-number="814"></td>
        <td id="LC814" class="blob-code blob-code-inner js-file-line">            tdx <span class="pl-k">+=</span> <span class="pl-v">self</span>.rbend</td>
      </tr>
      <tr>
        <td id="L815" class="blob-num js-line-number" data-line-number="815"></td>
        <td id="LC815" class="blob-code blob-code-inner js-file-line">            tdy <span class="pl-k">-=</span> <span class="pl-v">self</span>.rbend</td>
      </tr>
      <tr>
        <td id="L816" class="blob-num js-line-number" data-line-number="816"></td>
        <td id="LC816" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> endrot <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>: </td>
      </tr>
      <tr>
        <td id="L817" class="blob-num js-line-number" data-line-number="817"></td>
        <td id="LC817" class="blob-code blob-code-inner js-file-line">            tdx <span class="pl-k">-=</span> <span class="pl-v">self</span>.rbend</td>
      </tr>
      <tr>
        <td id="L818" class="blob-num js-line-number" data-line-number="818"></td>
        <td id="LC818" class="blob-code blob-code-inner js-file-line">            tdy <span class="pl-k">-=</span> <span class="pl-v">self</span>.rbend</td>
      </tr>
      <tr>
        <td id="L819" class="blob-num js-line-number" data-line-number="819"></td>
        <td id="LC819" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L820" class="blob-num js-line-number" data-line-number="820"></td>
        <td id="LC820" class="blob-code blob-code-inner js-file-line">        routeCell <span class="pl-k">=</span> md.CPWroute(<span class="pl-v">self</span>.startcoords, tdx, tdy, <span class="pl-smi">rot</span> <span class="pl-k">=</span> rotBack,</td>
      </tr>
      <tr>
        <td id="L821" class="blob-num js-line-number" data-line-number="821"></td>
        <td id="LC821" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">endrot</span><span class="pl-k">=</span>endrot) </td>
      </tr>
      <tr>
        <td id="L822" class="blob-num js-line-number" data-line-number="822"></td>
        <td id="LC822" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.topCell.add(routeCell)</td>
      </tr>
      <tr>
        <td id="L823" class="blob-num js-line-number" data-line-number="823"></td>
        <td id="LC823" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L824" class="blob-num js-line-number" data-line-number="824"></td>
        <td id="LC824" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L825" class="blob-num js-line-number" data-line-number="825"></td>
        <td id="LC825" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">save</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L826" class="blob-num js-line-number" data-line-number="826"></td>
        <td id="LC826" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.layout.add(<span class="pl-v">self</span>.topCell)</td>
      </tr>
      <tr>
        <td id="L827" class="blob-num js-line-number" data-line-number="827"></td>
        <td id="LC827" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.layout.save(<span class="pl-v">self</span>.fileName)</td>
      </tr>
      <tr>
        <td id="L828" class="blob-num js-line-number" data-line-number="828"></td>
        <td id="LC828" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L829" class="blob-num js-line-number" data-line-number="829"></td>
        <td id="LC829" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">show</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L830" class="blob-num js-line-number" data-line-number="830"></td>
        <td id="LC830" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.layout.add(<span class="pl-v">self</span>.topCell)</td>
      </tr>
      <tr>
        <td id="L831" class="blob-num js-line-number" data-line-number="831"></td>
        <td id="LC831" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.layout.show()</td>
      </tr>
      <tr>
        <td id="L832" class="blob-num js-line-number" data-line-number="832"></td>
        <td id="LC832" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L833" class="blob-num js-line-number" data-line-number="833"></td>
        <td id="LC833" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#=============================================================================</span></td>
      </tr>
      <tr>
        <td id="L834" class="blob-num js-line-number" data-line-number="834"></td>
        <td id="LC834" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#------------------------------COMPONENT OBJECTS-------------------------------</span></td>
      </tr>
      <tr>
        <td id="L835" class="blob-num js-line-number" data-line-number="835"></td>
        <td id="LC835" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#=============================================================================</span></td>
      </tr>
      <tr>
        <td id="L836" class="blob-num js-line-number" data-line-number="836"></td>
        <td id="LC836" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L837" class="blob-num js-line-number" data-line-number="837"></td>
        <td id="LC837" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L838" class="blob-num js-line-number" data-line-number="838"></td>
        <td id="LC838" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Border</span>:</td>
      </tr>
      <tr>
        <td id="L839" class="blob-num js-line-number" data-line-number="839"></td>
        <td id="LC839" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L840" class="blob-num js-line-number" data-line-number="840"></td>
        <td id="LC840" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    sample borders</span></td>
      </tr>
      <tr>
        <td id="L841" class="blob-num js-line-number" data-line-number="841"></td>
        <td id="LC841" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L842" class="blob-num js-line-number" data-line-number="842"></td>
        <td id="LC842" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L843" class="blob-num js-line-number" data-line-number="843"></td>
        <td id="LC843" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>,<span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L844" class="blob-num js-line-number" data-line-number="844"></td>
        <td id="LC844" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L845" class="blob-num js-line-number" data-line-number="845"></td>
        <td id="LC845" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#make the cell</span></td>
      </tr>
      <tr>
        <td id="L846" class="blob-num js-line-number" data-line-number="846"></td>
        <td id="LC846" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span>  sampleX.posRes:    <span class="pl-c"># For positive photoresist samples</span></td>
      </tr>
      <tr>
        <td id="L847" class="blob-num js-line-number" data-line-number="847"></td>
        <td id="LC847" class="blob-code blob-code-inner js-file-line">            whiteGap <span class="pl-k">=</span> sampleX.borderGap <span class="pl-k">-</span> sampleX.posResEdge</td>
      </tr>
      <tr>
        <td id="L848" class="blob-num js-line-number" data-line-number="848"></td>
        <td id="LC848" class="blob-code blob-code-inner js-file-line">            xborder, yborder <span class="pl-k">=</span> sampleX.borders[<span class="pl-c1">0</span>] <span class="pl-k">+</span> whiteGap, sampleX.borders[<span class="pl-c1">1</span>] <span class="pl-k">+</span> whiteGap</td>
      </tr>
      <tr>
        <td id="L849" class="blob-num js-line-number" data-line-number="849"></td>
        <td id="LC849" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.borderA(xborder, yborder, sampleX.posResEdge, sampleX.alignPos, <span class="pl-smi">layer</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L850" class="blob-num js-line-number" data-line-number="850"></td>
        <td id="LC850" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:               <span class="pl-c"># For negative photoresist samples</span></td>
      </tr>
      <tr>
        <td id="L851" class="blob-num js-line-number" data-line-number="851"></td>
        <td id="LC851" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.borderA(sampleX.borders[<span class="pl-c1">0</span>],sampleX.borders[<span class="pl-c1">1</span>],</td>
      </tr>
      <tr>
        <td id="L852" class="blob-num js-line-number" data-line-number="852"></td>
        <td id="LC852" class="blob-code blob-code-inner js-file-line">                    sampleX.borderGap, sampleX.alignPos)</td>
      </tr>
      <tr>
        <td id="L853" class="blob-num js-line-number" data-line-number="853"></td>
        <td id="LC853" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L854" class="blob-num js-line-number" data-line-number="854"></td>
        <td id="LC854" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L855" class="blob-num js-line-number" data-line-number="855"></td>
        <td id="LC855" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L856" class="blob-num js-line-number" data-line-number="856"></td>
        <td id="LC856" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Launcher</span>:</td>
      </tr>
      <tr>
        <td id="L857" class="blob-num js-line-number" data-line-number="857"></td>
        <td id="LC857" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L858" class="blob-num js-line-number" data-line-number="858"></td>
        <td id="LC858" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Add the launchers to the chip</span></td>
      </tr>
      <tr>
        <td id="L859" class="blob-num js-line-number" data-line-number="859"></td>
        <td id="LC859" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L860" class="blob-num js-line-number" data-line-number="860"></td>
        <td id="LC860" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L861" class="blob-num js-line-number" data-line-number="861"></td>
        <td id="LC861" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">center</span>, <span class="pl-smi">gap</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L862" class="blob-num js-line-number" data-line-number="862"></td>
        <td id="LC862" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L863" class="blob-num js-line-number" data-line-number="863"></td>
        <td id="LC863" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        make the launchers</span></td>
      </tr>
      <tr>
        <td id="L864" class="blob-num js-line-number" data-line-number="864"></td>
        <td id="LC864" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L865" class="blob-num js-line-number" data-line-number="865"></td>
        <td id="LC865" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        pos is the position of this specific launcher, counting from the center</span></td>
      </tr>
      <tr>
        <td id="L866" class="blob-num js-line-number" data-line-number="866"></td>
        <td id="LC866" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        left</span></td>
      </tr>
      <tr>
        <td id="L867" class="blob-num js-line-number" data-line-number="867"></td>
        <td id="LC867" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L868" class="blob-num js-line-number" data-line-number="868"></td>
        <td id="LC868" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L869" class="blob-num js-line-number" data-line-number="869"></td>
        <td id="LC869" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#initialize variables</span></td>
      </tr>
      <tr>
        <td id="L870" class="blob-num js-line-number" data-line-number="870"></td>
        <td id="LC870" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L871" class="blob-num js-line-number" data-line-number="871"></td>
        <td id="LC871" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L872" class="blob-num js-line-number" data-line-number="872"></td>
        <td id="LC872" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L873" class="blob-num js-line-number" data-line-number="873"></td>
        <td id="LC873" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L874" class="blob-num js-line-number" data-line-number="874"></td>
        <td id="LC874" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">int</span>:</td>
      </tr>
      <tr>
        <td id="L875" class="blob-num js-line-number" data-line-number="875"></td>
        <td id="LC875" class="blob-code blob-code-inner js-file-line">            x, y, rot <span class="pl-k">=</span> sampleX.launcherLocations[placeInfo]</td>
      </tr>
      <tr>
        <td id="L876" class="blob-num js-line-number" data-line-number="876"></td>
        <td id="LC876" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L877" class="blob-num js-line-number" data-line-number="877"></td>
        <td id="LC877" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L878" class="blob-num js-line-number" data-line-number="878"></td>
        <td id="LC878" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (x, y)</td>
      </tr>
      <tr>
        <td id="L879" class="blob-num js-line-number" data-line-number="879"></td>
        <td id="LC879" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L880" class="blob-num js-line-number" data-line-number="880"></td>
        <td id="LC880" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L881" class="blob-num js-line-number" data-line-number="881"></td>
        <td id="LC881" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L882" class="blob-num js-line-number" data-line-number="882"></td>
        <td id="LC882" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L883" class="blob-num js-line-number" data-line-number="883"></td>
        <td id="LC883" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L884" class="blob-num js-line-number" data-line-number="884"></td>
        <td id="LC884" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for size of device</span></td>
      </tr>
      <tr>
        <td id="L885" class="blob-num js-line-number" data-line-number="885"></td>
        <td id="LC885" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.taperLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)),</td>
      </tr>
      <tr>
        <td id="L886" class="blob-num js-line-number" data-line-number="886"></td>
        <td id="LC886" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.taperLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L887" class="blob-num js-line-number" data-line-number="887"></td>
        <td id="LC887" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">tuple</span> <span class="pl-k">or</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">list</span>:</td>
      </tr>
      <tr>
        <td id="L888" class="blob-num js-line-number" data-line-number="888"></td>
        <td id="LC888" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L889" class="blob-num js-line-number" data-line-number="889"></td>
        <td id="LC889" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L890" class="blob-num js-line-number" data-line-number="890"></td>
        <td id="LC890" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L891" class="blob-num js-line-number" data-line-number="891"></td>
        <td id="LC891" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#make the cell, using default variables</span></td>
      </tr>
      <tr>
        <td id="L892" class="blob-num js-line-number" data-line-number="892"></td>
        <td id="LC892" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.launcher(<span class="pl-v">self</span>.coords, <span class="pl-smi">center</span><span class="pl-k">=</span>center, <span class="pl-smi">gap</span><span class="pl-k">=</span>gap, <span class="pl-smi">rot</span><span class="pl-k">=</span>rot)</td>
      </tr>
      <tr>
        <td id="L893" class="blob-num js-line-number" data-line-number="893"></td>
        <td id="LC893" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L894" class="blob-num js-line-number" data-line-number="894"></td>
        <td id="LC894" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#easier typing</span></td>
      </tr>
      <tr>
        <td id="L895" class="blob-num js-line-number" data-line-number="895"></td>
        <td id="LC895" class="blob-code blob-code-inner js-file-line">        x, y  <span class="pl-k">=</span> <span class="pl-v">self</span>.coords</td>
      </tr>
      <tr>
        <td id="L896" class="blob-num js-line-number" data-line-number="896"></td>
        <td id="LC896" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L897" class="blob-num js-line-number" data-line-number="897"></td>
        <td id="LC897" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Define connection points</span></td>
      </tr>
      <tr>
        <td id="L898" class="blob-num js-line-number" data-line-number="898"></td>
        <td id="LC898" class="blob-code blob-code-inner js-file-line">        totlen <span class="pl-k">=</span> sampleX.launcherTlen<span class="pl-k">+</span>sampleX.launcherWlen</td>
      </tr>
      <tr>
        <td id="L899" class="blob-num js-line-number" data-line-number="899"></td>
        <td id="LC899" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectDistance <span class="pl-k">=</span> (totlen<span class="pl-k">*</span>np.cos(rad(rot)), totlen<span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L900" class="blob-num js-line-number" data-line-number="900"></td>
        <td id="LC900" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connect <span class="pl-k">=</span> (x <span class="pl-k">+</span> <span class="pl-v">self</span>.connectDistance[<span class="pl-c1">0</span>], y <span class="pl-k">+</span> <span class="pl-v">self</span>.connectDistance[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L901" class="blob-num js-line-number" data-line-number="901"></td>
        <td id="LC901" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L902" class="blob-num js-line-number" data-line-number="902"></td>
        <td id="LC902" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#add cell to sample topcell</span></td>
      </tr>
      <tr>
        <td id="L903" class="blob-num js-line-number" data-line-number="903"></td>
        <td id="LC903" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L904" class="blob-num js-line-number" data-line-number="904"></td>
        <td id="LC904" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L905" class="blob-num js-line-number" data-line-number="905"></td>
        <td id="LC905" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L906" class="blob-num js-line-number" data-line-number="906"></td>
        <td id="LC906" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Taper</span>:</td>
      </tr>
      <tr>
        <td id="L907" class="blob-num js-line-number" data-line-number="907"></td>
        <td id="LC907" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L908" class="blob-num js-line-number" data-line-number="908"></td>
        <td id="LC908" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">taperLen</span>, <span class="pl-smi">startCenter</span>, <span class="pl-smi">endCenter</span>, <span class="pl-smi">placeInfo</span>,</td>
      </tr>
      <tr>
        <td id="L909" class="blob-num js-line-number" data-line-number="909"></td>
        <td id="LC909" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">abr</span>, <span class="pl-smi">rot</span>, <span class="pl-smi">flip</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-smi">noground</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L910" class="blob-num js-line-number" data-line-number="910"></td>
        <td id="LC910" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L911" class="blob-num js-line-number" data-line-number="911"></td>
        <td id="LC911" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Initialize attributes</span></td>
      </tr>
      <tr>
        <td id="L912" class="blob-num js-line-number" data-line-number="912"></td>
        <td id="LC912" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.startCenter <span class="pl-k">=</span> startCenter</td>
      </tr>
      <tr>
        <td id="L913" class="blob-num js-line-number" data-line-number="913"></td>
        <td id="LC913" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.endCenter <span class="pl-k">=</span> endCenter</td>
      </tr>
      <tr>
        <td id="L914" class="blob-num js-line-number" data-line-number="914"></td>
        <td id="LC914" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.taperLen <span class="pl-k">=</span> taperLen</td>
      </tr>
      <tr>
        <td id="L915" class="blob-num js-line-number" data-line-number="915"></td>
        <td id="LC915" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.abr <span class="pl-k">=</span> abr</td>
      </tr>
      <tr>
        <td id="L916" class="blob-num js-line-number" data-line-number="916"></td>
        <td id="LC916" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L917" class="blob-num js-line-number" data-line-number="917"></td>
        <td id="LC917" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.flip <span class="pl-k">=</span> flip</td>
      </tr>
      <tr>
        <td id="L918" class="blob-num js-line-number" data-line-number="918"></td>
        <td id="LC918" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.noground <span class="pl-k">=</span> noground</td>
      </tr>
      <tr>
        <td id="L919" class="blob-num js-line-number" data-line-number="919"></td>
        <td id="LC919" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L920" class="blob-num js-line-number" data-line-number="920"></td>
        <td id="LC920" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L921" class="blob-num js-line-number" data-line-number="921"></td>
        <td id="LC921" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L922" class="blob-num js-line-number" data-line-number="922"></td>
        <td id="LC922" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L923" class="blob-num js-line-number" data-line-number="923"></td>
        <td id="LC923" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L924" class="blob-num js-line-number" data-line-number="924"></td>
        <td id="LC924" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L925" class="blob-num js-line-number" data-line-number="925"></td>
        <td id="LC925" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for size of device</span></td>
      </tr>
      <tr>
        <td id="L926" class="blob-num js-line-number" data-line-number="926"></td>
        <td id="LC926" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.taperLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)),</td>
      </tr>
      <tr>
        <td id="L927" class="blob-num js-line-number" data-line-number="927"></td>
        <td id="LC927" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.taperLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L928" class="blob-num js-line-number" data-line-number="928"></td>
        <td id="LC928" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L929" class="blob-num js-line-number" data-line-number="929"></td>
        <td id="LC929" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L930" class="blob-num js-line-number" data-line-number="930"></td>
        <td id="LC930" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L931" class="blob-num js-line-number" data-line-number="931"></td>
        <td id="LC931" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L932" class="blob-num js-line-number" data-line-number="932"></td>
        <td id="LC932" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Taper is centered around the origin</span></td>
      </tr>
      <tr>
        <td id="L933" class="blob-num js-line-number" data-line-number="933"></td>
        <td id="LC933" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.taperLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L934" class="blob-num js-line-number" data-line-number="934"></td>
        <td id="LC934" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.taperLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L935" class="blob-num js-line-number" data-line-number="935"></td>
        <td id="LC935" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.taperLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L936" class="blob-num js-line-number" data-line-number="936"></td>
        <td id="LC936" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.taperLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L937" class="blob-num js-line-number" data-line-number="937"></td>
        <td id="LC937" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L938" class="blob-num js-line-number" data-line-number="938"></td>
        <td id="LC938" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#create and add the Cell</span></td>
      </tr>
      <tr>
        <td id="L939" class="blob-num js-line-number" data-line-number="939"></td>
        <td id="LC939" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell()</td>
      </tr>
      <tr>
        <td id="L940" class="blob-num js-line-number" data-line-number="940"></td>
        <td id="LC940" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L941" class="blob-num js-line-number" data-line-number="941"></td>
        <td id="LC941" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L942" class="blob-num js-line-number" data-line-number="942"></td>
        <td id="LC942" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L943" class="blob-num js-line-number" data-line-number="943"></td>
        <td id="LC943" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L944" class="blob-num js-line-number" data-line-number="944"></td>
        <td id="LC944" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        make the cad Cell reference of the Taper</span></td>
      </tr>
      <tr>
        <td id="L945" class="blob-num js-line-number" data-line-number="945"></td>
        <td id="LC945" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L946" class="blob-num js-line-number" data-line-number="946"></td>
        <td id="LC946" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>drawing a Taper, startCenter  = <span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.startCenter </td>
      </tr>
      <tr>
        <td id="L947" class="blob-num js-line-number" data-line-number="947"></td>
        <td id="LC947" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L948" class="blob-num js-line-number" data-line-number="948"></td>
        <td id="LC948" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># outer lines</span></td>
      </tr>
      <tr>
        <td id="L949" class="blob-num js-line-number" data-line-number="949"></td>
        <td id="LC949" class="blob-code blob-code-inner js-file-line">        startOuter <span class="pl-k">=</span> <span class="pl-v">self</span>.abr<span class="pl-k">*</span><span class="pl-v">self</span>.startCenter</td>
      </tr>
      <tr>
        <td id="L950" class="blob-num js-line-number" data-line-number="950"></td>
        <td id="LC950" class="blob-code blob-code-inner js-file-line">        endOuter <span class="pl-k">=</span> <span class="pl-v">self</span>.abr<span class="pl-k">*</span><span class="pl-v">self</span>.endCenter</td>
      </tr>
      <tr>
        <td id="L951" class="blob-num js-line-number" data-line-number="951"></td>
        <td id="LC951" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L952" class="blob-num js-line-number" data-line-number="952"></td>
        <td id="LC952" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.taper(<span class="pl-v">self</span>.coords, <span class="pl-v">self</span>.taperLen, startOuter, endOuter,</td>
      </tr>
      <tr>
        <td id="L953" class="blob-num js-line-number" data-line-number="953"></td>
        <td id="LC953" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.startCenter, <span class="pl-v">self</span>.endCenter, <span class="pl-v">self</span>.rot, <span class="pl-v">self</span>.flip, <span class="pl-v">self</span>.noground)</td>
      </tr>
      <tr>
        <td id="L954" class="blob-num js-line-number" data-line-number="954"></td>
        <td id="LC954" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L955" class="blob-num js-line-number" data-line-number="955"></td>
        <td id="LC955" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L956" class="blob-num js-line-number" data-line-number="956"></td>
        <td id="LC956" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L957" class="blob-num js-line-number" data-line-number="957"></td>
        <td id="LC957" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">CPW</span>:</td>
      </tr>
      <tr>
        <td id="L958" class="blob-num js-line-number" data-line-number="958"></td>
        <td id="LC958" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L959" class="blob-num js-line-number" data-line-number="959"></td>
        <td id="LC959" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">leng</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">bridges</span>, <span class="pl-smi">bridgeDistance</span>, <span class="pl-smi">bridgeStart</span>,</td>
      </tr>
      <tr>
        <td id="L960" class="blob-num js-line-number" data-line-number="960"></td>
        <td id="LC960" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">bridgeEnd</span>, <span class="pl-smi">closeA</span>, <span class="pl-smi">closeB</span>, <span class="pl-smi">flip</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L961" class="blob-num js-line-number" data-line-number="961"></td>
        <td id="LC961" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L962" class="blob-num js-line-number" data-line-number="962"></td>
        <td id="LC962" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Initialize the object</span></td>
      </tr>
      <tr>
        <td id="L963" class="blob-num js-line-number" data-line-number="963"></td>
        <td id="LC963" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L964" class="blob-num js-line-number" data-line-number="964"></td>
        <td id="LC964" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L965" class="blob-num js-line-number" data-line-number="965"></td>
        <td id="LC965" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.leng <span class="pl-k">=</span> leng</td>
      </tr>
      <tr>
        <td id="L966" class="blob-num js-line-number" data-line-number="966"></td>
        <td id="LC966" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L967" class="blob-num js-line-number" data-line-number="967"></td>
        <td id="LC967" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridges <span class="pl-k">=</span> bridges</td>
      </tr>
      <tr>
        <td id="L968" class="blob-num js-line-number" data-line-number="968"></td>
        <td id="LC968" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridgeStart<span class="pl-k">=</span> bridgeStart</td>
      </tr>
      <tr>
        <td id="L969" class="blob-num js-line-number" data-line-number="969"></td>
        <td id="LC969" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridgeEnd<span class="pl-k">=</span> bridgeEnd</td>
      </tr>
      <tr>
        <td id="L970" class="blob-num js-line-number" data-line-number="970"></td>
        <td id="LC970" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridgeDistance <span class="pl-k">=</span> bridgeDistance</td>
      </tr>
      <tr>
        <td id="L971" class="blob-num js-line-number" data-line-number="971"></td>
        <td id="LC971" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.closeA <span class="pl-k">=</span> closeA</td>
      </tr>
      <tr>
        <td id="L972" class="blob-num js-line-number" data-line-number="972"></td>
        <td id="LC972" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.closeB <span class="pl-k">=</span> closeB</td>
      </tr>
      <tr>
        <td id="L973" class="blob-num js-line-number" data-line-number="973"></td>
        <td id="LC973" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.flip <span class="pl-k">=</span> flip</td>
      </tr>
      <tr>
        <td id="L974" class="blob-num js-line-number" data-line-number="974"></td>
        <td id="LC974" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L975" class="blob-num js-line-number" data-line-number="975"></td>
        <td id="LC975" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L976" class="blob-num js-line-number" data-line-number="976"></td>
        <td id="LC976" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L977" class="blob-num js-line-number" data-line-number="977"></td>
        <td id="LC977" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L978" class="blob-num js-line-number" data-line-number="978"></td>
        <td id="LC978" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L979" class="blob-num js-line-number" data-line-number="979"></td>
        <td id="LC979" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L980" class="blob-num js-line-number" data-line-number="980"></td>
        <td id="LC980" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for size of device</span></td>
      </tr>
      <tr>
        <td id="L981" class="blob-num js-line-number" data-line-number="981"></td>
        <td id="LC981" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.flip:</td>
      </tr>
      <tr>
        <td id="L982" class="blob-num js-line-number" data-line-number="982"></td>
        <td id="LC982" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)),</td>
      </tr>
      <tr>
        <td id="L983" class="blob-num js-line-number" data-line-number="983"></td>
        <td id="LC983" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L984" class="blob-num js-line-number" data-line-number="984"></td>
        <td id="LC984" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L985" class="blob-num js-line-number" data-line-number="985"></td>
        <td id="LC985" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)),</td>
      </tr>
      <tr>
        <td id="L986" class="blob-num js-line-number" data-line-number="986"></td>
        <td id="LC986" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L987" class="blob-num js-line-number" data-line-number="987"></td>
        <td id="LC987" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L988" class="blob-num js-line-number" data-line-number="988"></td>
        <td id="LC988" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L989" class="blob-num js-line-number" data-line-number="989"></td>
        <td id="LC989" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L990" class="blob-num js-line-number" data-line-number="990"></td>
        <td id="LC990" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L991" class="blob-num js-line-number" data-line-number="991"></td>
        <td id="LC991" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#CPW is now centered, so connector A is just given by the coordinates</span></td>
      </tr>
      <tr>
        <td id="L992" class="blob-num js-line-number" data-line-number="992"></td>
        <td id="LC992" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L993" class="blob-num js-line-number" data-line-number="993"></td>
        <td id="LC993" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L994" class="blob-num js-line-number" data-line-number="994"></td>
        <td id="LC994" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L995" class="blob-num js-line-number" data-line-number="995"></td>
        <td id="LC995" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L996" class="blob-num js-line-number" data-line-number="996"></td>
        <td id="LC996" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L997" class="blob-num js-line-number" data-line-number="997"></td>
        <td id="LC997" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Make the Cell</span></td>
      </tr>
      <tr>
        <td id="L998" class="blob-num js-line-number" data-line-number="998"></td>
        <td id="LC998" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L999" class="blob-num js-line-number" data-line-number="999"></td>
        <td id="LC999" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1000" class="blob-num js-line-number" data-line-number="1000"></td>
        <td id="LC1000" class="blob-code blob-code-inner js-file-line">  <span class="pl-c">#      if bridges:</span></td>
      </tr>
      <tr>
        <td id="L1001" class="blob-num js-line-number" data-line-number="1001"></td>
        <td id="LC1001" class="blob-code blob-code-inner js-file-line">  <span class="pl-c">#          self.addBridges()</span></td>
      </tr>
      <tr>
        <td id="L1002" class="blob-num js-line-number" data-line-number="1002"></td>
        <td id="LC1002" class="blob-code blob-code-inner js-file-line">  <span class="pl-c">#          sampleX.topCell.add(self.ABCellr)</span></td>
      </tr>
      <tr>
        <td id="L1003" class="blob-num js-line-number" data-line-number="1003"></td>
        <td id="LC1003" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add the CPW cell to the TopCell</span></td>
      </tr>
      <tr>
        <td id="L1004" class="blob-num js-line-number" data-line-number="1004"></td>
        <td id="LC1004" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1005" class="blob-num js-line-number" data-line-number="1005"></td>
        <td id="LC1005" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1006" class="blob-num js-line-number" data-line-number="1006"></td>
        <td id="LC1006" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1007" class="blob-num js-line-number" data-line-number="1007"></td>
        <td id="LC1007" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1008" class="blob-num js-line-number" data-line-number="1008"></td>
        <td id="LC1008" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        make the cad Cell reference of the CPW</span></td>
      </tr>
      <tr>
        <td id="L1009" class="blob-num js-line-number" data-line-number="1009"></td>
        <td id="LC1009" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1010" class="blob-num js-line-number" data-line-number="1010"></td>
        <td id="LC1010" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>drawing a CPW of <span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">1e6</span>, <span class="pl-s"><span class="pl-pds">&#39;</span> mm long<span class="pl-pds">&#39;</span></span> </td>
      </tr>
      <tr>
        <td id="L1011" class="blob-num js-line-number" data-line-number="1011"></td>
        <td id="LC1011" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.CPW(<span class="pl-v">self</span>.coords,<span class="pl-v">self</span>.leng, <span class="pl-smi">center</span><span class="pl-k">=</span>sampleX.a1,</td>
      </tr>
      <tr>
        <td id="L1012" class="blob-num js-line-number" data-line-number="1012"></td>
        <td id="LC1012" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">gap</span><span class="pl-k">=</span>sampleX.a1<span class="pl-k">*</span>sampleX.abr, <span class="pl-smi">closeA</span> <span class="pl-k">=</span></td>
      </tr>
      <tr>
        <td id="L1013" class="blob-num js-line-number" data-line-number="1013"></td>
        <td id="LC1013" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.closeA, <span class="pl-smi">closeB</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.closeB, <span class="pl-smi">bridges</span><span class="pl-k">=</span><span class="pl-v">self</span>.bridges, </td>
      </tr>
      <tr>
        <td id="L1014" class="blob-num js-line-number" data-line-number="1014"></td>
        <td id="LC1014" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">bridgeDistance</span><span class="pl-k">=</span> <span class="pl-v">self</span>.bridgeDistance, </td>
      </tr>
      <tr>
        <td id="L1015" class="blob-num js-line-number" data-line-number="1015"></td>
        <td id="LC1015" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">bridgeStart</span><span class="pl-k">=</span><span class="pl-v">self</span>.bridgeStart, <span class="pl-smi">bridgeEnd</span><span class="pl-k">=</span><span class="pl-v">self</span>.bridgeEnd,<span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-v">self</span>.rot)</td>
      </tr>
      <tr>
        <td id="L1016" class="blob-num js-line-number" data-line-number="1016"></td>
        <td id="LC1016" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L1017" class="blob-num js-line-number" data-line-number="1017"></td>
        <td id="LC1017" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#    def addBridges(self):</span></td>
      </tr>
      <tr>
        <td id="L1018" class="blob-num js-line-number" data-line-number="1018"></td>
        <td id="LC1018" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L1019" class="blob-num js-line-number" data-line-number="1019"></td>
        <td id="LC1019" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        #Cell for bridges</span></td>
      </tr>
      <tr>
        <td id="L1020" class="blob-num js-line-number" data-line-number="1020"></td>
        <td id="LC1020" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        bridgeCell = cad.core.Cell(&#39;AB&#39;)</span></td>
      </tr>
      <tr>
        <td id="L1021" class="blob-num js-line-number" data-line-number="1021"></td>
        <td id="LC1021" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        xloc = self.bridgeDistance/2.</span></td>
      </tr>
      <tr>
        <td id="L1022" class="blob-num js-line-number" data-line-number="1022"></td>
        <td id="LC1022" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        </span></td>
      </tr>
      <tr>
        <td id="L1023" class="blob-num js-line-number" data-line-number="1023"></td>
        <td id="LC1023" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        #Generate airbridges symmetrically around 0</span></td>
      </tr>
      <tr>
        <td id="L1024" class="blob-num js-line-number" data-line-number="1024"></td>
        <td id="LC1024" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        while xloc &lt; self.leng/2:</span></td>
      </tr>
      <tr>
        <td id="L1025" class="blob-num js-line-number" data-line-number="1025"></td>
        <td id="LC1025" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#            if xloc &lt; self.leng/2. - self.bridgeEnd:</span></td>
      </tr>
      <tr>
        <td id="L1026" class="blob-num js-line-number" data-line-number="1026"></td>
        <td id="LC1026" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#                ab1 = md.airBridge((xloc,0), rot=90)</span></td>
      </tr>
      <tr>
        <td id="L1027" class="blob-num js-line-number" data-line-number="1027"></td>
        <td id="LC1027" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#                bridgeCell.add(ab1)</span></td>
      </tr>
      <tr>
        <td id="L1028" class="blob-num js-line-number" data-line-number="1028"></td>
        <td id="LC1028" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#            if -xloc &gt; -self.leng/2. + self.bridgeStart:</span></td>
      </tr>
      <tr>
        <td id="L1029" class="blob-num js-line-number" data-line-number="1029"></td>
        <td id="LC1029" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#                ab2 = md.airBridge((-xloc,0), rot=90)</span></td>
      </tr>
      <tr>
        <td id="L1030" class="blob-num js-line-number" data-line-number="1030"></td>
        <td id="LC1030" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#                bridgeCell.add(ab2)</span></td>
      </tr>
      <tr>
        <td id="L1031" class="blob-num js-line-number" data-line-number="1031"></td>
        <td id="LC1031" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#            xloc = xloc + self.bridgeDistance</span></td>
      </tr>
      <tr>
        <td id="L1032" class="blob-num js-line-number" data-line-number="1032"></td>
        <td id="LC1032" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L1033" class="blob-num js-line-number" data-line-number="1033"></td>
        <td id="LC1033" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        self.ABCellr = cad.core.CellReference(bridgeCell, rotation=self.rot)</span></td>
      </tr>
      <tr>
        <td id="L1034" class="blob-num js-line-number" data-line-number="1034"></td>
        <td id="LC1034" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#        self.ABCellr.translate(self.coords)</span></td>
      </tr>
      <tr>
        <td id="L1035" class="blob-num js-line-number" data-line-number="1035"></td>
        <td id="LC1035" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L1036" class="blob-num js-line-number" data-line-number="1036"></td>
        <td id="LC1036" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Arc</span>:</td>
      </tr>
      <tr>
        <td id="L1037" class="blob-num js-line-number" data-line-number="1037"></td>
        <td id="LC1037" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1038" class="blob-num js-line-number" data-line-number="1038"></td>
        <td id="LC1038" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">initAngle</span>, <span class="pl-smi">degrees</span>, <span class="pl-smi">placeInfo</span>,<span class="pl-smi">flip</span>, <span class="pl-smi">rbend</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1039" class="blob-num js-line-number" data-line-number="1039"></td>
        <td id="LC1039" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1040" class="blob-num js-line-number" data-line-number="1040"></td>
        <td id="LC1040" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Construct an Arc</span></td>
      </tr>
      <tr>
        <td id="L1041" class="blob-num js-line-number" data-line-number="1041"></td>
        <td id="LC1041" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1042" class="blob-num js-line-number" data-line-number="1042"></td>
        <td id="LC1042" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1043" class="blob-num js-line-number" data-line-number="1043"></td>
        <td id="LC1043" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#attributes</span></td>
      </tr>
      <tr>
        <td id="L1044" class="blob-num js-line-number" data-line-number="1044"></td>
        <td id="LC1044" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.initAngle <span class="pl-k">=</span> initAngle</td>
      </tr>
      <tr>
        <td id="L1045" class="blob-num js-line-number" data-line-number="1045"></td>
        <td id="LC1045" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.degrees <span class="pl-k">=</span> degrees</td>
      </tr>
      <tr>
        <td id="L1046" class="blob-num js-line-number" data-line-number="1046"></td>
        <td id="LC1046" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rbend <span class="pl-k">=</span> rbend</td>
      </tr>
      <tr>
        <td id="L1047" class="blob-num js-line-number" data-line-number="1047"></td>
        <td id="LC1047" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1048" class="blob-num js-line-number" data-line-number="1048"></td>
        <td id="LC1048" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1049" class="blob-num js-line-number" data-line-number="1049"></td>
        <td id="LC1049" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1050" class="blob-num js-line-number" data-line-number="1050"></td>
        <td id="LC1050" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1051" class="blob-num js-line-number" data-line-number="1051"></td>
        <td id="LC1051" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1052" class="blob-num js-line-number" data-line-number="1052"></td>
        <td id="LC1052" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1053" class="blob-num js-line-number" data-line-number="1053"></td>
        <td id="LC1053" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1054" class="blob-num js-line-number" data-line-number="1054"></td>
        <td id="LC1054" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for the size of the component</span></td>
      </tr>
      <tr>
        <td id="L1055" class="blob-num js-line-number" data-line-number="1055"></td>
        <td id="LC1055" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> flip:</td>
      </tr>
      <tr>
        <td id="L1056" class="blob-num js-line-number" data-line-number="1056"></td>
        <td id="LC1056" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1057" class="blob-num js-line-number" data-line-number="1057"></td>
        <td id="LC1057" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>(np.cos(rad(<span class="pl-v">self</span>.initAngle<span class="pl-k">+</span>degrees<span class="pl-k">+</span><span class="pl-v">self</span>.rot))),</td>
      </tr>
      <tr>
        <td id="L1058" class="blob-num js-line-number" data-line-number="1058"></td>
        <td id="LC1058" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1059" class="blob-num js-line-number" data-line-number="1059"></td>
        <td id="LC1059" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.initAngle<span class="pl-k">+</span>degrees<span class="pl-k">+</span><span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1060" class="blob-num js-line-number" data-line-number="1060"></td>
        <td id="LC1060" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1061" class="blob-num js-line-number" data-line-number="1061"></td>
        <td id="LC1061" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1062" class="blob-num js-line-number" data-line-number="1062"></td>
        <td id="LC1062" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>(np.cos(rad(<span class="pl-v">self</span>.initAngle<span class="pl-k">+</span><span class="pl-v">self</span>.rot))),</td>
      </tr>
      <tr>
        <td id="L1063" class="blob-num js-line-number" data-line-number="1063"></td>
        <td id="LC1063" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.initAngle<span class="pl-k">+</span><span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1064" class="blob-num js-line-number" data-line-number="1064"></td>
        <td id="LC1064" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1065" class="blob-num js-line-number" data-line-number="1065"></td>
        <td id="LC1065" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1066" class="blob-num js-line-number" data-line-number="1066"></td>
        <td id="LC1066" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (placeInfo[<span class="pl-c1">0</span>] <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1067" class="blob-num js-line-number" data-line-number="1067"></td>
        <td id="LC1067" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>(np.cos(<span class="pl-v">self</span>.initAngle<span class="pl-k">+</span><span class="pl-v">self</span>.rot)),</td>
      </tr>
      <tr>
        <td id="L1068" class="blob-num js-line-number" data-line-number="1068"></td>
        <td id="LC1068" class="blob-code blob-code-inner js-file-line">                placeInfo[<span class="pl-c1">1</span>] <span class="pl-k">-</span> np.cos(<span class="pl-v">self</span>.initAngle<span class="pl-k">+</span><span class="pl-v">self</span>.rot))</td>
      </tr>
      <tr>
        <td id="L1069" class="blob-num js-line-number" data-line-number="1069"></td>
        <td id="LC1069" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1070" class="blob-num js-line-number" data-line-number="1070"></td>
        <td id="LC1070" class="blob-code blob-code-inner js-file-line">        dxA <span class="pl-k">=</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.cos(rad(initAngle<span class="pl-k">+</span><span class="pl-v">self</span>.rot)) </td>
      </tr>
      <tr>
        <td id="L1071" class="blob-num js-line-number" data-line-number="1071"></td>
        <td id="LC1071" class="blob-code blob-code-inner js-file-line">        dxB <span class="pl-k">=</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.cos(rad(initAngle<span class="pl-k">+</span>degrees<span class="pl-k">+</span><span class="pl-v">self</span>.rot))</td>
      </tr>
      <tr>
        <td id="L1072" class="blob-num js-line-number" data-line-number="1072"></td>
        <td id="LC1072" class="blob-code blob-code-inner js-file-line">        dyA <span class="pl-k">=</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(initAngle<span class="pl-k">+</span><span class="pl-v">self</span>.rot))</td>
      </tr>
      <tr>
        <td id="L1073" class="blob-num js-line-number" data-line-number="1073"></td>
        <td id="LC1073" class="blob-code blob-code-inner js-file-line">        dyB <span class="pl-k">=</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(initAngle<span class="pl-k">+</span>degrees<span class="pl-k">+</span><span class="pl-v">self</span>.rot)) </td>
      </tr>
      <tr>
        <td id="L1074" class="blob-num js-line-number" data-line-number="1074"></td>
        <td id="LC1074" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L1075" class="blob-num js-line-number" data-line-number="1075"></td>
        <td id="LC1075" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Connector locations</span></td>
      </tr>
      <tr>
        <td id="L1076" class="blob-num js-line-number" data-line-number="1076"></td>
        <td id="LC1076" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> flip:</td>
      </tr>
      <tr>
        <td id="L1077" class="blob-num js-line-number" data-line-number="1077"></td>
        <td id="LC1077" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> dxA, <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> dyA)</td>
      </tr>
      <tr>
        <td id="L1078" class="blob-num js-line-number" data-line-number="1078"></td>
        <td id="LC1078" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> dxB, <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> dyB)</td>
      </tr>
      <tr>
        <td id="L1079" class="blob-num js-line-number" data-line-number="1079"></td>
        <td id="LC1079" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1080" class="blob-num js-line-number" data-line-number="1080"></td>
        <td id="LC1080" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> dxA, <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> dyA)</td>
      </tr>
      <tr>
        <td id="L1081" class="blob-num js-line-number" data-line-number="1081"></td>
        <td id="LC1081" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> dxB, <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> dyB)</td>
      </tr>
      <tr>
        <td id="L1082" class="blob-num js-line-number" data-line-number="1082"></td>
        <td id="LC1082" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1083" class="blob-num js-line-number" data-line-number="1083"></td>
        <td id="LC1083" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#make the cell</span></td>
      </tr>
      <tr>
        <td id="L1084" class="blob-num js-line-number" data-line-number="1084"></td>
        <td id="LC1084" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L1085" class="blob-num js-line-number" data-line-number="1085"></td>
        <td id="LC1085" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1086" class="blob-num js-line-number" data-line-number="1086"></td>
        <td id="LC1086" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1087" class="blob-num js-line-number" data-line-number="1087"></td>
        <td id="LC1087" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>,<span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1088" class="blob-num js-line-number" data-line-number="1088"></td>
        <td id="LC1088" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1089" class="blob-num js-line-number" data-line-number="1089"></td>
        <td id="LC1089" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        make the cad Cell reference of the CPW</span></td>
      </tr>
      <tr>
        <td id="L1090" class="blob-num js-line-number" data-line-number="1090"></td>
        <td id="LC1090" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1091" class="blob-num js-line-number" data-line-number="1091"></td>
        <td id="LC1091" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.CPWArc(<span class="pl-v">self</span>.coords, <span class="pl-v">self</span>.initAngle, <span class="pl-v">self</span>.degrees,</td>
      </tr>
      <tr>
        <td id="L1092" class="blob-num js-line-number" data-line-number="1092"></td>
        <td id="LC1092" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">radius</span><span class="pl-k">=</span><span class="pl-v">self</span>.rbend, <span class="pl-smi">rot</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.rot, <span class="pl-smi">center</span><span class="pl-k">=</span>sampleX.a1, <span class="pl-smi">gap</span><span class="pl-k">=</span>sampleX.b1)</td>
      </tr>
      <tr>
        <td id="L1093" class="blob-num js-line-number" data-line-number="1093"></td>
        <td id="LC1093" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add the cell to the TopCell</span></td>
      </tr>
      <tr>
        <td id="L1094" class="blob-num js-line-number" data-line-number="1094"></td>
        <td id="LC1094" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1095" class="blob-num js-line-number" data-line-number="1095"></td>
        <td id="LC1095" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1096" class="blob-num js-line-number" data-line-number="1096"></td>
        <td id="LC1096" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1097" class="blob-num js-line-number" data-line-number="1097"></td>
        <td id="LC1097" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">DoubleArc</span>:</td>
      </tr>
      <tr>
        <td id="L1098" class="blob-num js-line-number" data-line-number="1098"></td>
        <td id="LC1098" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1099" class="blob-num js-line-number" data-line-number="1099"></td>
        <td id="LC1099" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">dy</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">rbend</span>, <span class="pl-smi">flip</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1100" class="blob-num js-line-number" data-line-number="1100"></td>
        <td id="LC1100" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1101" class="blob-num js-line-number" data-line-number="1101"></td>
        <td id="LC1101" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.dy <span class="pl-k">=</span> dy</td>
      </tr>
      <tr>
        <td id="L1102" class="blob-num js-line-number" data-line-number="1102"></td>
        <td id="LC1102" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1103" class="blob-num js-line-number" data-line-number="1103"></td>
        <td id="LC1103" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rbend <span class="pl-k">=</span> rbend</td>
      </tr>
      <tr>
        <td id="L1104" class="blob-num js-line-number" data-line-number="1104"></td>
        <td id="LC1104" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1105" class="blob-num js-line-number" data-line-number="1105"></td>
        <td id="LC1105" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Calculate angle</span></td>
      </tr>
      <tr>
        <td id="L1106" class="blob-num js-line-number" data-line-number="1106"></td>
        <td id="LC1106" class="blob-code blob-code-inner js-file-line">        phirad <span class="pl-k">=</span> np.arccos(<span class="pl-c1">1</span><span class="pl-k">-</span><span class="pl-c1">abs</span>(dy)<span class="pl-k">/</span>(rbend<span class="pl-k">*</span><span class="pl-c1">2</span>))</td>
      </tr>
      <tr>
        <td id="L1107" class="blob-num js-line-number" data-line-number="1107"></td>
        <td id="LC1107" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.xspan <span class="pl-k">=</span> <span class="pl-c1">2</span><span class="pl-k">*</span>rbend<span class="pl-k">*</span>np.sin(phirad)</td>
      </tr>
      <tr>
        <td id="L1108" class="blob-num js-line-number" data-line-number="1108"></td>
        <td id="LC1108" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1109" class="blob-num js-line-number" data-line-number="1109"></td>
        <td id="LC1109" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1110" class="blob-num js-line-number" data-line-number="1110"></td>
        <td id="LC1110" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1111" class="blob-num js-line-number" data-line-number="1111"></td>
        <td id="LC1111" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1112" class="blob-num js-line-number" data-line-number="1112"></td>
        <td id="LC1112" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1113" class="blob-num js-line-number" data-line-number="1113"></td>
        <td id="LC1113" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1114" class="blob-num js-line-number" data-line-number="1114"></td>
        <td id="LC1114" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for the size of the component</span></td>
      </tr>
      <tr>
        <td id="L1115" class="blob-num js-line-number" data-line-number="1115"></td>
        <td id="LC1115" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> flip:</td>
      </tr>
      <tr>
        <td id="L1116" class="blob-num js-line-number" data-line-number="1116"></td>
        <td id="LC1116" class="blob-code blob-code-inner js-file-line">                 <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.dy<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1117" class="blob-num js-line-number" data-line-number="1117"></td>
        <td id="LC1117" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)), <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1118" class="blob-num js-line-number" data-line-number="1118"></td>
        <td id="LC1118" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span> <span class="pl-v">self</span>.dy<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1119" class="blob-num js-line-number" data-line-number="1119"></td>
        <td id="LC1119" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1120" class="blob-num js-line-number" data-line-number="1120"></td>
        <td id="LC1120" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.dy<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1121" class="blob-num js-line-number" data-line-number="1121"></td>
        <td id="LC1121" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1122" class="blob-num js-line-number" data-line-number="1122"></td>
        <td id="LC1122" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.dy<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1123" class="blob-num js-line-number" data-line-number="1123"></td>
        <td id="LC1123" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1124" class="blob-num js-line-number" data-line-number="1124"></td>
        <td id="LC1124" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1125" class="blob-num js-line-number" data-line-number="1125"></td>
        <td id="LC1125" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1126" class="blob-num js-line-number" data-line-number="1126"></td>
        <td id="LC1126" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1127" class="blob-num js-line-number" data-line-number="1127"></td>
        <td id="LC1127" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Define Connectors</span></td>
      </tr>
      <tr>
        <td id="L1128" class="blob-num js-line-number" data-line-number="1128"></td>
        <td id="LC1128" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.dy<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1129" class="blob-num js-line-number" data-line-number="1129"></td>
        <td id="LC1129" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)), <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1130" class="blob-num js-line-number" data-line-number="1130"></td>
        <td id="LC1130" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span> <span class="pl-v">self</span>.dy<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1131" class="blob-num js-line-number" data-line-number="1131"></td>
        <td id="LC1131" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.dy<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1132" class="blob-num js-line-number" data-line-number="1132"></td>
        <td id="LC1132" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)), <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1133" class="blob-num js-line-number" data-line-number="1133"></td>
        <td id="LC1133" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.dy<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1134" class="blob-num js-line-number" data-line-number="1134"></td>
        <td id="LC1134" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1135" class="blob-num js-line-number" data-line-number="1135"></td>
        <td id="LC1135" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L1136" class="blob-num js-line-number" data-line-number="1136"></td>
        <td id="LC1136" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1137" class="blob-num js-line-number" data-line-number="1137"></td>
        <td id="LC1137" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1138" class="blob-num js-line-number" data-line-number="1138"></td>
        <td id="LC1138" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1139" class="blob-num js-line-number" data-line-number="1139"></td>
        <td id="LC1139" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell, b <span class="pl-k">=</span> md.doubleArc(<span class="pl-v">self</span>.coords, <span class="pl-v">self</span>.dy, <span class="pl-smi">rot</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.rot,</td>
      </tr>
      <tr>
        <td id="L1140" class="blob-num js-line-number" data-line-number="1140"></td>
        <td id="LC1140" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">rbend</span><span class="pl-k">=</span><span class="pl-v">self</span>.rbend, <span class="pl-smi">center</span><span class="pl-k">=</span>sampleX.a1, <span class="pl-smi">gap</span><span class="pl-k">=</span>sampleX.b1)</td>
      </tr>
      <tr>
        <td id="L1141" class="blob-num js-line-number" data-line-number="1141"></td>
        <td id="LC1141" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1142" class="blob-num js-line-number" data-line-number="1142"></td>
        <td id="LC1142" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1143" class="blob-num js-line-number" data-line-number="1143"></td>
        <td id="LC1143" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">SLine</span>:</td>
      </tr>
      <tr>
        <td id="L1144" class="blob-num js-line-number" data-line-number="1144"></td>
        <td id="LC1144" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1145" class="blob-num js-line-number" data-line-number="1145"></td>
        <td id="LC1145" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">yspan</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">rbend</span>, <span class="pl-smi">reflect</span>, <span class="pl-smi">flip</span>, <span class="pl-smi">enter</span>,</td>
      </tr>
      <tr>
        <td id="L1146" class="blob-num js-line-number" data-line-number="1146"></td>
        <td id="LC1146" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">exit</span>, <span class="pl-smi">bridges</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1147" class="blob-num js-line-number" data-line-number="1147"></td>
        <td id="LC1147" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1148" class="blob-num js-line-number" data-line-number="1148"></td>
        <td id="LC1148" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Construct an Sline </span></td>
      </tr>
      <tr>
        <td id="L1149" class="blob-num js-line-number" data-line-number="1149"></td>
        <td id="LC1149" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1150" class="blob-num js-line-number" data-line-number="1150"></td>
        <td id="LC1150" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1151" class="blob-num js-line-number" data-line-number="1151"></td>
        <td id="LC1151" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>drawing an S-shape Line<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1152" class="blob-num js-line-number" data-line-number="1152"></td>
        <td id="LC1152" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1153" class="blob-num js-line-number" data-line-number="1153"></td>
        <td id="LC1153" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#attributes</span></td>
      </tr>
      <tr>
        <td id="L1154" class="blob-num js-line-number" data-line-number="1154"></td>
        <td id="LC1154" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.yspan <span class="pl-k">=</span> yspan</td>
      </tr>
      <tr>
        <td id="L1155" class="blob-num js-line-number" data-line-number="1155"></td>
        <td id="LC1155" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rbend <span class="pl-k">=</span> rbend</td>
      </tr>
      <tr>
        <td id="L1156" class="blob-num js-line-number" data-line-number="1156"></td>
        <td id="LC1156" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.flip <span class="pl-k">=</span> flip</td>
      </tr>
      <tr>
        <td id="L1157" class="blob-num js-line-number" data-line-number="1157"></td>
        <td id="LC1157" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.reflect <span class="pl-k">=</span> reflect</td>
      </tr>
      <tr>
        <td id="L1158" class="blob-num js-line-number" data-line-number="1158"></td>
        <td id="LC1158" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1159" class="blob-num js-line-number" data-line-number="1159"></td>
        <td id="LC1159" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.enter <span class="pl-k">=</span> enter</td>
      </tr>
      <tr>
        <td id="L1160" class="blob-num js-line-number" data-line-number="1160"></td>
        <td id="LC1160" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridges <span class="pl-k">=</span> bridges</td>
      </tr>
      <tr>
        <td id="L1161" class="blob-num js-line-number" data-line-number="1161"></td>
        <td id="LC1161" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.exit <span class="pl-k">=</span> exit</td>
      </tr>
      <tr>
        <td id="L1162" class="blob-num js-line-number" data-line-number="1162"></td>
        <td id="LC1162" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1163" class="blob-num js-line-number" data-line-number="1163"></td>
        <td id="LC1163" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1164" class="blob-num js-line-number" data-line-number="1164"></td>
        <td id="LC1164" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1165" class="blob-num js-line-number" data-line-number="1165"></td>
        <td id="LC1165" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1166" class="blob-num js-line-number" data-line-number="1166"></td>
        <td id="LC1166" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1167" class="blob-num js-line-number" data-line-number="1167"></td>
        <td id="LC1167" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1168" class="blob-num js-line-number" data-line-number="1168"></td>
        <td id="LC1168" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for the size of the component</span></td>
      </tr>
      <tr>
        <td id="L1169" class="blob-num js-line-number" data-line-number="1169"></td>
        <td id="LC1169" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> flip:</td>
      </tr>
      <tr>
        <td id="L1170" class="blob-num js-line-number" data-line-number="1170"></td>
        <td id="LC1170" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> reflect:</td>
      </tr>
      <tr>
        <td id="L1171" class="blob-num js-line-number" data-line-number="1171"></td>
        <td id="LC1171" class="blob-code blob-code-inner js-file-line">                     <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1172" class="blob-num js-line-number" data-line-number="1172"></td>
        <td id="LC1172" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)), <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1173" class="blob-num js-line-number" data-line-number="1173"></td>
        <td id="LC1173" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span><span class="pl-v">self</span>.exit<span class="pl-k">*</span><span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1174" class="blob-num js-line-number" data-line-number="1174"></td>
        <td id="LC1174" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1175" class="blob-num js-line-number" data-line-number="1175"></td>
        <td id="LC1175" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1176" class="blob-num js-line-number" data-line-number="1176"></td>
        <td id="LC1176" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)), <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1177" class="blob-num js-line-number" data-line-number="1177"></td>
        <td id="LC1177" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.enter<span class="pl-k">*</span><span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1178" class="blob-num js-line-number" data-line-number="1178"></td>
        <td id="LC1178" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1179" class="blob-num js-line-number" data-line-number="1179"></td>
        <td id="LC1179" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> reflect:</td>
      </tr>
      <tr>
        <td id="L1180" class="blob-num js-line-number" data-line-number="1180"></td>
        <td id="LC1180" class="blob-code blob-code-inner js-file-line">                     <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1181" class="blob-num js-line-number" data-line-number="1181"></td>
        <td id="LC1181" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)), <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1182" class="blob-num js-line-number" data-line-number="1182"></td>
        <td id="LC1182" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span><span class="pl-v">self</span>.exit<span class="pl-k">*</span><span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1183" class="blob-num js-line-number" data-line-number="1183"></td>
        <td id="LC1183" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1184" class="blob-num js-line-number" data-line-number="1184"></td>
        <td id="LC1184" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1185" class="blob-num js-line-number" data-line-number="1185"></td>
        <td id="LC1185" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)), <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1186" class="blob-num js-line-number" data-line-number="1186"></td>
        <td id="LC1186" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span> <span class="pl-v">self</span>.enter<span class="pl-k">*</span><span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1187" class="blob-num js-line-number" data-line-number="1187"></td>
        <td id="LC1187" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1188" class="blob-num js-line-number" data-line-number="1188"></td>
        <td id="LC1188" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1189" class="blob-num js-line-number" data-line-number="1189"></td>
        <td id="LC1189" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1190" class="blob-num js-line-number" data-line-number="1190"></td>
        <td id="LC1190" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1191" class="blob-num js-line-number" data-line-number="1191"></td>
        <td id="LC1191" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Connector locations</span></td>
      </tr>
      <tr>
        <td id="L1192" class="blob-num js-line-number" data-line-number="1192"></td>
        <td id="LC1192" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.reflect:</td>
      </tr>
      <tr>
        <td id="L1193" class="blob-num js-line-number" data-line-number="1193"></td>
        <td id="LC1193" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1194" class="blob-num js-line-number" data-line-number="1194"></td>
        <td id="LC1194" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)), <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1195" class="blob-num js-line-number" data-line-number="1195"></td>
        <td id="LC1195" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.exit<span class="pl-k">*</span><span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1196" class="blob-num js-line-number" data-line-number="1196"></td>
        <td id="LC1196" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1197" class="blob-num js-line-number" data-line-number="1197"></td>
        <td id="LC1197" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)), <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1198" class="blob-num js-line-number" data-line-number="1198"></td>
        <td id="LC1198" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span> <span class="pl-v">self</span>.enter<span class="pl-k">*</span><span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1199" class="blob-num js-line-number" data-line-number="1199"></td>
        <td id="LC1199" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1200" class="blob-num js-line-number" data-line-number="1200"></td>
        <td id="LC1200" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1201" class="blob-num js-line-number" data-line-number="1201"></td>
        <td id="LC1201" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)), <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1202" class="blob-num js-line-number" data-line-number="1202"></td>
        <td id="LC1202" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.exit<span class="pl-k">*</span><span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1203" class="blob-num js-line-number" data-line-number="1203"></td>
        <td id="LC1203" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L1204" class="blob-num js-line-number" data-line-number="1204"></td>
        <td id="LC1204" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)), <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span></td>
      </tr>
      <tr>
        <td id="L1205" class="blob-num js-line-number" data-line-number="1205"></td>
        <td id="LC1205" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)) <span class="pl-k">-</span> <span class="pl-v">self</span>.enter<span class="pl-k">*</span><span class="pl-v">self</span>.rbend<span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L1206" class="blob-num js-line-number" data-line-number="1206"></td>
        <td id="LC1206" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1207" class="blob-num js-line-number" data-line-number="1207"></td>
        <td id="LC1207" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1208" class="blob-num js-line-number" data-line-number="1208"></td>
        <td id="LC1208" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#make the cell</span></td>
      </tr>
      <tr>
        <td id="L1209" class="blob-num js-line-number" data-line-number="1209"></td>
        <td id="LC1209" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L1210" class="blob-num js-line-number" data-line-number="1210"></td>
        <td id="LC1210" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1211" class="blob-num js-line-number" data-line-number="1211"></td>
        <td id="LC1211" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>,<span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1212" class="blob-num js-line-number" data-line-number="1212"></td>
        <td id="LC1212" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1213" class="blob-num js-line-number" data-line-number="1213"></td>
        <td id="LC1213" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        make the cad Cell reference of the CPW</span></td>
      </tr>
      <tr>
        <td id="L1214" class="blob-num js-line-number" data-line-number="1214"></td>
        <td id="LC1214" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1215" class="blob-num js-line-number" data-line-number="1215"></td>
        <td id="LC1215" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.sLine(<span class="pl-v">self</span>.coords, <span class="pl-v">self</span>.yspan, <span class="pl-smi">rbend</span><span class="pl-k">=</span><span class="pl-v">self</span>.rbend,</td>
      </tr>
      <tr>
        <td id="L1216" class="blob-num js-line-number" data-line-number="1216"></td>
        <td id="LC1216" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">reflect</span><span class="pl-k">=</span><span class="pl-v">self</span>.reflect, <span class="pl-smi">enter</span><span class="pl-k">=</span><span class="pl-v">self</span>.enter, <span class="pl-smi">exit</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.exit,</td>
      </tr>
      <tr>
        <td id="L1217" class="blob-num js-line-number" data-line-number="1217"></td>
        <td id="LC1217" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">bridges</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.bridges, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-v">self</span>.rot, <span class="pl-smi">center</span><span class="pl-k">=</span>sampleX.a1, <span class="pl-smi">gap</span><span class="pl-k">=</span>sampleX.b1)</td>
      </tr>
      <tr>
        <td id="L1218" class="blob-num js-line-number" data-line-number="1218"></td>
        <td id="LC1218" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add the cell to the TopCell</span></td>
      </tr>
      <tr>
        <td id="L1219" class="blob-num js-line-number" data-line-number="1219"></td>
        <td id="LC1219" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1220" class="blob-num js-line-number" data-line-number="1220"></td>
        <td id="LC1220" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1221" class="blob-num js-line-number" data-line-number="1221"></td>
        <td id="LC1221" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">JLine</span>:</td>
      </tr>
      <tr>
        <td id="L1222" class="blob-num js-line-number" data-line-number="1222"></td>
        <td id="LC1222" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1223" class="blob-num js-line-number" data-line-number="1223"></td>
        <td id="LC1223" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">totLen</span>, <span class="pl-smi">xspan</span>, <span class="pl-smi">yspan</span>, <span class="pl-smi">nWiggles</span>, <span class="pl-smi">placeInfo</span>,</td>
      </tr>
      <tr>
        <td id="L1224" class="blob-num js-line-number" data-line-number="1224"></td>
        <td id="LC1224" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">offsets</span>, <span class="pl-smi">rbend</span>, <span class="pl-smi">bridges</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1225" class="blob-num js-line-number" data-line-number="1225"></td>
        <td id="LC1225" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1226" class="blob-num js-line-number" data-line-number="1226"></td>
        <td id="LC1226" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Construct a Jline </span></td>
      </tr>
      <tr>
        <td id="L1227" class="blob-num js-line-number" data-line-number="1227"></td>
        <td id="LC1227" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1228" class="blob-num js-line-number" data-line-number="1228"></td>
        <td id="LC1228" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L1229" class="blob-num js-line-number" data-line-number="1229"></td>
        <td id="LC1229" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>drawing a J-shape Line<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1230" class="blob-num js-line-number" data-line-number="1230"></td>
        <td id="LC1230" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1231" class="blob-num js-line-number" data-line-number="1231"></td>
        <td id="LC1231" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#attributes</span></td>
      </tr>
      <tr>
        <td id="L1232" class="blob-num js-line-number" data-line-number="1232"></td>
        <td id="LC1232" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.totLen <span class="pl-k">=</span> totLen</td>
      </tr>
      <tr>
        <td id="L1233" class="blob-num js-line-number" data-line-number="1233"></td>
        <td id="LC1233" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.xspan <span class="pl-k">=</span> xspan</td>
      </tr>
      <tr>
        <td id="L1234" class="blob-num js-line-number" data-line-number="1234"></td>
        <td id="LC1234" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.yspan <span class="pl-k">=</span> yspan</td>
      </tr>
      <tr>
        <td id="L1235" class="blob-num js-line-number" data-line-number="1235"></td>
        <td id="LC1235" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rbend <span class="pl-k">=</span> rbend</td>
      </tr>
      <tr>
        <td id="L1236" class="blob-num js-line-number" data-line-number="1236"></td>
        <td id="LC1236" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.nWiggles <span class="pl-k">=</span> nWiggles</td>
      </tr>
      <tr>
        <td id="L1237" class="blob-num js-line-number" data-line-number="1237"></td>
        <td id="LC1237" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.offsets <span class="pl-k">=</span> offsets</td>
      </tr>
      <tr>
        <td id="L1238" class="blob-num js-line-number" data-line-number="1238"></td>
        <td id="LC1238" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridges <span class="pl-k">=</span> bridges</td>
      </tr>
      <tr>
        <td id="L1239" class="blob-num js-line-number" data-line-number="1239"></td>
        <td id="LC1239" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1240" class="blob-num js-line-number" data-line-number="1240"></td>
        <td id="LC1240" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1241" class="blob-num js-line-number" data-line-number="1241"></td>
        <td id="LC1241" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1242" class="blob-num js-line-number" data-line-number="1242"></td>
        <td id="LC1242" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1243" class="blob-num js-line-number" data-line-number="1243"></td>
        <td id="LC1243" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1244" class="blob-num js-line-number" data-line-number="1244"></td>
        <td id="LC1244" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1245" class="blob-num js-line-number" data-line-number="1245"></td>
        <td id="LC1245" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1246" class="blob-num js-line-number" data-line-number="1246"></td>
        <td id="LC1246" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Apply offsets</span></td>
      </tr>
      <tr>
        <td id="L1247" class="blob-num js-line-number" data-line-number="1247"></td>
        <td id="LC1247" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>]<span class="pl-k">+</span><span class="pl-v">self</span>.offsets[<span class="pl-c1">0</span>],</td>
      </tr>
      <tr>
        <td id="L1248" class="blob-num js-line-number" data-line-number="1248"></td>
        <td id="LC1248" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>]<span class="pl-k">+</span><span class="pl-v">self</span>.offsets[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1249" class="blob-num js-line-number" data-line-number="1249"></td>
        <td id="LC1249" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1250" class="blob-num js-line-number" data-line-number="1250"></td>
        <td id="LC1250" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1251" class="blob-num js-line-number" data-line-number="1251"></td>
        <td id="LC1251" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1252" class="blob-num js-line-number" data-line-number="1252"></td>
        <td id="LC1252" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1253" class="blob-num js-line-number" data-line-number="1253"></td>
        <td id="LC1253" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Make the Cell</span></td>
      </tr>
      <tr>
        <td id="L1254" class="blob-num js-line-number" data-line-number="1254"></td>
        <td id="LC1254" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L1255" class="blob-num js-line-number" data-line-number="1255"></td>
        <td id="LC1255" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1256" class="blob-num js-line-number" data-line-number="1256"></td>
        <td id="LC1256" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add airbridges</span></td>
      </tr>
      <tr>
        <td id="L1257" class="blob-num js-line-number" data-line-number="1257"></td>
        <td id="LC1257" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> bridges:</td>
      </tr>
      <tr>
        <td id="L1258" class="blob-num js-line-number" data-line-number="1258"></td>
        <td id="LC1258" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.addBridges()</td>
      </tr>
      <tr>
        <td id="L1259" class="blob-num js-line-number" data-line-number="1259"></td>
        <td id="LC1259" class="blob-code blob-code-inner js-file-line">            sampleX.topCell.add(<span class="pl-v">self</span>.abCellr)</td>
      </tr>
      <tr>
        <td id="L1260" class="blob-num js-line-number" data-line-number="1260"></td>
        <td id="LC1260" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1261" class="blob-num js-line-number" data-line-number="1261"></td>
        <td id="LC1261" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add cell to total</span></td>
      </tr>
      <tr>
        <td id="L1262" class="blob-num js-line-number" data-line-number="1262"></td>
        <td id="LC1262" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1263" class="blob-num js-line-number" data-line-number="1263"></td>
        <td id="LC1263" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1264" class="blob-num js-line-number" data-line-number="1264"></td>
        <td id="LC1264" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1265" class="blob-num js-line-number" data-line-number="1265"></td>
        <td id="LC1265" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1266" class="blob-num js-line-number" data-line-number="1266"></td>
        <td id="LC1266" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell, <span class="pl-v">self</span>.wigyspan <span class="pl-k">=</span> md.jLine(<span class="pl-v">self</span>.coords, <span class="pl-v">self</span>.totLen, <span class="pl-v">self</span>.xspan, <span class="pl-v">self</span>.yspan,</td>
      </tr>
      <tr>
        <td id="L1267" class="blob-num js-line-number" data-line-number="1267"></td>
        <td id="LC1267" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.nWiggles, <span class="pl-smi">rbend</span><span class="pl-k">=</span><span class="pl-v">self</span>.rbend, <span class="pl-smi">rot</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.rot, <span class="pl-smi">center</span><span class="pl-k">=</span>sampleX.a1, <span class="pl-smi">gap</span><span class="pl-k">=</span>sampleX.b1)</td>
      </tr>
      <tr>
        <td id="L1268" class="blob-num js-line-number" data-line-number="1268"></td>
        <td id="LC1268" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1269" class="blob-num js-line-number" data-line-number="1269"></td>
        <td id="LC1269" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addBridges</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L1270" class="blob-num js-line-number" data-line-number="1270"></td>
        <td id="LC1270" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1271" class="blob-num js-line-number" data-line-number="1271"></td>
        <td id="LC1271" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        add airbridges, by default 2 symmetrically around the center</span></td>
      </tr>
      <tr>
        <td id="L1272" class="blob-num js-line-number" data-line-number="1272"></td>
        <td id="LC1272" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1273" class="blob-num js-line-number" data-line-number="1273"></td>
        <td id="LC1273" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1274" class="blob-num js-line-number" data-line-number="1274"></td>
        <td id="LC1274" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1275" class="blob-num js-line-number" data-line-number="1275"></td>
        <td id="LC1275" class="blob-code blob-code-inner js-file-line">        wigOffset <span class="pl-k">=</span> <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2</span> <span class="pl-k">-</span> (<span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.nWiggles<span class="pl-k">-</span><span class="pl-c1">2</span>)<span class="pl-k">*</span><span class="pl-v">self</span>.rbend <span class="pl-k">-</span> <span class="pl-v">self</span>.rbend<span class="pl-k">/</span><span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L1276" class="blob-num js-line-number" data-line-number="1276"></td>
        <td id="LC1276" class="blob-code blob-code-inner js-file-line">        abYOffset <span class="pl-k">=</span> <span class="pl-k">-</span> <span class="pl-v">self</span>.yspan<span class="pl-k">/</span><span class="pl-c1">2</span> <span class="pl-k">+</span> wigOffset </td>
      </tr>
      <tr>
        <td id="L1277" class="blob-num js-line-number" data-line-number="1277"></td>
        <td id="LC1277" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1278" class="blob-num js-line-number" data-line-number="1278"></td>
        <td id="LC1278" class="blob-code blob-code-inner js-file-line">        abCell <span class="pl-k">=</span> cad.core.Cell(<span class="pl-s"><span class="pl-pds">&#39;</span>AB<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1279" class="blob-num js-line-number" data-line-number="1279"></td>
        <td id="LC1279" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.nWiggles<span class="pl-k">%</span><span class="pl-c1">2</span> <span class="pl-k">==</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L1280" class="blob-num js-line-number" data-line-number="1280"></td>
        <td id="LC1280" class="blob-code blob-code-inner js-file-line">            ab1 <span class="pl-k">=</span> md.airBridge((<span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2</span> <span class="pl-k">-</span><span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.wigyspan <span class="pl-k">+</span> <span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.rbend,</td>
      </tr>
      <tr>
        <td id="L1281" class="blob-num js-line-number" data-line-number="1281"></td>
        <td id="LC1281" class="blob-code blob-code-inner js-file-line">                abYOffset <span class="pl-k">-</span> <span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.rbend))</td>
      </tr>
      <tr>
        <td id="L1282" class="blob-num js-line-number" data-line-number="1282"></td>
        <td id="LC1282" class="blob-code blob-code-inner js-file-line">            ab2 <span class="pl-k">=</span> md.airBridge((<span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2</span> <span class="pl-k">-</span> <span class="pl-c1">2</span><span class="pl-k">*</span> <span class="pl-v">self</span>.wigyspan <span class="pl-k">+</span><span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.rbend,</td>
      </tr>
      <tr>
        <td id="L1283" class="blob-num js-line-number" data-line-number="1283"></td>
        <td id="LC1283" class="blob-code blob-code-inner js-file-line">                abYOffset <span class="pl-k">+</span> <span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.rbend))</td>
      </tr>
      <tr>
        <td id="L1284" class="blob-num js-line-number" data-line-number="1284"></td>
        <td id="LC1284" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>: </td>
      </tr>
      <tr>
        <td id="L1285" class="blob-num js-line-number" data-line-number="1285"></td>
        <td id="LC1285" class="blob-code blob-code-inner js-file-line">            ab1 <span class="pl-k">=</span> md.airBridge((<span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2</span> <span class="pl-k">+</span><span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.rbend <span class="pl-k">-</span> <span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.wigyspan, </td>
      </tr>
      <tr>
        <td id="L1286" class="blob-num js-line-number" data-line-number="1286"></td>
        <td id="LC1286" class="blob-code blob-code-inner js-file-line">                abYOffset <span class="pl-k">-</span> <span class="pl-v">self</span>.rbend))</td>
      </tr>
      <tr>
        <td id="L1287" class="blob-num js-line-number" data-line-number="1287"></td>
        <td id="LC1287" class="blob-code blob-code-inner js-file-line">            ab2 <span class="pl-k">=</span> md.airBridge((<span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2</span> <span class="pl-k">+</span><span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.rbend,</td>
      </tr>
      <tr>
        <td id="L1288" class="blob-num js-line-number" data-line-number="1288"></td>
        <td id="LC1288" class="blob-code blob-code-inner js-file-line">                abYOffset <span class="pl-k">+</span> <span class="pl-v">self</span>.rbend))        </td>
      </tr>
      <tr>
        <td id="L1289" class="blob-num js-line-number" data-line-number="1289"></td>
        <td id="LC1289" class="blob-code blob-code-inner js-file-line">        abCell.add([ab1, ab2])</td>
      </tr>
      <tr>
        <td id="L1290" class="blob-num js-line-number" data-line-number="1290"></td>
        <td id="LC1290" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.abCellr <span class="pl-k">=</span> cad.core.CellReference(abCell, <span class="pl-smi">origin</span><span class="pl-k">=</span><span class="pl-v">self</span>.coords)</td>
      </tr>
      <tr>
        <td id="L1291" class="blob-num js-line-number" data-line-number="1291"></td>
        <td id="LC1291" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.abCellr.rotate(<span class="pl-v">self</span>.rot)</td>
      </tr>
      <tr>
        <td id="L1292" class="blob-num js-line-number" data-line-number="1292"></td>
        <td id="LC1292" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1293" class="blob-num js-line-number" data-line-number="1293"></td>
        <td id="LC1293" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1294" class="blob-num js-line-number" data-line-number="1294"></td>
        <td id="LC1294" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Wiggle</span>:</td>
      </tr>
      <tr>
        <td id="L1295" class="blob-num js-line-number" data-line-number="1295"></td>
        <td id="LC1295" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L1296" class="blob-num js-line-number" data-line-number="1296"></td>
        <td id="LC1296" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">nWiggles</span>, <span class="pl-smi">leng</span>, <span class="pl-smi">xspan</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">xOffset</span>,</td>
      </tr>
      <tr>
        <td id="L1297" class="blob-num js-line-number" data-line-number="1297"></td>
        <td id="LC1297" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">yOffset</span>, <span class="pl-smi">skew</span>, <span class="pl-smi">rbend</span>, <span class="pl-smi">bridges</span>, <span class="pl-smi">closeA</span>, <span class="pl-smi">closeB</span>, <span class="pl-smi">flip</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1298" class="blob-num js-line-number" data-line-number="1298"></td>
        <td id="LC1298" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1299" class="blob-num js-line-number" data-line-number="1299"></td>
        <td id="LC1299" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Construct a Wiggles</span></td>
      </tr>
      <tr>
        <td id="L1300" class="blob-num js-line-number" data-line-number="1300"></td>
        <td id="LC1300" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1301" class="blob-num js-line-number" data-line-number="1301"></td>
        <td id="LC1301" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1302" class="blob-num js-line-number" data-line-number="1302"></td>
        <td id="LC1302" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#attributes</span></td>
      </tr>
      <tr>
        <td id="L1303" class="blob-num js-line-number" data-line-number="1303"></td>
        <td id="LC1303" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.nWiggles <span class="pl-k">=</span> nWiggles</td>
      </tr>
      <tr>
        <td id="L1304" class="blob-num js-line-number" data-line-number="1304"></td>
        <td id="LC1304" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.leng <span class="pl-k">=</span> leng</td>
      </tr>
      <tr>
        <td id="L1305" class="blob-num js-line-number" data-line-number="1305"></td>
        <td id="LC1305" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.xspan <span class="pl-k">=</span> xspan</td>
      </tr>
      <tr>
        <td id="L1306" class="blob-num js-line-number" data-line-number="1306"></td>
        <td id="LC1306" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.xOffset <span class="pl-k">=</span> xOffset</td>
      </tr>
      <tr>
        <td id="L1307" class="blob-num js-line-number" data-line-number="1307"></td>
        <td id="LC1307" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.yOffset <span class="pl-k">=</span> yOffset</td>
      </tr>
      <tr>
        <td id="L1308" class="blob-num js-line-number" data-line-number="1308"></td>
        <td id="LC1308" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rbend <span class="pl-k">=</span> rbend</td>
      </tr>
      <tr>
        <td id="L1309" class="blob-num js-line-number" data-line-number="1309"></td>
        <td id="LC1309" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridges <span class="pl-k">=</span> bridges</td>
      </tr>
      <tr>
        <td id="L1310" class="blob-num js-line-number" data-line-number="1310"></td>
        <td id="LC1310" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.skew <span class="pl-k">=</span> skew</td>
      </tr>
      <tr>
        <td id="L1311" class="blob-num js-line-number" data-line-number="1311"></td>
        <td id="LC1311" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.closeA <span class="pl-k">=</span> closeA</td>
      </tr>
      <tr>
        <td id="L1312" class="blob-num js-line-number" data-line-number="1312"></td>
        <td id="LC1312" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.closeB <span class="pl-k">=</span> closeB</td>
      </tr>
      <tr>
        <td id="L1313" class="blob-num js-line-number" data-line-number="1313"></td>
        <td id="LC1313" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1314" class="blob-num js-line-number" data-line-number="1314"></td>
        <td id="LC1314" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1315" class="blob-num js-line-number" data-line-number="1315"></td>
        <td id="LC1315" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1316" class="blob-num js-line-number" data-line-number="1316"></td>
        <td id="LC1316" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1317" class="blob-num js-line-number" data-line-number="1317"></td>
        <td id="LC1317" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1318" class="blob-num js-line-number" data-line-number="1318"></td>
        <td id="LC1318" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1319" class="blob-num js-line-number" data-line-number="1319"></td>
        <td id="LC1319" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1320" class="blob-num js-line-number" data-line-number="1320"></td>
        <td id="LC1320" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for the size of the component</span></td>
      </tr>
      <tr>
        <td id="L1321" class="blob-num js-line-number" data-line-number="1321"></td>
        <td id="LC1321" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> flip:</td>
      </tr>
      <tr>
        <td id="L1322" class="blob-num js-line-number" data-line-number="1322"></td>
        <td id="LC1322" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.skew<span class="pl-k">*</span>np.sin(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1323" class="blob-num js-line-number" data-line-number="1323"></td>
        <td id="LC1323" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)) <span class="pl-k">-</span> <span class="pl-v">self</span>.skew<span class="pl-k">*</span>np.cos(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1324" class="blob-num js-line-number" data-line-number="1324"></td>
        <td id="LC1324" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1325" class="blob-num js-line-number" data-line-number="1325"></td>
        <td id="LC1325" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span> <span class="pl-v">self</span>.skew<span class="pl-k">*</span>np.sin(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1326" class="blob-num js-line-number" data-line-number="1326"></td>
        <td id="LC1326" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.skew<span class="pl-k">*</span>np.cos(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1327" class="blob-num js-line-number" data-line-number="1327"></td>
        <td id="LC1327" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1328" class="blob-num js-line-number" data-line-number="1328"></td>
        <td id="LC1328" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1329" class="blob-num js-line-number" data-line-number="1329"></td>
        <td id="LC1329" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1330" class="blob-num js-line-number" data-line-number="1330"></td>
        <td id="LC1330" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1331" class="blob-num js-line-number" data-line-number="1331"></td>
        <td id="LC1331" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1332" class="blob-num js-line-number" data-line-number="1332"></td>
        <td id="LC1332" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Connector locations</span></td>
      </tr>
      <tr>
        <td id="L1333" class="blob-num js-line-number" data-line-number="1333"></td>
        <td id="LC1333" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> flip:</td>
      </tr>
      <tr>
        <td id="L1334" class="blob-num js-line-number" data-line-number="1334"></td>
        <td id="LC1334" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1335" class="blob-num js-line-number" data-line-number="1335"></td>
        <td id="LC1335" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.skew<span class="pl-k">*</span>np.cos(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1336" class="blob-num js-line-number" data-line-number="1336"></td>
        <td id="LC1336" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1337" class="blob-num js-line-number" data-line-number="1337"></td>
        <td id="LC1337" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)) <span class="pl-k">-</span> <span class="pl-v">self</span>.skew<span class="pl-k">*</span>np.cos(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1338" class="blob-num js-line-number" data-line-number="1338"></td>
        <td id="LC1338" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1339" class="blob-num js-line-number" data-line-number="1339"></td>
        <td id="LC1339" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1340" class="blob-num js-line-number" data-line-number="1340"></td>
        <td id="LC1340" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)) <span class="pl-k">-</span> <span class="pl-v">self</span>.skew<span class="pl-k">*</span>np.cos(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1341" class="blob-num js-line-number" data-line-number="1341"></td>
        <td id="LC1341" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1342" class="blob-num js-line-number" data-line-number="1342"></td>
        <td id="LC1342" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.xspan<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.skew<span class="pl-k">*</span>np.cos(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1343" class="blob-num js-line-number" data-line-number="1343"></td>
        <td id="LC1343" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1344" class="blob-num js-line-number" data-line-number="1344"></td>
        <td id="LC1344" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#make the cell</span></td>
      </tr>
      <tr>
        <td id="L1345" class="blob-num js-line-number" data-line-number="1345"></td>
        <td id="LC1345" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L1346" class="blob-num js-line-number" data-line-number="1346"></td>
        <td id="LC1346" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1347" class="blob-num js-line-number" data-line-number="1347"></td>
        <td id="LC1347" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> bridges <span class="pl-k">!=</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L1348" class="blob-num js-line-number" data-line-number="1348"></td>
        <td id="LC1348" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.addBridges(sampleX)</td>
      </tr>
      <tr>
        <td id="L1349" class="blob-num js-line-number" data-line-number="1349"></td>
        <td id="LC1349" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1350" class="blob-num js-line-number" data-line-number="1350"></td>
        <td id="LC1350" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#add Wigglecell to topCell</span></td>
      </tr>
      <tr>
        <td id="L1351" class="blob-num js-line-number" data-line-number="1351"></td>
        <td id="LC1351" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cellr)</td>
      </tr>
      <tr>
        <td id="L1352" class="blob-num js-line-number" data-line-number="1352"></td>
        <td id="LC1352" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1353" class="blob-num js-line-number" data-line-number="1353"></td>
        <td id="LC1353" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1354" class="blob-num js-line-number" data-line-number="1354"></td>
        <td id="LC1354" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1355" class="blob-num js-line-number" data-line-number="1355"></td>
        <td id="LC1355" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1356" class="blob-num js-line-number" data-line-number="1356"></td>
        <td id="LC1356" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#construct object</span></td>
      </tr>
      <tr>
        <td id="L1357" class="blob-num js-line-number" data-line-number="1357"></td>
        <td id="LC1357" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cellr, <span class="pl-v">self</span>.yspan <span class="pl-k">=</span> md.nWiggle(<span class="pl-v">self</span>.coords, <span class="pl-v">self</span>.leng, <span class="pl-v">self</span>.xspan, </td>
      </tr>
      <tr>
        <td id="L1358" class="blob-num js-line-number" data-line-number="1358"></td>
        <td id="LC1358" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.nWiggles, <span class="pl-smi">xOffset</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.xOffset, </td>
      </tr>
      <tr>
        <td id="L1359" class="blob-num js-line-number" data-line-number="1359"></td>
        <td id="LC1359" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">yOffset</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.yOffset, <span class="pl-smi">skew</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.skew, <span class="pl-smi">closeA</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.closeA,</td>
      </tr>
      <tr>
        <td id="L1360" class="blob-num js-line-number" data-line-number="1360"></td>
        <td id="LC1360" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">closeB</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.closeB, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-v">self</span>.rot, <span class="pl-smi">center</span><span class="pl-k">=</span>sampleX.a1, <span class="pl-smi">gap</span><span class="pl-k">=</span>sampleX.b1)</td>
      </tr>
      <tr>
        <td id="L1361" class="blob-num js-line-number" data-line-number="1361"></td>
        <td id="LC1361" class="blob-code blob-code-inner js-file-line">   </td>
      </tr>
      <tr>
        <td id="L1362" class="blob-num js-line-number" data-line-number="1362"></td>
        <td id="LC1362" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1363" class="blob-num js-line-number" data-line-number="1363"></td>
        <td id="LC1363" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addBridges</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1364" class="blob-num js-line-number" data-line-number="1364"></td>
        <td id="LC1364" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1365" class="blob-num js-line-number" data-line-number="1365"></td>
        <td id="LC1365" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        add airbridges, by default 2 symmetrically around the center</span></td>
      </tr>
      <tr>
        <td id="L1366" class="blob-num js-line-number" data-line-number="1366"></td>
        <td id="LC1366" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1367" class="blob-num js-line-number" data-line-number="1367"></td>
        <td id="LC1367" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1368" class="blob-num js-line-number" data-line-number="1368"></td>
        <td id="LC1368" class="blob-code blob-code-inner js-file-line">        abCell <span class="pl-k">=</span> cad.core.Cell(<span class="pl-s"><span class="pl-pds">&#39;</span>AB<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1369" class="blob-num js-line-number" data-line-number="1369"></td>
        <td id="LC1369" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1370" class="blob-num js-line-number" data-line-number="1370"></td>
        <td id="LC1370" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#multiplier to get the wiggles at the right spot </span></td>
      </tr>
      <tr>
        <td id="L1371" class="blob-num js-line-number" data-line-number="1371"></td>
        <td id="LC1371" class="blob-code blob-code-inner js-file-line">        m <span class="pl-k">=</span> (<span class="pl-k">-</span><span class="pl-c1">1</span>)<span class="pl-k">**</span>(<span class="pl-v">self</span>.nWiggles<span class="pl-k">/</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1372" class="blob-num js-line-number" data-line-number="1372"></td>
        <td id="LC1372" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1373" class="blob-num js-line-number" data-line-number="1373"></td>
        <td id="LC1373" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Determine: single or multiple wiggles</span></td>
      </tr>
      <tr>
        <td id="L1374" class="blob-num js-line-number" data-line-number="1374"></td>
        <td id="LC1374" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.bridges <span class="pl-k">==</span> <span class="pl-c1">True</span>: <span class="pl-c">#just two bridges</span></td>
      </tr>
      <tr>
        <td id="L1375" class="blob-num js-line-number" data-line-number="1375"></td>
        <td id="LC1375" class="blob-code blob-code-inner js-file-line">            xlocs <span class="pl-k">=</span> [<span class="pl-v">self</span>.xOffset <span class="pl-k">-</span> (<span class="pl-c1">1</span><span class="pl-k">+</span>(<span class="pl-v">self</span>.nWiggles<span class="pl-k">%</span><span class="pl-c1">2</span><span class="pl-k">==</span><span class="pl-c1">1</span>))<span class="pl-k">*</span><span class="pl-v">self</span>.rbend,</td>
      </tr>
      <tr>
        <td id="L1376" class="blob-num js-line-number" data-line-number="1376"></td>
        <td id="LC1376" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.xOffset <span class="pl-k">+</span> (<span class="pl-c1">1</span><span class="pl-k">+</span>(<span class="pl-v">self</span>.nWiggles<span class="pl-k">%</span><span class="pl-c1">2</span><span class="pl-k">==</span><span class="pl-c1">1</span>))<span class="pl-k">*</span><span class="pl-v">self</span>.rbend]</td>
      </tr>
      <tr>
        <td id="L1377" class="blob-num js-line-number" data-line-number="1377"></td>
        <td id="LC1377" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.bridges <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>more<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1378" class="blob-num js-line-number" data-line-number="1378"></td>
        <td id="LC1378" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>more bridges<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1379" class="blob-num js-line-number" data-line-number="1379"></td>
        <td id="LC1379" class="blob-code blob-code-inner js-file-line">            nbridges <span class="pl-k">=</span> <span class="pl-v">self</span>.nWiggles<span class="pl-k">/</span><span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L1380" class="blob-num js-line-number" data-line-number="1380"></td>
        <td id="LC1380" class="blob-code blob-code-inner js-file-line">            wigDis <span class="pl-k">=</span> <span class="pl-c1">4</span><span class="pl-k">*</span><span class="pl-v">self</span>.rbend </td>
      </tr>
      <tr>
        <td id="L1381" class="blob-num js-line-number" data-line-number="1381"></td>
        <td id="LC1381" class="blob-code blob-code-inner js-file-line">            wigStart <span class="pl-k">=</span> (<span class="pl-c1">1</span><span class="pl-k">+</span>(<span class="pl-v">self</span>.nWiggles<span class="pl-k">%</span><span class="pl-c1">2</span><span class="pl-k">==</span><span class="pl-c1">1</span>))<span class="pl-k">*</span><span class="pl-v">self</span>.rbend </td>
      </tr>
      <tr>
        <td id="L1382" class="blob-num js-line-number" data-line-number="1382"></td>
        <td id="LC1382" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.nWiggles<span class="pl-k">%</span><span class="pl-c1">2</span><span class="pl-k">==</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L1383" class="blob-num js-line-number" data-line-number="1383"></td>
        <td id="LC1383" class="blob-code blob-code-inner js-file-line">                xlocs1 <span class="pl-k">=</span> np.arange(<span class="pl-v">self</span>.xOffset <span class="pl-k">-</span> wigStart, <span class="pl-v">self</span>.xOffset <span class="pl-k">-</span> wigDis<span class="pl-k">*</span>(nbridges<span class="pl-k">+</span><span class="pl-c1">1</span>)<span class="pl-k">/</span><span class="pl-c1">2</span>, <span class="pl-k">-</span>wigDis)</td>
      </tr>
      <tr>
        <td id="L1384" class="blob-num js-line-number" data-line-number="1384"></td>
        <td id="LC1384" class="blob-code blob-code-inner js-file-line">                xlocs2 <span class="pl-k">=</span> np.arange(<span class="pl-v">self</span>.xOffset <span class="pl-k">+</span> wigStart, <span class="pl-v">self</span>.xOffset <span class="pl-k">+</span> wigDis<span class="pl-k">*</span>(nbridges<span class="pl-k">+</span><span class="pl-c1">1</span>)<span class="pl-k">/</span><span class="pl-c1">2</span>, wigDis)</td>
      </tr>
      <tr>
        <td id="L1385" class="blob-num js-line-number" data-line-number="1385"></td>
        <td id="LC1385" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1386" class="blob-num js-line-number" data-line-number="1386"></td>
        <td id="LC1386" class="blob-code blob-code-inner js-file-line">                xlocs1 <span class="pl-k">=</span> np.arange(<span class="pl-v">self</span>.xOffset <span class="pl-k">-</span> wigStart, <span class="pl-v">self</span>.xOffset <span class="pl-k">-</span> wigDis<span class="pl-k">*</span>(nbridges)<span class="pl-k">/</span><span class="pl-c1">2</span>, <span class="pl-k">-</span>wigDis)</td>
      </tr>
      <tr>
        <td id="L1387" class="blob-num js-line-number" data-line-number="1387"></td>
        <td id="LC1387" class="blob-code blob-code-inner js-file-line">                xlocs2 <span class="pl-k">=</span> np.arange(<span class="pl-v">self</span>.xOffset <span class="pl-k">+</span> wigStart, <span class="pl-v">self</span>.xOffset <span class="pl-k">+</span> wigDis<span class="pl-k">*</span>(nbridges)<span class="pl-k">/</span><span class="pl-c1">2</span>, wigDis)</td>
      </tr>
      <tr>
        <td id="L1388" class="blob-num js-line-number" data-line-number="1388"></td>
        <td id="LC1388" class="blob-code blob-code-inner js-file-line">            xlocs <span class="pl-k">=</span> np.concatenate([xlocs1, xlocs2])</td>
      </tr>
      <tr>
        <td id="L1389" class="blob-num js-line-number" data-line-number="1389"></td>
        <td id="LC1389" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">print</span> xlocs</td>
      </tr>
      <tr>
        <td id="L1390" class="blob-num js-line-number" data-line-number="1390"></td>
        <td id="LC1390" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1391" class="blob-num js-line-number" data-line-number="1391"></td>
        <td id="LC1391" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Put the wiggles</span></td>
      </tr>
      <tr>
        <td id="L1392" class="blob-num js-line-number" data-line-number="1392"></td>
        <td id="LC1392" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> x <span class="pl-k">in</span> xlocs:</td>
      </tr>
      <tr>
        <td id="L1393" class="blob-num js-line-number" data-line-number="1393"></td>
        <td id="LC1393" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-v">self</span>.nWiggles<span class="pl-k">%</span><span class="pl-c1">2</span><span class="pl-k">==</span><span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1394" class="blob-num js-line-number" data-line-number="1394"></td>
        <td id="LC1394" class="blob-code blob-code-inner js-file-line">                    m <span class="pl-k">=</span> (<span class="pl-k">-</span><span class="pl-c1">1</span>)<span class="pl-k">**</span>(<span class="pl-v">self</span>.nWiggles<span class="pl-k">/</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1395" class="blob-num js-line-number" data-line-number="1395"></td>
        <td id="LC1395" class="blob-code blob-code-inner js-file-line">                    ab <span class="pl-k">=</span> md.airBridge((x, <span class="pl-v">self</span>.yOffset<span class="pl-k">-</span>np.sign(x)<span class="pl-k">*-</span>m<span class="pl-k">*</span><span class="pl-v">self</span>.yspan), <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">90</span>)</td>
      </tr>
      <tr>
        <td id="L1396" class="blob-num js-line-number" data-line-number="1396"></td>
        <td id="LC1396" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1397" class="blob-num js-line-number" data-line-number="1397"></td>
        <td id="LC1397" class="blob-code blob-code-inner js-file-line">                    m <span class="pl-k">=</span> (<span class="pl-k">-</span><span class="pl-c1">1</span>)<span class="pl-k">**</span>((<span class="pl-v">self</span>.nWiggles<span class="pl-k">+</span><span class="pl-c1">1</span>)<span class="pl-k">/</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1398" class="blob-num js-line-number" data-line-number="1398"></td>
        <td id="LC1398" class="blob-code blob-code-inner js-file-line">                    ab <span class="pl-k">=</span> md.airBridge((x, <span class="pl-v">self</span>.yOffset<span class="pl-k">+</span>m<span class="pl-k">*</span><span class="pl-v">self</span>.yspan), <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-c1">90</span>)</td>
      </tr>
      <tr>
        <td id="L1399" class="blob-num js-line-number" data-line-number="1399"></td>
        <td id="LC1399" class="blob-code blob-code-inner js-file-line">                abCell.add(ab)</td>
      </tr>
      <tr>
        <td id="L1400" class="blob-num js-line-number" data-line-number="1400"></td>
        <td id="LC1400" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1401" class="blob-num js-line-number" data-line-number="1401"></td>
        <td id="LC1401" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1402" class="blob-num js-line-number" data-line-number="1402"></td>
        <td id="LC1402" class="blob-code blob-code-inner js-file-line">        m <span class="pl-k">=</span> (<span class="pl-k">-</span><span class="pl-c1">1</span>)<span class="pl-k">**</span>(<span class="pl-v">self</span>.nWiggles<span class="pl-k">/</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1403" class="blob-num js-line-number" data-line-number="1403"></td>
        <td id="LC1403" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.bridges <span class="pl-k">==</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1404" class="blob-num js-line-number" data-line-number="1404"></td>
        <td id="LC1404" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.nWiggles<span class="pl-k">%</span><span class="pl-c1">2</span> <span class="pl-k">==</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L1405" class="blob-num js-line-number" data-line-number="1405"></td>
        <td id="LC1405" class="blob-code blob-code-inner js-file-line">                m <span class="pl-k">=</span> (<span class="pl-k">-</span><span class="pl-c1">1</span>)<span class="pl-k">**</span>((<span class="pl-v">self</span>.nWiggles<span class="pl-k">+</span><span class="pl-c1">1</span>)<span class="pl-k">/</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1406" class="blob-num js-line-number" data-line-number="1406"></td>
        <td id="LC1406" class="blob-code blob-code-inner js-file-line">                ab1 <span class="pl-k">=</span> md.airBridge((<span class="pl-v">self</span>.xOffset <span class="pl-k">-</span> <span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.rbend, <span class="pl-v">self</span>.yOffset <span class="pl-k">+</span> m<span class="pl-k">*</span><span class="pl-v">self</span>.yspan),</td>
      </tr>
      <tr>
        <td id="L1407" class="blob-num js-line-number" data-line-number="1407"></td>
        <td id="LC1407" class="blob-code blob-code-inner js-file-line">                        <span class="pl-smi">rot</span> <span class="pl-k">=</span> <span class="pl-c1">90</span>)</td>
      </tr>
      <tr>
        <td id="L1408" class="blob-num js-line-number" data-line-number="1408"></td>
        <td id="LC1408" class="blob-code blob-code-inner js-file-line">                ab2 <span class="pl-k">=</span> md.airBridge((<span class="pl-v">self</span>.xOffset <span class="pl-k">+</span> <span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.rbend, <span class="pl-v">self</span>.yOffset <span class="pl-k">+</span> m<span class="pl-k">*</span><span class="pl-v">self</span>.yspan),</td>
      </tr>
      <tr>
        <td id="L1409" class="blob-num js-line-number" data-line-number="1409"></td>
        <td id="LC1409" class="blob-code blob-code-inner js-file-line">                        <span class="pl-smi">rot</span> <span class="pl-k">=</span> <span class="pl-c1">90</span>)</td>
      </tr>
      <tr>
        <td id="L1410" class="blob-num js-line-number" data-line-number="1410"></td>
        <td id="LC1410" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>: </td>
      </tr>
      <tr>
        <td id="L1411" class="blob-num js-line-number" data-line-number="1411"></td>
        <td id="LC1411" class="blob-code blob-code-inner js-file-line">                ab1 <span class="pl-k">=</span> md.airBridge((<span class="pl-v">self</span>.xOffset <span class="pl-k">-</span> <span class="pl-v">self</span>.rbend, <span class="pl-v">self</span>.yOffset <span class="pl-k">-</span> m<span class="pl-k">*</span><span class="pl-v">self</span>.yspan),</td>
      </tr>
      <tr>
        <td id="L1412" class="blob-num js-line-number" data-line-number="1412"></td>
        <td id="LC1412" class="blob-code blob-code-inner js-file-line">                        <span class="pl-smi">rot</span> <span class="pl-k">=</span> <span class="pl-c1">90</span>)</td>
      </tr>
      <tr>
        <td id="L1413" class="blob-num js-line-number" data-line-number="1413"></td>
        <td id="LC1413" class="blob-code blob-code-inner js-file-line">                ab2 <span class="pl-k">=</span> md.airBridge((<span class="pl-v">self</span>.xOffset <span class="pl-k">+</span> <span class="pl-v">self</span>.rbend, <span class="pl-v">self</span>.yOffset <span class="pl-k">+</span> m<span class="pl-k">*</span><span class="pl-v">self</span>.yspan),</td>
      </tr>
      <tr>
        <td id="L1414" class="blob-num js-line-number" data-line-number="1414"></td>
        <td id="LC1414" class="blob-code blob-code-inner js-file-line">                        <span class="pl-smi">rot</span> <span class="pl-k">=</span> <span class="pl-c1">90</span>)</td>
      </tr>
      <tr>
        <td id="L1415" class="blob-num js-line-number" data-line-number="1415"></td>
        <td id="LC1415" class="blob-code blob-code-inner js-file-line">            abCell.add([ab1, ab2])</td>
      </tr>
      <tr>
        <td id="L1416" class="blob-num js-line-number" data-line-number="1416"></td>
        <td id="LC1416" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1417" class="blob-num js-line-number" data-line-number="1417"></td>
        <td id="LC1417" class="blob-code blob-code-inner js-file-line">        abCellr <span class="pl-k">=</span> cad.core.CellReference(abCell, <span class="pl-smi">origin</span><span class="pl-k">=</span><span class="pl-v">self</span>.coords)</td>
      </tr>
      <tr>
        <td id="L1418" class="blob-num js-line-number" data-line-number="1418"></td>
        <td id="LC1418" class="blob-code blob-code-inner js-file-line">        abCellr.rotate(<span class="pl-v">self</span>.rot)</td>
      </tr>
      <tr>
        <td id="L1419" class="blob-num js-line-number" data-line-number="1419"></td>
        <td id="LC1419" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(abCellr)</td>
      </tr>
      <tr>
        <td id="L1420" class="blob-num js-line-number" data-line-number="1420"></td>
        <td id="LC1420" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1421" class="blob-num js-line-number" data-line-number="1421"></td>
        <td id="LC1421" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1422" class="blob-num js-line-number" data-line-number="1422"></td>
        <td id="LC1422" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1423" class="blob-num js-line-number" data-line-number="1423"></td>
        <td id="LC1423" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">ChargeLine</span>:</td>
      </tr>
      <tr>
        <td id="L1424" class="blob-num js-line-number" data-line-number="1424"></td>
        <td id="LC1424" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1425" class="blob-num js-line-number" data-line-number="1425"></td>
        <td id="LC1425" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">placeInfoLaunch</span>, <span class="pl-smi">placeInfoTransmon</span>, <span class="pl-smi">gapLen</span>,</td>
      </tr>
      <tr>
        <td id="L1426" class="blob-num js-line-number" data-line-number="1426"></td>
        <td id="LC1426" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">extraLen</span>, <span class="pl-smi">chargeOffset</span>, <span class="pl-smi">endrot</span>, <span class="pl-smi">startrot</span>):</td>
      </tr>
      <tr>
        <td id="L1427" class="blob-num js-line-number" data-line-number="1427"></td>
        <td id="LC1427" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1428" class="blob-num js-line-number" data-line-number="1428"></td>
        <td id="LC1428" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1429" class="blob-num js-line-number" data-line-number="1429"></td>
        <td id="LC1429" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gapLen <span class="pl-k">=</span> gapLen</td>
      </tr>
      <tr>
        <td id="L1430" class="blob-num js-line-number" data-line-number="1430"></td>
        <td id="LC1430" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.extraLen <span class="pl-k">=</span> extraLen</td>
      </tr>
      <tr>
        <td id="L1431" class="blob-num js-line-number" data-line-number="1431"></td>
        <td id="LC1431" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.chargeOffset <span class="pl-k">=</span> chargeOffset</td>
      </tr>
      <tr>
        <td id="L1432" class="blob-num js-line-number" data-line-number="1432"></td>
        <td id="LC1432" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.endrot <span class="pl-k">=</span> endrot</td>
      </tr>
      <tr>
        <td id="L1433" class="blob-num js-line-number" data-line-number="1433"></td>
        <td id="LC1433" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1434" class="blob-num js-line-number" data-line-number="1434"></td>
        <td id="LC1434" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection: For the Launcher</span></td>
      </tr>
      <tr>
        <td id="L1435" class="blob-num js-line-number" data-line-number="1435"></td>
        <td id="LC1435" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfoLaunch) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1436" class="blob-num js-line-number" data-line-number="1436"></td>
        <td id="LC1436" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1437" class="blob-num js-line-number" data-line-number="1437"></td>
        <td id="LC1437" class="blob-code blob-code-inner js-file-line">            compL <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfoLaunch.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1438" class="blob-num js-line-number" data-line-number="1438"></td>
        <td id="LC1438" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Lcoords <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(compL, placeInfoLaunch.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1439" class="blob-num js-line-number" data-line-number="1439"></td>
        <td id="LC1439" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Lrot <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(compL, <span class="pl-s"><span class="pl-pds">&#39;</span>rot<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1440" class="blob-num js-line-number" data-line-number="1440"></td>
        <td id="LC1440" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1441" class="blob-num js-line-number" data-line-number="1441"></td>
        <td id="LC1441" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1442" class="blob-num js-line-number" data-line-number="1442"></td>
        <td id="LC1442" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Lcoords <span class="pl-k">=</span> placeInfoLaunch</td>
      </tr>
      <tr>
        <td id="L1443" class="blob-num js-line-number" data-line-number="1443"></td>
        <td id="LC1443" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Lrot <span class="pl-k">=</span> startrot</td>
      </tr>
      <tr>
        <td id="L1444" class="blob-num js-line-number" data-line-number="1444"></td>
        <td id="LC1444" class="blob-code blob-code-inner js-file-line">           </td>
      </tr>
      <tr>
        <td id="L1445" class="blob-num js-line-number" data-line-number="1445"></td>
        <td id="LC1445" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#First, Add a chargeLine End</span></td>
      </tr>
      <tr>
        <td id="L1446" class="blob-num js-line-number" data-line-number="1446"></td>
        <td id="LC1446" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.addChargeLineEnd(sampleX, placeInfoTransmon)</td>
      </tr>
      <tr>
        <td id="L1447" class="blob-num js-line-number" data-line-number="1447"></td>
        <td id="LC1447" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1448" class="blob-num js-line-number" data-line-number="1448"></td>
        <td id="LC1448" class="blob-code blob-code-inner js-file-line">        sampleX.route(placeInfoLaunch, <span class="pl-v">self</span>.gateEndConnect,</td>
      </tr>
      <tr>
        <td id="L1449" class="blob-num js-line-number" data-line-number="1449"></td>
        <td id="LC1449" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">endrot</span><span class="pl-k">=</span><span class="pl-v">self</span>.endrot, <span class="pl-smi">rot1</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.Lrot)</td>
      </tr>
      <tr>
        <td id="L1450" class="blob-num js-line-number" data-line-number="1450"></td>
        <td id="LC1450" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1451" class="blob-num js-line-number" data-line-number="1451"></td>
        <td id="LC1451" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1452" class="blob-num js-line-number" data-line-number="1452"></td>
        <td id="LC1452" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addChargeLineEnd</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">placeInfoTransmon</span>):</td>
      </tr>
      <tr>
        <td id="L1453" class="blob-num js-line-number" data-line-number="1453"></td>
        <td id="LC1453" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1454" class="blob-num js-line-number" data-line-number="1454"></td>
        <td id="LC1454" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a CPW + gap, as a chargeLine end.</span></td>
      </tr>
      <tr>
        <td id="L1455" class="blob-num js-line-number" data-line-number="1455"></td>
        <td id="LC1455" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Inputs:</span></td>
      </tr>
      <tr>
        <td id="L1456" class="blob-num js-line-number" data-line-number="1456"></td>
        <td id="LC1456" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            gapLen (taken from default values if not specified)</span></td>
      </tr>
      <tr>
        <td id="L1457" class="blob-num js-line-number" data-line-number="1457"></td>
        <td id="LC1457" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            chargeOffset (default zero, otherwise a tuple (x, y)</span></td>
      </tr>
      <tr>
        <td id="L1458" class="blob-num js-line-number" data-line-number="1458"></td>
        <td id="LC1458" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            rot: rotation: ignored if placeInfo is a string</span></td>
      </tr>
      <tr>
        <td id="L1459" class="blob-num js-line-number" data-line-number="1459"></td>
        <td id="LC1459" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1460" class="blob-num js-line-number" data-line-number="1460"></td>
        <td id="LC1460" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1461" class="blob-num js-line-number" data-line-number="1461"></td>
        <td id="LC1461" class="blob-code blob-code-inner js-file-line">        totLen <span class="pl-k">=</span> <span class="pl-v">self</span>.gapLen <span class="pl-k">+</span> <span class="pl-v">self</span>.extraLen</td>
      </tr>
      <tr>
        <td id="L1462" class="blob-num js-line-number" data-line-number="1462"></td>
        <td id="LC1462" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1463" class="blob-num js-line-number" data-line-number="1463"></td>
        <td id="LC1463" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1464" class="blob-num js-line-number" data-line-number="1464"></td>
        <td id="LC1464" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#PlaceInfo for the Transmon Box, compensated for the chargeLineEnd</span></td>
      </tr>
      <tr>
        <td id="L1465" class="blob-num js-line-number" data-line-number="1465"></td>
        <td id="LC1465" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfoTransmon) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1466" class="blob-num js-line-number" data-line-number="1466"></td>
        <td id="LC1466" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1467" class="blob-num js-line-number" data-line-number="1467"></td>
        <td id="LC1467" class="blob-code blob-code-inner js-file-line">            compT <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfoTransmon.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1468" class="blob-num js-line-number" data-line-number="1468"></td>
        <td id="LC1468" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Tcoords <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(compT, placeInfoTransmon.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1469" class="blob-num js-line-number" data-line-number="1469"></td>
        <td id="LC1469" class="blob-code blob-code-inner js-file-line">            Trot <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(compT, <span class="pl-s"><span class="pl-pds">&#39;</span>rot<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1470" class="blob-num js-line-number" data-line-number="1470"></td>
        <td id="LC1470" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1471" class="blob-num js-line-number" data-line-number="1471"></td>
        <td id="LC1471" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Endrot</span></td>
      </tr>
      <tr>
        <td id="L1472" class="blob-num js-line-number" data-line-number="1472"></td>
        <td id="LC1472" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.endrot <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>l<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1473" class="blob-num js-line-number" data-line-number="1473"></td>
        <td id="LC1473" class="blob-code blob-code-inner js-file-line">                GLErot <span class="pl-k">=</span> <span class="pl-v">self</span>.Lrot <span class="pl-k">+</span> <span class="pl-c1">90</span></td>
      </tr>
      <tr>
        <td id="L1474" class="blob-num js-line-number" data-line-number="1474"></td>
        <td id="LC1474" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-v">self</span>.endrot <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1475" class="blob-num js-line-number" data-line-number="1475"></td>
        <td id="LC1475" class="blob-code blob-code-inner js-file-line">                GLErot <span class="pl-k">=</span> <span class="pl-v">self</span>.Lrot <span class="pl-k">-</span> <span class="pl-c1">90</span></td>
      </tr>
      <tr>
        <td id="L1476" class="blob-num js-line-number" data-line-number="1476"></td>
        <td id="LC1476" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1477" class="blob-num js-line-number" data-line-number="1477"></td>
        <td id="LC1477" class="blob-code blob-code-inner js-file-line">                GLErot <span class="pl-k">=</span> <span class="pl-v">self</span>.Lrot</td>
      </tr>
      <tr>
        <td id="L1478" class="blob-num js-line-number" data-line-number="1478"></td>
        <td id="LC1478" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1479" class="blob-num js-line-number" data-line-number="1479"></td>
        <td id="LC1479" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.GLcoords <span class="pl-k">=</span> (<span class="pl-v">self</span>.Tcoords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.chargeOffset[<span class="pl-c1">0</span>]<span class="pl-k">-</span> np.cos(rad(GLErot))<span class="pl-k">*</span>totLen<span class="pl-k">/</span><span class="pl-c1">2</span>,</td>
      </tr>
      <tr>
        <td id="L1480" class="blob-num js-line-number" data-line-number="1480"></td>
        <td id="LC1480" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.Tcoords[<span class="pl-c1">1</span>]<span class="pl-k">-</span>totLen<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.sin(rad(GLErot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.chargeOffset[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1481" class="blob-num js-line-number" data-line-number="1481"></td>
        <td id="LC1481" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1482" class="blob-num js-line-number" data-line-number="1482"></td>
        <td id="LC1482" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1483" class="blob-num js-line-number" data-line-number="1483"></td>
        <td id="LC1483" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.GLcoords <span class="pl-k">=</span> placeInfoTransmon</td>
      </tr>
      <tr>
        <td id="L1484" class="blob-num js-line-number" data-line-number="1484"></td>
        <td id="LC1484" class="blob-code blob-code-inner js-file-line">            GLErot <span class="pl-k">=</span> <span class="pl-v">self</span>.Lrot</td>
      </tr>
      <tr>
        <td id="L1485" class="blob-num js-line-number" data-line-number="1485"></td>
        <td id="LC1485" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1486" class="blob-num js-line-number" data-line-number="1486"></td>
        <td id="LC1486" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#draw!</span></td>
      </tr>
      <tr>
        <td id="L1487" class="blob-num js-line-number" data-line-number="1487"></td>
        <td id="LC1487" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.chargeLineEnd(<span class="pl-v">self</span>.GLcoords, totLen, <span class="pl-v">self</span>.gapLen, <span class="pl-smi">rot</span><span class="pl-k">=</span>GLErot)</td>
      </tr>
      <tr>
        <td id="L1488" class="blob-num js-line-number" data-line-number="1488"></td>
        <td id="LC1488" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1489" class="blob-num js-line-number" data-line-number="1489"></td>
        <td id="LC1489" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Connector</span></td>
      </tr>
      <tr>
        <td id="L1490" class="blob-num js-line-number" data-line-number="1490"></td>
        <td id="LC1490" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gateEndConnect <span class="pl-k">=</span> (<span class="pl-v">self</span>.GLcoords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> np.cos(rad(GLErot))<span class="pl-k">*</span>(totLen<span class="pl-k">/</span><span class="pl-c1">2</span>),</td>
      </tr>
      <tr>
        <td id="L1491" class="blob-num js-line-number" data-line-number="1491"></td>
        <td id="LC1491" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.GLcoords[<span class="pl-c1">1</span>] <span class="pl-k">-</span>(totLen<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.sin(rad(GLErot)))</td>
      </tr>
      <tr>
        <td id="L1492" class="blob-num js-line-number" data-line-number="1492"></td>
        <td id="LC1492" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1493" class="blob-num js-line-number" data-line-number="1493"></td>
        <td id="LC1493" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1494" class="blob-num js-line-number" data-line-number="1494"></td>
        <td id="LC1494" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1495" class="blob-num js-line-number" data-line-number="1495"></td>
        <td id="LC1495" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">FluxLine</span>:</td>
      </tr>
      <tr>
        <td id="L1496" class="blob-num js-line-number" data-line-number="1496"></td>
        <td id="LC1496" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1497" class="blob-num js-line-number" data-line-number="1497"></td>
        <td id="LC1497" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">placeInfoLaunch</span>, <span class="pl-smi">placeInfoTransmon</span>, <span class="pl-smi">fluxGap</span>,</td>
      </tr>
      <tr>
        <td id="L1498" class="blob-num js-line-number" data-line-number="1498"></td>
        <td id="LC1498" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">extraLine</span>, <span class="pl-smi">fluxLen</span>, <span class="pl-smi">fluxOffset</span>, <span class="pl-smi">endrot</span>, <span class="pl-smi">startrot</span>):</td>
      </tr>
      <tr>
        <td id="L1499" class="blob-num js-line-number" data-line-number="1499"></td>
        <td id="LC1499" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1500" class="blob-num js-line-number" data-line-number="1500"></td>
        <td id="LC1500" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#init</span></td>
      </tr>
      <tr>
        <td id="L1501" class="blob-num js-line-number" data-line-number="1501"></td>
        <td id="LC1501" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fluxGap <span class="pl-k">=</span> fluxGap</td>
      </tr>
      <tr>
        <td id="L1502" class="blob-num js-line-number" data-line-number="1502"></td>
        <td id="LC1502" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.extraLine <span class="pl-k">=</span> extraLine</td>
      </tr>
      <tr>
        <td id="L1503" class="blob-num js-line-number" data-line-number="1503"></td>
        <td id="LC1503" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fluxLen <span class="pl-k">=</span> fluxLen</td>
      </tr>
      <tr>
        <td id="L1504" class="blob-num js-line-number" data-line-number="1504"></td>
        <td id="LC1504" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fluxOffset <span class="pl-k">=</span> fluxOffset</td>
      </tr>
      <tr>
        <td id="L1505" class="blob-num js-line-number" data-line-number="1505"></td>
        <td id="LC1505" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.endrot <span class="pl-k">=</span> endrot</td>
      </tr>
      <tr>
        <td id="L1506" class="blob-num js-line-number" data-line-number="1506"></td>
        <td id="LC1506" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1507" class="blob-num js-line-number" data-line-number="1507"></td>
        <td id="LC1507" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection: For the Launcher</span></td>
      </tr>
      <tr>
        <td id="L1508" class="blob-num js-line-number" data-line-number="1508"></td>
        <td id="LC1508" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfoLaunch) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1509" class="blob-num js-line-number" data-line-number="1509"></td>
        <td id="LC1509" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1510" class="blob-num js-line-number" data-line-number="1510"></td>
        <td id="LC1510" class="blob-code blob-code-inner js-file-line">            compL <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfoLaunch.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1511" class="blob-num js-line-number" data-line-number="1511"></td>
        <td id="LC1511" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Lcoords <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(compL, placeInfoLaunch.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1512" class="blob-num js-line-number" data-line-number="1512"></td>
        <td id="LC1512" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Lrot <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(compL, <span class="pl-s"><span class="pl-pds">&#39;</span>rot<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1513" class="blob-num js-line-number" data-line-number="1513"></td>
        <td id="LC1513" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1514" class="blob-num js-line-number" data-line-number="1514"></td>
        <td id="LC1514" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1515" class="blob-num js-line-number" data-line-number="1515"></td>
        <td id="LC1515" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Lcoords <span class="pl-k">=</span> placeInfoLaunch</td>
      </tr>
      <tr>
        <td id="L1516" class="blob-num js-line-number" data-line-number="1516"></td>
        <td id="LC1516" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Lrot <span class="pl-k">=</span> startrot</td>
      </tr>
      <tr>
        <td id="L1517" class="blob-num js-line-number" data-line-number="1517"></td>
        <td id="LC1517" class="blob-code blob-code-inner js-file-line">           </td>
      </tr>
      <tr>
        <td id="L1518" class="blob-num js-line-number" data-line-number="1518"></td>
        <td id="LC1518" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#First, Add a chargeLine End</span></td>
      </tr>
      <tr>
        <td id="L1519" class="blob-num js-line-number" data-line-number="1519"></td>
        <td id="LC1519" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.addFluxLineEnd(sampleX, placeInfoTransmon)</td>
      </tr>
      <tr>
        <td id="L1520" class="blob-num js-line-number" data-line-number="1520"></td>
        <td id="LC1520" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1521" class="blob-num js-line-number" data-line-number="1521"></td>
        <td id="LC1521" class="blob-code blob-code-inner js-file-line">        sampleX.route(placeInfoLaunch, <span class="pl-v">self</span>.fluxEndConnect, <span class="pl-smi">endrot</span> <span class="pl-k">=</span></td>
      </tr>
      <tr>
        <td id="L1522" class="blob-num js-line-number" data-line-number="1522"></td>
        <td id="LC1522" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.endrot, <span class="pl-smi">rot1</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.Lrot)</td>
      </tr>
      <tr>
        <td id="L1523" class="blob-num js-line-number" data-line-number="1523"></td>
        <td id="LC1523" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1524" class="blob-num js-line-number" data-line-number="1524"></td>
        <td id="LC1524" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addFluxLineEnd</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">placeInfoTransmon</span>):</td>
      </tr>
      <tr>
        <td id="L1525" class="blob-num js-line-number" data-line-number="1525"></td>
        <td id="LC1525" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1526" class="blob-num js-line-number" data-line-number="1526"></td>
        <td id="LC1526" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a CPW + gap, as a chargeLine end.</span></td>
      </tr>
      <tr>
        <td id="L1527" class="blob-num js-line-number" data-line-number="1527"></td>
        <td id="LC1527" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Inputs:</span></td>
      </tr>
      <tr>
        <td id="L1528" class="blob-num js-line-number" data-line-number="1528"></td>
        <td id="LC1528" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            gapLen (taken from default values if not specified)</span></td>
      </tr>
      <tr>
        <td id="L1529" class="blob-num js-line-number" data-line-number="1529"></td>
        <td id="LC1529" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            chargeOffset (default zero, otherwise a tuple (x, y)</span></td>
      </tr>
      <tr>
        <td id="L1530" class="blob-num js-line-number" data-line-number="1530"></td>
        <td id="LC1530" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            rot: rotation: ignored if placeInfo is a string</span></td>
      </tr>
      <tr>
        <td id="L1531" class="blob-num js-line-number" data-line-number="1531"></td>
        <td id="LC1531" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1532" class="blob-num js-line-number" data-line-number="1532"></td>
        <td id="LC1532" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1533" class="blob-num js-line-number" data-line-number="1533"></td>
        <td id="LC1533" class="blob-code blob-code-inner js-file-line">        totLen <span class="pl-k">=</span> <span class="pl-v">self</span>.fluxLen <span class="pl-k">+</span> <span class="pl-v">self</span>.extraLine</td>
      </tr>
      <tr>
        <td id="L1534" class="blob-num js-line-number" data-line-number="1534"></td>
        <td id="LC1534" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1535" class="blob-num js-line-number" data-line-number="1535"></td>
        <td id="LC1535" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1536" class="blob-num js-line-number" data-line-number="1536"></td>
        <td id="LC1536" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#PlaceInfo for the Transmon Box, compensated for the chargeLineEnd</span></td>
      </tr>
      <tr>
        <td id="L1537" class="blob-num js-line-number" data-line-number="1537"></td>
        <td id="LC1537" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfoTransmon) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1538" class="blob-num js-line-number" data-line-number="1538"></td>
        <td id="LC1538" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1539" class="blob-num js-line-number" data-line-number="1539"></td>
        <td id="LC1539" class="blob-code blob-code-inner js-file-line">            compT <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfoTransmon.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1540" class="blob-num js-line-number" data-line-number="1540"></td>
        <td id="LC1540" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.Tcoords <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(compT, placeInfoTransmon.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1541" class="blob-num js-line-number" data-line-number="1541"></td>
        <td id="LC1541" class="blob-code blob-code-inner js-file-line">            Trot <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(compT, <span class="pl-s"><span class="pl-pds">&#39;</span>rot<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1542" class="blob-num js-line-number" data-line-number="1542"></td>
        <td id="LC1542" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1543" class="blob-num js-line-number" data-line-number="1543"></td>
        <td id="LC1543" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Endrot</span></td>
      </tr>
      <tr>
        <td id="L1544" class="blob-num js-line-number" data-line-number="1544"></td>
        <td id="LC1544" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.endrot <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>l<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1545" class="blob-num js-line-number" data-line-number="1545"></td>
        <td id="LC1545" class="blob-code blob-code-inner js-file-line">                FLErot <span class="pl-k">=</span> <span class="pl-v">self</span>.Lrot <span class="pl-k">+</span> <span class="pl-c1">90</span></td>
      </tr>
      <tr>
        <td id="L1546" class="blob-num js-line-number" data-line-number="1546"></td>
        <td id="LC1546" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-v">self</span>.endrot <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1547" class="blob-num js-line-number" data-line-number="1547"></td>
        <td id="LC1547" class="blob-code blob-code-inner js-file-line">                FLErot <span class="pl-k">=</span> <span class="pl-v">self</span>.Lrot <span class="pl-k">-</span> <span class="pl-c1">90</span></td>
      </tr>
      <tr>
        <td id="L1548" class="blob-num js-line-number" data-line-number="1548"></td>
        <td id="LC1548" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1549" class="blob-num js-line-number" data-line-number="1549"></td>
        <td id="LC1549" class="blob-code blob-code-inner js-file-line">                FLErot <span class="pl-k">=</span> <span class="pl-v">self</span>.Lrot </td>
      </tr>
      <tr>
        <td id="L1550" class="blob-num js-line-number" data-line-number="1550"></td>
        <td id="LC1550" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1551" class="blob-num js-line-number" data-line-number="1551"></td>
        <td id="LC1551" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.FLcoords <span class="pl-k">=</span> (<span class="pl-v">self</span>.Tcoords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.fluxOffset[<span class="pl-c1">0</span>] <span class="pl-k">-</span> np.cos(rad(FLErot))<span class="pl-k">*</span>totLen<span class="pl-k">/</span><span class="pl-c1">2</span>,</td>
      </tr>
      <tr>
        <td id="L1552" class="blob-num js-line-number" data-line-number="1552"></td>
        <td id="LC1552" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.Tcoords[<span class="pl-c1">1</span>]<span class="pl-k">+</span><span class="pl-v">self</span>.fluxOffset[<span class="pl-c1">1</span>] <span class="pl-k">-</span> totLen<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.sin(rad(FLErot)))</td>
      </tr>
      <tr>
        <td id="L1553" class="blob-num js-line-number" data-line-number="1553"></td>
        <td id="LC1553" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1554" class="blob-num js-line-number" data-line-number="1554"></td>
        <td id="LC1554" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1555" class="blob-num js-line-number" data-line-number="1555"></td>
        <td id="LC1555" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.FLcoords <span class="pl-k">=</span> placeInfoTransmon</td>
      </tr>
      <tr>
        <td id="L1556" class="blob-num js-line-number" data-line-number="1556"></td>
        <td id="LC1556" class="blob-code blob-code-inner js-file-line">            FLErot <span class="pl-k">=</span> <span class="pl-v">self</span>.Lrot</td>
      </tr>
      <tr>
        <td id="L1557" class="blob-num js-line-number" data-line-number="1557"></td>
        <td id="LC1557" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1558" class="blob-num js-line-number" data-line-number="1558"></td>
        <td id="LC1558" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#draw!</span></td>
      </tr>
      <tr>
        <td id="L1559" class="blob-num js-line-number" data-line-number="1559"></td>
        <td id="LC1559" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.fluxLineEnd(<span class="pl-v">self</span>.FLcoords, totLen, <span class="pl-smi">fluxlen</span><span class="pl-k">=</span><span class="pl-v">self</span>.fluxLen,</td>
      </tr>
      <tr>
        <td id="L1560" class="blob-num js-line-number" data-line-number="1560"></td>
        <td id="LC1560" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">fluxgap</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.fluxGap, <span class="pl-smi">rot</span><span class="pl-k">=</span>FLErot)</td>
      </tr>
      <tr>
        <td id="L1561" class="blob-num js-line-number" data-line-number="1561"></td>
        <td id="LC1561" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1562" class="blob-num js-line-number" data-line-number="1562"></td>
        <td id="LC1562" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Connector</span></td>
      </tr>
      <tr>
        <td id="L1563" class="blob-num js-line-number" data-line-number="1563"></td>
        <td id="LC1563" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fluxEndConnect <span class="pl-k">=</span> (<span class="pl-v">self</span>.FLcoords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> np.cos(rad(FLErot))<span class="pl-k">*</span>(totLen<span class="pl-k">/</span><span class="pl-c1">2</span>),</td>
      </tr>
      <tr>
        <td id="L1564" class="blob-num js-line-number" data-line-number="1564"></td>
        <td id="LC1564" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.FLcoords[<span class="pl-c1">1</span>] <span class="pl-k">-</span>(totLen<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.sin(rad(FLErot)))</td>
      </tr>
      <tr>
        <td id="L1565" class="blob-num js-line-number" data-line-number="1565"></td>
        <td id="LC1565" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1566" class="blob-num js-line-number" data-line-number="1566"></td>
        <td id="LC1566" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1567" class="blob-num js-line-number" data-line-number="1567"></td>
        <td id="LC1567" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1568" class="blob-num js-line-number" data-line-number="1568"></td>
        <td id="LC1568" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1569" class="blob-num js-line-number" data-line-number="1569"></td>
        <td id="LC1569" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">TransmonBox</span>:</td>
      </tr>
      <tr>
        <td id="L1570" class="blob-num js-line-number" data-line-number="1570"></td>
        <td id="LC1570" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1571" class="blob-num js-line-number" data-line-number="1571"></td>
        <td id="LC1571" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Box for Transmon</span></td>
      </tr>
      <tr>
        <td id="L1572" class="blob-num js-line-number" data-line-number="1572"></td>
        <td id="LC1572" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1573" class="blob-num js-line-number" data-line-number="1573"></td>
        <td id="LC1573" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1574" class="blob-num js-line-number" data-line-number="1574"></td>
        <td id="LC1574" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">shape</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">offset</span>, <span class="pl-smi">almarks</span>, <span class="pl-smi">flip</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1575" class="blob-num js-line-number" data-line-number="1575"></td>
        <td id="LC1575" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1576" class="blob-num js-line-number" data-line-number="1576"></td>
        <td id="LC1576" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Initialize Transmon Box properties</span></td>
      </tr>
      <tr>
        <td id="L1577" class="blob-num js-line-number" data-line-number="1577"></td>
        <td id="LC1577" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1578" class="blob-num js-line-number" data-line-number="1578"></td>
        <td id="LC1578" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The offset is relative to the placeInfo, such that the</span></td>
      </tr>
      <tr>
        <td id="L1579" class="blob-num js-line-number" data-line-number="1579"></td>
        <td id="LC1579" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        transmonBox can be connected to a resonator or wiggle connector</span></td>
      </tr>
      <tr>
        <td id="L1580" class="blob-num js-line-number" data-line-number="1580"></td>
        <td id="LC1580" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1581" class="blob-num js-line-number" data-line-number="1581"></td>
        <td id="LC1581" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        flip switches a normal qubit to the other side of the Transmission line.</span></td>
      </tr>
      <tr>
        <td id="L1582" class="blob-num js-line-number" data-line-number="1582"></td>
        <td id="LC1582" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1583" class="blob-num js-line-number" data-line-number="1583"></td>
        <td id="LC1583" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1584" class="blob-num js-line-number" data-line-number="1584"></td>
        <td id="LC1584" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1585" class="blob-num js-line-number" data-line-number="1585"></td>
        <td id="LC1585" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1586" class="blob-num js-line-number" data-line-number="1586"></td>
        <td id="LC1586" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.shape <span class="pl-k">=</span> shape</td>
      </tr>
      <tr>
        <td id="L1587" class="blob-num js-line-number" data-line-number="1587"></td>
        <td id="LC1587" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.offset <span class="pl-k">=</span> offset</td>
      </tr>
      <tr>
        <td id="L1588" class="blob-num js-line-number" data-line-number="1588"></td>
        <td id="LC1588" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.alMarks <span class="pl-k">=</span> almarks</td>
      </tr>
      <tr>
        <td id="L1589" class="blob-num js-line-number" data-line-number="1589"></td>
        <td id="LC1589" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.flip <span class="pl-k">=</span> flip</td>
      </tr>
      <tr>
        <td id="L1590" class="blob-num js-line-number" data-line-number="1590"></td>
        <td id="LC1590" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1591" class="blob-num js-line-number" data-line-number="1591"></td>
        <td id="LC1591" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1592" class="blob-num js-line-number" data-line-number="1592"></td>
        <td id="LC1592" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Include the CPW dimensions for easier connecting</span></td>
      </tr>
      <tr>
        <td id="L1593" class="blob-num js-line-number" data-line-number="1593"></td>
        <td id="LC1593" class="blob-code blob-code-inner js-file-line">        xlen2 <span class="pl-k">=</span> <span class="pl-v">self</span>.offset[<span class="pl-c1">0</span>] <span class="pl-c">#+ self.shape[0]/2</span></td>
      </tr>
      <tr>
        <td id="L1594" class="blob-num js-line-number" data-line-number="1594"></td>
        <td id="LC1594" class="blob-code blob-code-inner js-file-line">        ylen2 <span class="pl-k">=</span> <span class="pl-v">self</span>.shape[<span class="pl-c1">1</span>]<span class="pl-k">/</span><span class="pl-c1">2.</span> <span class="pl-k">+</span> sampleX.b1<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">+</span> <span class="pl-v">self</span>.offset[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L1595" class="blob-num js-line-number" data-line-number="1595"></td>
        <td id="LC1595" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1596" class="blob-num js-line-number" data-line-number="1596"></td>
        <td id="LC1596" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1597" class="blob-num js-line-number" data-line-number="1597"></td>
        <td id="LC1597" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1598" class="blob-num js-line-number" data-line-number="1598"></td>
        <td id="LC1598" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1599" class="blob-num js-line-number" data-line-number="1599"></td>
        <td id="LC1599" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1600" class="blob-num js-line-number" data-line-number="1600"></td>
        <td id="LC1600" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1601" class="blob-num js-line-number" data-line-number="1601"></td>
        <td id="LC1601" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for the size of the component</span></td>
      </tr>
      <tr>
        <td id="L1602" class="blob-num js-line-number" data-line-number="1602"></td>
        <td id="LC1602" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.flip:</td>
      </tr>
      <tr>
        <td id="L1603" class="blob-num js-line-number" data-line-number="1603"></td>
        <td id="LC1603" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> (xlen2<span class="pl-k">*</span>np.cos(rad(rot))<span class="pl-k">+</span> ylen2<span class="pl-k">*</span>np.sin(rad(rot))),</td>
      </tr>
      <tr>
        <td id="L1604" class="blob-num js-line-number" data-line-number="1604"></td>
        <td id="LC1604" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span> xlen2<span class="pl-k">*</span>np.sin(rad(rot)) <span class="pl-k">+</span> ylen2<span class="pl-k">*</span>np.cos(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1605" class="blob-num js-line-number" data-line-number="1605"></td>
        <td id="LC1605" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1606" class="blob-num js-line-number" data-line-number="1606"></td>
        <td id="LC1606" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> (xlen2<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span> ylen2<span class="pl-k">*</span>np.sin(rad(rot))),</td>
      </tr>
      <tr>
        <td id="L1607" class="blob-num js-line-number" data-line-number="1607"></td>
        <td id="LC1607" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span> xlen2<span class="pl-k">*</span>np.sin(rad(rot)) <span class="pl-k">-</span> ylen2<span class="pl-k">*</span>np.cos(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1608" class="blob-num js-line-number" data-line-number="1608"></td>
        <td id="LC1608" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1609" class="blob-num js-line-number" data-line-number="1609"></td>
        <td id="LC1609" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1610" class="blob-num js-line-number" data-line-number="1610"></td>
        <td id="LC1610" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1611" class="blob-num js-line-number" data-line-number="1611"></td>
        <td id="LC1611" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1612" class="blob-num js-line-number" data-line-number="1612"></td>
        <td id="LC1612" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add connectors for non-corner transmon</span></td>
      </tr>
      <tr>
        <td id="L1613" class="blob-num js-line-number" data-line-number="1613"></td>
        <td id="LC1613" class="blob-code blob-code-inner js-file-line">        (w, h) <span class="pl-k">=</span> <span class="pl-v">self</span>.shape <span class="pl-c">#for easier typing</span></td>
      </tr>
      <tr>
        <td id="L1614" class="blob-num js-line-number" data-line-number="1614"></td>
        <td id="LC1614" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>]<span class="pl-k">-</span>w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1615" class="blob-num js-line-number" data-line-number="1615"></td>
        <td id="LC1615" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> np.sin(rad(rot))<span class="pl-k">*</span>w<span class="pl-k">/</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1616" class="blob-num js-line-number" data-line-number="1616"></td>
        <td id="LC1616" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectC <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>]<span class="pl-k">+</span>w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1617" class="blob-num js-line-number" data-line-number="1617"></td>
        <td id="LC1617" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> np.sin(rad(rot))<span class="pl-k">*</span>w<span class="pl-k">/</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1618" class="blob-num js-line-number" data-line-number="1618"></td>
        <td id="LC1618" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.flip:</td>
      </tr>
      <tr>
        <td id="L1619" class="blob-num js-line-number" data-line-number="1619"></td>
        <td id="LC1619" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> h<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.sin(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1620" class="blob-num js-line-number" data-line-number="1620"></td>
        <td id="LC1620" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>]<span class="pl-k">+</span><span class="pl-v">self</span>.shape[<span class="pl-c1">1</span>]<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1621" class="blob-num js-line-number" data-line-number="1621"></td>
        <td id="LC1621" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1622" class="blob-num js-line-number" data-line-number="1622"></td>
        <td id="LC1622" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span>h<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.sin(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1623" class="blob-num js-line-number" data-line-number="1623"></td>
        <td id="LC1623" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>]<span class="pl-k">-</span><span class="pl-v">self</span>.shape[<span class="pl-c1">1</span>]<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1624" class="blob-num js-line-number" data-line-number="1624"></td>
        <td id="LC1624" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1625" class="blob-num js-line-number" data-line-number="1625"></td>
        <td id="LC1625" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#make the cell</span></td>
      </tr>
      <tr>
        <td id="L1626" class="blob-num js-line-number" data-line-number="1626"></td>
        <td id="LC1626" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell()</td>
      </tr>
      <tr>
        <td id="L1627" class="blob-num js-line-number" data-line-number="1627"></td>
        <td id="LC1627" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add to sample Cell</span></td>
      </tr>
      <tr>
        <td id="L1628" class="blob-num js-line-number" data-line-number="1628"></td>
        <td id="LC1628" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1629" class="blob-num js-line-number" data-line-number="1629"></td>
        <td id="LC1629" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1630" class="blob-num js-line-number" data-line-number="1630"></td>
        <td id="LC1630" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1631" class="blob-num js-line-number" data-line-number="1631"></td>
        <td id="LC1631" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L1632" class="blob-num js-line-number" data-line-number="1632"></td>
        <td id="LC1632" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1633" class="blob-num js-line-number" data-line-number="1633"></td>
        <td id="LC1633" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Use the maskDesign module to generate the object</span></td>
      </tr>
      <tr>
        <td id="L1634" class="blob-num js-line-number" data-line-number="1634"></td>
        <td id="LC1634" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1635" class="blob-num js-line-number" data-line-number="1635"></td>
        <td id="LC1635" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1636" class="blob-num js-line-number" data-line-number="1636"></td>
        <td id="LC1636" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.transmonBoxAlign(<span class="pl-v">self</span>.coords, <span class="pl-v">self</span>.shape, <span class="pl-v">self</span>.alMarks, <span class="pl-v">self</span>.rot)</td>
      </tr>
      <tr>
        <td id="L1637" class="blob-num js-line-number" data-line-number="1637"></td>
        <td id="LC1637" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1638" class="blob-num js-line-number" data-line-number="1638"></td>
        <td id="LC1638" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1639" class="blob-num js-line-number" data-line-number="1639"></td>
        <td id="LC1639" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1640" class="blob-num js-line-number" data-line-number="1640"></td>
        <td id="LC1640" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">CornerTransmonBox</span>:</td>
      </tr>
      <tr>
        <td id="L1641" class="blob-num js-line-number" data-line-number="1641"></td>
        <td id="LC1641" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1642" class="blob-num js-line-number" data-line-number="1642"></td>
        <td id="LC1642" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    CornerBox for Transmon</span></td>
      </tr>
      <tr>
        <td id="L1643" class="blob-num js-line-number" data-line-number="1643"></td>
        <td id="LC1643" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1644" class="blob-num js-line-number" data-line-number="1644"></td>
        <td id="LC1644" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1645" class="blob-num js-line-number" data-line-number="1645"></td>
        <td id="LC1645" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">shape</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">offset</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1646" class="blob-num js-line-number" data-line-number="1646"></td>
        <td id="LC1646" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1647" class="blob-num js-line-number" data-line-number="1647"></td>
        <td id="LC1647" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Initialize Transmon Box properties</span></td>
      </tr>
      <tr>
        <td id="L1648" class="blob-num js-line-number" data-line-number="1648"></td>
        <td id="LC1648" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1649" class="blob-num js-line-number" data-line-number="1649"></td>
        <td id="LC1649" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        The offset is relative to the placeInfo, such that the</span></td>
      </tr>
      <tr>
        <td id="L1650" class="blob-num js-line-number" data-line-number="1650"></td>
        <td id="LC1650" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        cornertransmonBox can be connected to a resonator or wiggle connector</span></td>
      </tr>
      <tr>
        <td id="L1651" class="blob-num js-line-number" data-line-number="1651"></td>
        <td id="LC1651" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1652" class="blob-num js-line-number" data-line-number="1652"></td>
        <td id="LC1652" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        To put the cornerTransmon at the other side of a CPW, use rotate</span></td>
      </tr>
      <tr>
        <td id="L1653" class="blob-num js-line-number" data-line-number="1653"></td>
        <td id="LC1653" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1654" class="blob-num js-line-number" data-line-number="1654"></td>
        <td id="LC1654" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1655" class="blob-num js-line-number" data-line-number="1655"></td>
        <td id="LC1655" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.shape <span class="pl-k">=</span> shape</td>
      </tr>
      <tr>
        <td id="L1656" class="blob-num js-line-number" data-line-number="1656"></td>
        <td id="LC1656" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.offset <span class="pl-k">=</span> offset</td>
      </tr>
      <tr>
        <td id="L1657" class="blob-num js-line-number" data-line-number="1657"></td>
        <td id="LC1657" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1658" class="blob-num js-line-number" data-line-number="1658"></td>
        <td id="LC1658" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1659" class="blob-num js-line-number" data-line-number="1659"></td>
        <td id="LC1659" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Include the CPW dimensions for easier connecting</span></td>
      </tr>
      <tr>
        <td id="L1660" class="blob-num js-line-number" data-line-number="1660"></td>
        <td id="LC1660" class="blob-code blob-code-inner js-file-line">        xlen2 <span class="pl-k">=</span> <span class="pl-v">self</span>.shape[<span class="pl-c1">0</span>]<span class="pl-k">/</span><span class="pl-c1">2</span> <span class="pl-k">+</span> sampleX.b1<span class="pl-k">/</span><span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L1661" class="blob-num js-line-number" data-line-number="1661"></td>
        <td id="LC1661" class="blob-code blob-code-inner js-file-line">        ylen2 <span class="pl-k">=</span> <span class="pl-v">self</span>.shape[<span class="pl-c1">0</span>]<span class="pl-k">/</span><span class="pl-c1">2</span> <span class="pl-k">+</span> sampleX.b1<span class="pl-k">/</span><span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L1662" class="blob-num js-line-number" data-line-number="1662"></td>
        <td id="LC1662" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1663" class="blob-num js-line-number" data-line-number="1663"></td>
        <td id="LC1663" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1664" class="blob-num js-line-number" data-line-number="1664"></td>
        <td id="LC1664" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1665" class="blob-num js-line-number" data-line-number="1665"></td>
        <td id="LC1665" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1666" class="blob-num js-line-number" data-line-number="1666"></td>
        <td id="LC1666" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1667" class="blob-num js-line-number" data-line-number="1667"></td>
        <td id="LC1667" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1668" class="blob-num js-line-number" data-line-number="1668"></td>
        <td id="LC1668" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for the size of the component</span></td>
      </tr>
      <tr>
        <td id="L1669" class="blob-num js-line-number" data-line-number="1669"></td>
        <td id="LC1669" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.offset[<span class="pl-c1">0</span>] <span class="pl-k">-</span> xlen2<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span> ylen2<span class="pl-k">*</span>np.sin(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1670" class="blob-num js-line-number" data-line-number="1670"></td>
        <td id="LC1670" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.offset[<span class="pl-c1">1</span>] <span class="pl-k">+</span> ylen2<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span> xlen2<span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1671" class="blob-num js-line-number" data-line-number="1671"></td>
        <td id="LC1671" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-c1">type</span>(placeInfo[<span class="pl-c1">0</span>]) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1672" class="blob-num js-line-number" data-line-number="1672"></td>
        <td id="LC1672" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1673" class="blob-num js-line-number" data-line-number="1673"></td>
        <td id="LC1673" class="blob-code blob-code-inner js-file-line">            comp1 <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo[<span class="pl-c1">0</span>].split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1674" class="blob-num js-line-number" data-line-number="1674"></td>
        <td id="LC1674" class="blob-code blob-code-inner js-file-line">            comp2 <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo[<span class="pl-c1">1</span>].split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1675" class="blob-num js-line-number" data-line-number="1675"></td>
        <td id="LC1675" class="blob-code blob-code-inner js-file-line">            cpx <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp1, placeInfo[<span class="pl-c1">0</span>].split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L1676" class="blob-num js-line-number" data-line-number="1676"></td>
        <td id="LC1676" class="blob-code blob-code-inner js-file-line">            cpy <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp2, placeInfo[<span class="pl-c1">0</span>].split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L1677" class="blob-num js-line-number" data-line-number="1677"></td>
        <td id="LC1677" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>cpx, cpy are <span class="pl-pds">&#39;</span></span>, cpx, cpy</td>
      </tr>
      <tr>
        <td id="L1678" class="blob-num js-line-number" data-line-number="1678"></td>
        <td id="LC1678" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> (cpx, cpy)</td>
      </tr>
      <tr>
        <td id="L1679" class="blob-num js-line-number" data-line-number="1679"></td>
        <td id="LC1679" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for the size of the component</span></td>
      </tr>
      <tr>
        <td id="L1680" class="blob-num js-line-number" data-line-number="1680"></td>
        <td id="LC1680" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.offset[<span class="pl-c1">0</span>] <span class="pl-k">-</span> xlen2<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span> ylen2<span class="pl-k">*</span>np.sin(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1681" class="blob-num js-line-number" data-line-number="1681"></td>
        <td id="LC1681" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.offset[<span class="pl-c1">1</span>] <span class="pl-k">+</span> ylen2<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span> xlen2<span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1682" class="blob-num js-line-number" data-line-number="1682"></td>
        <td id="LC1682" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1683" class="blob-num js-line-number" data-line-number="1683"></td>
        <td id="LC1683" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1684" class="blob-num js-line-number" data-line-number="1684"></td>
        <td id="LC1684" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1685" class="blob-num js-line-number" data-line-number="1685"></td>
        <td id="LC1685" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1686" class="blob-num js-line-number" data-line-number="1686"></td>
        <td id="LC1686" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1687" class="blob-num js-line-number" data-line-number="1687"></td>
        <td id="LC1687" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Connectors</span></td>
      </tr>
      <tr>
        <td id="L1688" class="blob-num js-line-number" data-line-number="1688"></td>
        <td id="LC1688" class="blob-code blob-code-inner js-file-line">        (w, h) <span class="pl-k">=</span> <span class="pl-v">self</span>.shape <span class="pl-c">#for easier typing</span></td>
      </tr>
      <tr>
        <td id="L1689" class="blob-num js-line-number" data-line-number="1689"></td>
        <td id="LC1689" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">+</span> (w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.sin(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1690" class="blob-num js-line-number" data-line-number="1690"></td>
        <td id="LC1690" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> (w<span class="pl-k">/</span><span class="pl-c1">2</span> <span class="pl-k">-</span> h<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span> w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1691" class="blob-num js-line-number" data-line-number="1691"></td>
        <td id="LC1691" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span>(w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span> (w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h)<span class="pl-k">*</span>np.sin(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1692" class="blob-num js-line-number" data-line-number="1692"></td>
        <td id="LC1692" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> (w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h)<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span> (w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1693" class="blob-num js-line-number" data-line-number="1693"></td>
        <td id="LC1693" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectC <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span>(w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h)<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span> (w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.sin(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1694" class="blob-num js-line-number" data-line-number="1694"></td>
        <td id="LC1694" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> (w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">+</span> (w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h)<span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1695" class="blob-num js-line-number" data-line-number="1695"></td>
        <td id="LC1695" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectD <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span>(w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">-</span>(w<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.sin(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1696" class="blob-num js-line-number" data-line-number="1696"></td>
        <td id="LC1696" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">*</span>np.cos(rad(rot)) <span class="pl-k">+</span> (w<span class="pl-k">/</span><span class="pl-c1">2</span><span class="pl-k">-</span>h<span class="pl-k">/</span><span class="pl-c1">2</span>)<span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1697" class="blob-num js-line-number" data-line-number="1697"></td>
        <td id="LC1697" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1698" class="blob-num js-line-number" data-line-number="1698"></td>
        <td id="LC1698" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#make the cell</span></td>
      </tr>
      <tr>
        <td id="L1699" class="blob-num js-line-number" data-line-number="1699"></td>
        <td id="LC1699" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell()</td>
      </tr>
      <tr>
        <td id="L1700" class="blob-num js-line-number" data-line-number="1700"></td>
        <td id="LC1700" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add to sample Cell</span></td>
      </tr>
      <tr>
        <td id="L1701" class="blob-num js-line-number" data-line-number="1701"></td>
        <td id="LC1701" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1702" class="blob-num js-line-number" data-line-number="1702"></td>
        <td id="LC1702" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1703" class="blob-num js-line-number" data-line-number="1703"></td>
        <td id="LC1703" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1704" class="blob-num js-line-number" data-line-number="1704"></td>
        <td id="LC1704" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L1705" class="blob-num js-line-number" data-line-number="1705"></td>
        <td id="LC1705" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1706" class="blob-num js-line-number" data-line-number="1706"></td>
        <td id="LC1706" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Use the maskDesign module to generate the object</span></td>
      </tr>
      <tr>
        <td id="L1707" class="blob-num js-line-number" data-line-number="1707"></td>
        <td id="LC1707" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1708" class="blob-num js-line-number" data-line-number="1708"></td>
        <td id="LC1708" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1709" class="blob-num js-line-number" data-line-number="1709"></td>
        <td id="LC1709" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#construct object</span></td>
      </tr>
      <tr>
        <td id="L1710" class="blob-num js-line-number" data-line-number="1710"></td>
        <td id="LC1710" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.cornerTransmonBox(<span class="pl-v">self</span>.coords, <span class="pl-v">self</span>.shape, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-v">self</span>.rot)</td>
      </tr>
      <tr>
        <td id="L1711" class="blob-num js-line-number" data-line-number="1711"></td>
        <td id="LC1711" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1712" class="blob-num js-line-number" data-line-number="1712"></td>
        <td id="LC1712" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1713" class="blob-num js-line-number" data-line-number="1713"></td>
        <td id="LC1713" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1714" class="blob-num js-line-number" data-line-number="1714"></td>
        <td id="LC1714" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Airbridge</span>:</td>
      </tr>
      <tr>
        <td id="L1715" class="blob-num js-line-number" data-line-number="1715"></td>
        <td id="LC1715" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1716" class="blob-num js-line-number" data-line-number="1716"></td>
        <td id="LC1716" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">bridgeLenX</span>, <span class="pl-smi">bridgeLenY</span>, <span class="pl-smi">footerLen</span>,</td>
      </tr>
      <tr>
        <td id="L1717" class="blob-num js-line-number" data-line-number="1717"></td>
        <td id="LC1717" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">irGap</span>, <span class="pl-smi">reflowGap</span>, <span class="pl-smi">layers</span>, <span class="pl-smi">offset</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1718" class="blob-num js-line-number" data-line-number="1718"></td>
        <td id="LC1718" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1719" class="blob-num js-line-number" data-line-number="1719"></td>
        <td id="LC1719" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Initialize the Airbridge</span></td>
      </tr>
      <tr>
        <td id="L1720" class="blob-num js-line-number" data-line-number="1720"></td>
        <td id="LC1720" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1721" class="blob-num js-line-number" data-line-number="1721"></td>
        <td id="LC1721" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1722" class="blob-num js-line-number" data-line-number="1722"></td>
        <td id="LC1722" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1723" class="blob-num js-line-number" data-line-number="1723"></td>
        <td id="LC1723" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Iinitialize Attributes</span></td>
      </tr>
      <tr>
        <td id="L1724" class="blob-num js-line-number" data-line-number="1724"></td>
        <td id="LC1724" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridgeLenX <span class="pl-k">=</span> bridgeLenX</td>
      </tr>
      <tr>
        <td id="L1725" class="blob-num js-line-number" data-line-number="1725"></td>
        <td id="LC1725" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.bridgeLenY <span class="pl-k">=</span> bridgeLenY</td>
      </tr>
      <tr>
        <td id="L1726" class="blob-num js-line-number" data-line-number="1726"></td>
        <td id="LC1726" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.footerLen <span class="pl-k">=</span> footerLen</td>
      </tr>
      <tr>
        <td id="L1727" class="blob-num js-line-number" data-line-number="1727"></td>
        <td id="LC1727" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.irGap <span class="pl-k">=</span> irGap</td>
      </tr>
      <tr>
        <td id="L1728" class="blob-num js-line-number" data-line-number="1728"></td>
        <td id="LC1728" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.reflowGap <span class="pl-k">=</span> reflowGap</td>
      </tr>
      <tr>
        <td id="L1729" class="blob-num js-line-number" data-line-number="1729"></td>
        <td id="LC1729" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.layers <span class="pl-k">=</span> layers</td>
      </tr>
      <tr>
        <td id="L1730" class="blob-num js-line-number" data-line-number="1730"></td>
        <td id="LC1730" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.offset <span class="pl-k">=</span> offset</td>
      </tr>
      <tr>
        <td id="L1731" class="blob-num js-line-number" data-line-number="1731"></td>
        <td id="LC1731" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1732" class="blob-num js-line-number" data-line-number="1732"></td>
        <td id="LC1732" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1733" class="blob-num js-line-number" data-line-number="1733"></td>
        <td id="LC1733" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1734" class="blob-num js-line-number" data-line-number="1734"></td>
        <td id="LC1734" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1735" class="blob-num js-line-number" data-line-number="1735"></td>
        <td id="LC1735" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: put one airbridge perpendicular to whatever I got</span></td>
      </tr>
      <tr>
        <td id="L1736" class="blob-num js-line-number" data-line-number="1736"></td>
        <td id="LC1736" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1737" class="blob-num js-line-number" data-line-number="1737"></td>
        <td id="LC1737" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1738" class="blob-num js-line-number" data-line-number="1738"></td>
        <td id="LC1738" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>]<span class="pl-k">+</span><span class="pl-v">self</span>.offset[<span class="pl-c1">0</span>], <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>]<span class="pl-k">+</span><span class="pl-v">self</span>.offset[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1739" class="blob-num js-line-number" data-line-number="1739"></td>
        <td id="LC1739" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1740" class="blob-num js-line-number" data-line-number="1740"></td>
        <td id="LC1740" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1741" class="blob-num js-line-number" data-line-number="1741"></td>
        <td id="LC1741" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1742" class="blob-num js-line-number" data-line-number="1742"></td>
        <td id="LC1742" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1743" class="blob-num js-line-number" data-line-number="1743"></td>
        <td id="LC1743" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Make the Cell</span></td>
      </tr>
      <tr>
        <td id="L1744" class="blob-num js-line-number" data-line-number="1744"></td>
        <td id="LC1744" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L1745" class="blob-num js-line-number" data-line-number="1745"></td>
        <td id="LC1745" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1746" class="blob-num js-line-number" data-line-number="1746"></td>
        <td id="LC1746" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>,<span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1747" class="blob-num js-line-number" data-line-number="1747"></td>
        <td id="LC1747" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1748" class="blob-num js-line-number" data-line-number="1748"></td>
        <td id="LC1748" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        make the cad Cell reference of the CPW</span></td>
      </tr>
      <tr>
        <td id="L1749" class="blob-num js-line-number" data-line-number="1749"></td>
        <td id="LC1749" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1750" class="blob-num js-line-number" data-line-number="1750"></td>
        <td id="LC1750" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.airBridge(<span class="pl-v">self</span>.coords, <span class="pl-smi">footerLen</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.footerLen,</td>
      </tr>
      <tr>
        <td id="L1751" class="blob-num js-line-number" data-line-number="1751"></td>
        <td id="LC1751" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">bridgeSizeX</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.bridgeLenX, <span class="pl-smi">bridgeSizeY</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.bridgeLenY,</td>
      </tr>
      <tr>
        <td id="L1752" class="blob-num js-line-number" data-line-number="1752"></td>
        <td id="LC1752" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">reflowGap</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.reflowGap, <span class="pl-smi">irGap</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.irGap,</td>
      </tr>
      <tr>
        <td id="L1753" class="blob-num js-line-number" data-line-number="1753"></td>
        <td id="LC1753" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">layers</span> <span class="pl-k">=</span> <span class="pl-c1">list</span>(<span class="pl-v">self</span>.layers), <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-v">self</span>.rot)</td>
      </tr>
      <tr>
        <td id="L1754" class="blob-num js-line-number" data-line-number="1754"></td>
        <td id="LC1754" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1755" class="blob-num js-line-number" data-line-number="1755"></td>
        <td id="LC1755" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add the cell to the TopCell</span></td>
      </tr>
      <tr>
        <td id="L1756" class="blob-num js-line-number" data-line-number="1756"></td>
        <td id="LC1756" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1757" class="blob-num js-line-number" data-line-number="1757"></td>
        <td id="LC1757" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1758" class="blob-num js-line-number" data-line-number="1758"></td>
        <td id="LC1758" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1759" class="blob-num js-line-number" data-line-number="1759"></td>
        <td id="LC1759" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1760" class="blob-num js-line-number" data-line-number="1760"></td>
        <td id="LC1760" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">GapCoupler</span>:</td>
      </tr>
      <tr>
        <td id="L1761" class="blob-num js-line-number" data-line-number="1761"></td>
        <td id="LC1761" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1762" class="blob-num js-line-number" data-line-number="1762"></td>
        <td id="LC1762" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">gapSize</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">extralen</span>, <span class="pl-smi">flip</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1763" class="blob-num js-line-number" data-line-number="1763"></td>
        <td id="LC1763" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1764" class="blob-num js-line-number" data-line-number="1764"></td>
        <td id="LC1764" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Construct a gapCoupler</span></td>
      </tr>
      <tr>
        <td id="L1765" class="blob-num js-line-number" data-line-number="1765"></td>
        <td id="LC1765" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1766" class="blob-num js-line-number" data-line-number="1766"></td>
        <td id="LC1766" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1767" class="blob-num js-line-number" data-line-number="1767"></td>
        <td id="LC1767" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1768" class="blob-num js-line-number" data-line-number="1768"></td>
        <td id="LC1768" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gapSize <span class="pl-k">=</span> gapSize</td>
      </tr>
      <tr>
        <td id="L1769" class="blob-num js-line-number" data-line-number="1769"></td>
        <td id="LC1769" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.flip <span class="pl-k">=</span> flip</td>
      </tr>
      <tr>
        <td id="L1770" class="blob-num js-line-number" data-line-number="1770"></td>
        <td id="LC1770" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1771" class="blob-num js-line-number" data-line-number="1771"></td>
        <td id="LC1771" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#By default, make the length as long as the gap</span></td>
      </tr>
      <tr>
        <td id="L1772" class="blob-num js-line-number" data-line-number="1772"></td>
        <td id="LC1772" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.leng <span class="pl-k">=</span> <span class="pl-v">self</span>.gapSize <span class="pl-k">+</span> extralen</td>
      </tr>
      <tr>
        <td id="L1773" class="blob-num js-line-number" data-line-number="1773"></td>
        <td id="LC1773" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1774" class="blob-num js-line-number" data-line-number="1774"></td>
        <td id="LC1774" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1775" class="blob-num js-line-number" data-line-number="1775"></td>
        <td id="LC1775" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1776" class="blob-num js-line-number" data-line-number="1776"></td>
        <td id="LC1776" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1777" class="blob-num js-line-number" data-line-number="1777"></td>
        <td id="LC1777" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1778" class="blob-num js-line-number" data-line-number="1778"></td>
        <td id="LC1778" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1779" class="blob-num js-line-number" data-line-number="1779"></td>
        <td id="LC1779" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#adjust for the size of the component</span></td>
      </tr>
      <tr>
        <td id="L1780" class="blob-num js-line-number" data-line-number="1780"></td>
        <td id="LC1780" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> flip:</td>
      </tr>
      <tr>
        <td id="L1781" class="blob-num js-line-number" data-line-number="1781"></td>
        <td id="LC1781" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1782" class="blob-num js-line-number" data-line-number="1782"></td>
        <td id="LC1782" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1783" class="blob-num js-line-number" data-line-number="1783"></td>
        <td id="LC1783" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1784" class="blob-num js-line-number" data-line-number="1784"></td>
        <td id="LC1784" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1785" class="blob-num js-line-number" data-line-number="1785"></td>
        <td id="LC1785" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1786" class="blob-num js-line-number" data-line-number="1786"></td>
        <td id="LC1786" class="blob-code blob-code-inner js-file-line">      </td>
      </tr>
      <tr>
        <td id="L1787" class="blob-num js-line-number" data-line-number="1787"></td>
        <td id="LC1787" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1788" class="blob-num js-line-number" data-line-number="1788"></td>
        <td id="LC1788" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1789" class="blob-num js-line-number" data-line-number="1789"></td>
        <td id="LC1789" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeinfo</td>
      </tr>
      <tr>
        <td id="L1790" class="blob-num js-line-number" data-line-number="1790"></td>
        <td id="LC1790" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1791" class="blob-num js-line-number" data-line-number="1791"></td>
        <td id="LC1791" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Connector locations</span></td>
      </tr>
      <tr>
        <td id="L1792" class="blob-num js-line-number" data-line-number="1792"></td>
        <td id="LC1792" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1793" class="blob-num js-line-number" data-line-number="1793"></td>
        <td id="LC1793" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1794" class="blob-num js-line-number" data-line-number="1794"></td>
        <td id="LC1794" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1795" class="blob-num js-line-number" data-line-number="1795"></td>
        <td id="LC1795" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1796" class="blob-num js-line-number" data-line-number="1796"></td>
        <td id="LC1796" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1797" class="blob-num js-line-number" data-line-number="1797"></td>
        <td id="LC1797" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L1798" class="blob-num js-line-number" data-line-number="1798"></td>
        <td id="LC1798" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1799" class="blob-num js-line-number" data-line-number="1799"></td>
        <td id="LC1799" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1800" class="blob-num js-line-number" data-line-number="1800"></td>
        <td id="LC1800" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1801" class="blob-num js-line-number" data-line-number="1801"></td>
        <td id="LC1801" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#construct object</span></td>
      </tr>
      <tr>
        <td id="L1802" class="blob-num js-line-number" data-line-number="1802"></td>
        <td id="LC1802" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.gapCoupler(<span class="pl-v">self</span>.coords,<span class="pl-v">self</span>.gapSize,<span class="pl-smi">leng</span><span class="pl-k">=</span><span class="pl-v">self</span>.leng,<span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-v">self</span>.rot, <span class="pl-smi">center</span><span class="pl-k">=</span>sampleX.a1, <span class="pl-smi">gap</span><span class="pl-k">=</span>sampleX.b1)</td>
      </tr>
      <tr>
        <td id="L1803" class="blob-num js-line-number" data-line-number="1803"></td>
        <td id="LC1803" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add to sample Cell</span></td>
      </tr>
      <tr>
        <td id="L1804" class="blob-num js-line-number" data-line-number="1804"></td>
        <td id="LC1804" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1805" class="blob-num js-line-number" data-line-number="1805"></td>
        <td id="LC1805" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1806" class="blob-num js-line-number" data-line-number="1806"></td>
        <td id="LC1806" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1807" class="blob-num js-line-number" data-line-number="1807"></td>
        <td id="LC1807" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">FingerCap</span>:</td>
      </tr>
      <tr>
        <td id="L1808" class="blob-num js-line-number" data-line-number="1808"></td>
        <td id="LC1808" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L1809" class="blob-num js-line-number" data-line-number="1809"></td>
        <td id="LC1809" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">nFingers</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">fingerLen</span>, <span class="pl-smi">fingerThick</span>,</td>
      </tr>
      <tr>
        <td id="L1810" class="blob-num js-line-number" data-line-number="1810"></td>
        <td id="LC1810" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">gapHeight</span>, <span class="pl-smi">gapWidth</span>, <span class="pl-smi">flip</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1811" class="blob-num js-line-number" data-line-number="1811"></td>
        <td id="LC1811" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1812" class="blob-num js-line-number" data-line-number="1812"></td>
        <td id="LC1812" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Construct a gapCoupler</span></td>
      </tr>
      <tr>
        <td id="L1813" class="blob-num js-line-number" data-line-number="1813"></td>
        <td id="LC1813" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1814" class="blob-num js-line-number" data-line-number="1814"></td>
        <td id="LC1814" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1815" class="blob-num js-line-number" data-line-number="1815"></td>
        <td id="LC1815" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#attributes</span></td>
      </tr>
      <tr>
        <td id="L1816" class="blob-num js-line-number" data-line-number="1816"></td>
        <td id="LC1816" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.nFingers <span class="pl-k">=</span> nFingers</td>
      </tr>
      <tr>
        <td id="L1817" class="blob-num js-line-number" data-line-number="1817"></td>
        <td id="LC1817" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerLen <span class="pl-k">=</span> fingerLen</td>
      </tr>
      <tr>
        <td id="L1818" class="blob-num js-line-number" data-line-number="1818"></td>
        <td id="LC1818" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerThick <span class="pl-k">=</span> fingerThick</td>
      </tr>
      <tr>
        <td id="L1819" class="blob-num js-line-number" data-line-number="1819"></td>
        <td id="LC1819" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gapHeight <span class="pl-k">=</span> gapHeight</td>
      </tr>
      <tr>
        <td id="L1820" class="blob-num js-line-number" data-line-number="1820"></td>
        <td id="LC1820" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gapWidth <span class="pl-k">=</span> gapWidth</td>
      </tr>
      <tr>
        <td id="L1821" class="blob-num js-line-number" data-line-number="1821"></td>
        <td id="LC1821" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.flip <span class="pl-k">=</span> flip</td>
      </tr>
      <tr>
        <td id="L1822" class="blob-num js-line-number" data-line-number="1822"></td>
        <td id="LC1822" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1823" class="blob-num js-line-number" data-line-number="1823"></td>
        <td id="LC1823" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1824" class="blob-num js-line-number" data-line-number="1824"></td>
        <td id="LC1824" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.leng <span class="pl-k">=</span> fingerLen <span class="pl-k">+</span> <span class="pl-c1">2</span><span class="pl-k">*</span>gapWidth</td>
      </tr>
      <tr>
        <td id="L1825" class="blob-num js-line-number" data-line-number="1825"></td>
        <td id="LC1825" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1826" class="blob-num js-line-number" data-line-number="1826"></td>
        <td id="LC1826" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1827" class="blob-num js-line-number" data-line-number="1827"></td>
        <td id="LC1827" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1828" class="blob-num js-line-number" data-line-number="1828"></td>
        <td id="LC1828" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1829" class="blob-num js-line-number" data-line-number="1829"></td>
        <td id="LC1829" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1830" class="blob-num js-line-number" data-line-number="1830"></td>
        <td id="LC1830" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for the size of the component</span></td>
      </tr>
      <tr>
        <td id="L1831" class="blob-num js-line-number" data-line-number="1831"></td>
        <td id="LC1831" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> flip:</td>
      </tr>
      <tr>
        <td id="L1832" class="blob-num js-line-number" data-line-number="1832"></td>
        <td id="LC1832" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1833" class="blob-num js-line-number" data-line-number="1833"></td>
        <td id="LC1833" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1834" class="blob-num js-line-number" data-line-number="1834"></td>
        <td id="LC1834" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1835" class="blob-num js-line-number" data-line-number="1835"></td>
        <td id="LC1835" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1836" class="blob-num js-line-number" data-line-number="1836"></td>
        <td id="LC1836" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1837" class="blob-num js-line-number" data-line-number="1837"></td>
        <td id="LC1837" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1838" class="blob-num js-line-number" data-line-number="1838"></td>
        <td id="LC1838" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1839" class="blob-num js-line-number" data-line-number="1839"></td>
        <td id="LC1839" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1840" class="blob-num js-line-number" data-line-number="1840"></td>
        <td id="LC1840" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1841" class="blob-num js-line-number" data-line-number="1841"></td>
        <td id="LC1841" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Connector locations</span></td>
      </tr>
      <tr>
        <td id="L1842" class="blob-num js-line-number" data-line-number="1842"></td>
        <td id="LC1842" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1843" class="blob-num js-line-number" data-line-number="1843"></td>
        <td id="LC1843" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1844" class="blob-num js-line-number" data-line-number="1844"></td>
        <td id="LC1844" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1845" class="blob-num js-line-number" data-line-number="1845"></td>
        <td id="LC1845" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1846" class="blob-num js-line-number" data-line-number="1846"></td>
        <td id="LC1846" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1847" class="blob-num js-line-number" data-line-number="1847"></td>
        <td id="LC1847" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L1848" class="blob-num js-line-number" data-line-number="1848"></td>
        <td id="LC1848" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1849" class="blob-num js-line-number" data-line-number="1849"></td>
        <td id="LC1849" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1850" class="blob-num js-line-number" data-line-number="1850"></td>
        <td id="LC1850" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1851" class="blob-num js-line-number" data-line-number="1851"></td>
        <td id="LC1851" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#construct object</span></td>
      </tr>
      <tr>
        <td id="L1852" class="blob-num js-line-number" data-line-number="1852"></td>
        <td id="LC1852" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.fingerCap(<span class="pl-v">self</span>.coords,<span class="pl-v">self</span>.nFingers, <span class="pl-v">self</span>.fingerLen,</td>
      </tr>
      <tr>
        <td id="L1853" class="blob-num js-line-number" data-line-number="1853"></td>
        <td id="LC1853" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.fingerThick, <span class="pl-v">self</span>.gapHeight, <span class="pl-v">self</span>.gapWidth, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-v">self</span>.rot)</td>
      </tr>
      <tr>
        <td id="L1854" class="blob-num js-line-number" data-line-number="1854"></td>
        <td id="LC1854" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add to sample Cell</span></td>
      </tr>
      <tr>
        <td id="L1855" class="blob-num js-line-number" data-line-number="1855"></td>
        <td id="LC1855" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1856" class="blob-num js-line-number" data-line-number="1856"></td>
        <td id="LC1856" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1857" class="blob-num js-line-number" data-line-number="1857"></td>
        <td id="LC1857" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1858" class="blob-num js-line-number" data-line-number="1858"></td>
        <td id="LC1858" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1859" class="blob-num js-line-number" data-line-number="1859"></td>
        <td id="LC1859" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">FingerCoupler</span>:</td>
      </tr>
      <tr>
        <td id="L1860" class="blob-num js-line-number" data-line-number="1860"></td>
        <td id="LC1860" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L1861" class="blob-num js-line-number" data-line-number="1861"></td>
        <td id="LC1861" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">nFingers</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">fingerLen</span>, <span class="pl-smi">fingerThick</span>,</td>
      </tr>
      <tr>
        <td id="L1862" class="blob-num js-line-number" data-line-number="1862"></td>
        <td id="LC1862" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">gapHeight</span>, <span class="pl-smi">gapWidth</span>, <span class="pl-smi">taperLen</span>, <span class="pl-smi">centerLen</span>, <span class="pl-smi">flip</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1863" class="blob-num js-line-number" data-line-number="1863"></td>
        <td id="LC1863" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1864" class="blob-num js-line-number" data-line-number="1864"></td>
        <td id="LC1864" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Construct a gapCoupler</span></td>
      </tr>
      <tr>
        <td id="L1865" class="blob-num js-line-number" data-line-number="1865"></td>
        <td id="LC1865" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1866" class="blob-num js-line-number" data-line-number="1866"></td>
        <td id="LC1866" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1867" class="blob-num js-line-number" data-line-number="1867"></td>
        <td id="LC1867" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#attributes</span></td>
      </tr>
      <tr>
        <td id="L1868" class="blob-num js-line-number" data-line-number="1868"></td>
        <td id="LC1868" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.nFingers <span class="pl-k">=</span> nFingers</td>
      </tr>
      <tr>
        <td id="L1869" class="blob-num js-line-number" data-line-number="1869"></td>
        <td id="LC1869" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerLen <span class="pl-k">=</span> fingerLen</td>
      </tr>
      <tr>
        <td id="L1870" class="blob-num js-line-number" data-line-number="1870"></td>
        <td id="LC1870" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fingerThick <span class="pl-k">=</span> fingerThick</td>
      </tr>
      <tr>
        <td id="L1871" class="blob-num js-line-number" data-line-number="1871"></td>
        <td id="LC1871" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gapHeight <span class="pl-k">=</span> gapHeight</td>
      </tr>
      <tr>
        <td id="L1872" class="blob-num js-line-number" data-line-number="1872"></td>
        <td id="LC1872" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.gapWidth <span class="pl-k">=</span> gapWidth</td>
      </tr>
      <tr>
        <td id="L1873" class="blob-num js-line-number" data-line-number="1873"></td>
        <td id="LC1873" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.taperLen <span class="pl-k">=</span> taperLen</td>
      </tr>
      <tr>
        <td id="L1874" class="blob-num js-line-number" data-line-number="1874"></td>
        <td id="LC1874" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.centerLen <span class="pl-k">=</span> centerLen</td>
      </tr>
      <tr>
        <td id="L1875" class="blob-num js-line-number" data-line-number="1875"></td>
        <td id="LC1875" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.flip <span class="pl-k">=</span> flip</td>
      </tr>
      <tr>
        <td id="L1876" class="blob-num js-line-number" data-line-number="1876"></td>
        <td id="LC1876" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1877" class="blob-num js-line-number" data-line-number="1877"></td>
        <td id="LC1877" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1878" class="blob-num js-line-number" data-line-number="1878"></td>
        <td id="LC1878" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.leng <span class="pl-k">=</span> centerLen <span class="pl-k">+</span> <span class="pl-c1">2</span><span class="pl-k">*</span>taperLen</td>
      </tr>
      <tr>
        <td id="L1879" class="blob-num js-line-number" data-line-number="1879"></td>
        <td id="LC1879" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1880" class="blob-num js-line-number" data-line-number="1880"></td>
        <td id="LC1880" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1881" class="blob-num js-line-number" data-line-number="1881"></td>
        <td id="LC1881" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1882" class="blob-num js-line-number" data-line-number="1882"></td>
        <td id="LC1882" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1883" class="blob-num js-line-number" data-line-number="1883"></td>
        <td id="LC1883" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1884" class="blob-num js-line-number" data-line-number="1884"></td>
        <td id="LC1884" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for the size of the component</span></td>
      </tr>
      <tr>
        <td id="L1885" class="blob-num js-line-number" data-line-number="1885"></td>
        <td id="LC1885" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> flip:</td>
      </tr>
      <tr>
        <td id="L1886" class="blob-num js-line-number" data-line-number="1886"></td>
        <td id="LC1886" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1887" class="blob-num js-line-number" data-line-number="1887"></td>
        <td id="LC1887" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1888" class="blob-num js-line-number" data-line-number="1888"></td>
        <td id="LC1888" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1889" class="blob-num js-line-number" data-line-number="1889"></td>
        <td id="LC1889" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L1890" class="blob-num js-line-number" data-line-number="1890"></td>
        <td id="LC1890" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1891" class="blob-num js-line-number" data-line-number="1891"></td>
        <td id="LC1891" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1892" class="blob-num js-line-number" data-line-number="1892"></td>
        <td id="LC1892" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1893" class="blob-num js-line-number" data-line-number="1893"></td>
        <td id="LC1893" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1894" class="blob-num js-line-number" data-line-number="1894"></td>
        <td id="LC1894" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1895" class="blob-num js-line-number" data-line-number="1895"></td>
        <td id="LC1895" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Connector locations</span></td>
      </tr>
      <tr>
        <td id="L1896" class="blob-num js-line-number" data-line-number="1896"></td>
        <td id="LC1896" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1897" class="blob-num js-line-number" data-line-number="1897"></td>
        <td id="LC1897" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1898" class="blob-num js-line-number" data-line-number="1898"></td>
        <td id="LC1898" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L1899" class="blob-num js-line-number" data-line-number="1899"></td>
        <td id="LC1899" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.leng<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L1900" class="blob-num js-line-number" data-line-number="1900"></td>
        <td id="LC1900" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1901" class="blob-num js-line-number" data-line-number="1901"></td>
        <td id="LC1901" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L1902" class="blob-num js-line-number" data-line-number="1902"></td>
        <td id="LC1902" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1903" class="blob-num js-line-number" data-line-number="1903"></td>
        <td id="LC1903" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L1904" class="blob-num js-line-number" data-line-number="1904"></td>
        <td id="LC1904" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1905" class="blob-num js-line-number" data-line-number="1905"></td>
        <td id="LC1905" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#construct object</span></td>
      </tr>
      <tr>
        <td id="L1906" class="blob-num js-line-number" data-line-number="1906"></td>
        <td id="LC1906" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.fingerCoupler(<span class="pl-v">self</span>.coords,<span class="pl-v">self</span>.nFingers, <span class="pl-v">self</span>.fingerLen,</td>
      </tr>
      <tr>
        <td id="L1907" class="blob-num js-line-number" data-line-number="1907"></td>
        <td id="LC1907" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.fingerThick, <span class="pl-v">self</span>.gapHeight, <span class="pl-v">self</span>.gapWidth, </td>
      </tr>
      <tr>
        <td id="L1908" class="blob-num js-line-number" data-line-number="1908"></td>
        <td id="LC1908" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.taperLen, <span class="pl-v">self</span>.centerLen, <span class="pl-smi">center</span><span class="pl-k">=</span>sampleX.a1, <span class="pl-smi">gap</span><span class="pl-k">=</span>sampleX.b1, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-v">self</span>.rot)</td>
      </tr>
      <tr>
        <td id="L1909" class="blob-num js-line-number" data-line-number="1909"></td>
        <td id="LC1909" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Add to sample Cell</span></td>
      </tr>
      <tr>
        <td id="L1910" class="blob-num js-line-number" data-line-number="1910"></td>
        <td id="LC1910" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1911" class="blob-num js-line-number" data-line-number="1911"></td>
        <td id="LC1911" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1912" class="blob-num js-line-number" data-line-number="1912"></td>
        <td id="LC1912" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1913" class="blob-num js-line-number" data-line-number="1913"></td>
        <td id="LC1913" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">CText</span>:</td>
      </tr>
      <tr>
        <td id="L1914" class="blob-num js-line-number" data-line-number="1914"></td>
        <td id="LC1914" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L1915" class="blob-num js-line-number" data-line-number="1915"></td>
        <td id="LC1915" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">text</span>, <span class="pl-smi">fontSize</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">font</span>, <span class="pl-smi">rot</span>, <span class="pl-smi">layer</span>):</td>
      </tr>
      <tr>
        <td id="L1916" class="blob-num js-line-number" data-line-number="1916"></td>
        <td id="LC1916" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1917" class="blob-num js-line-number" data-line-number="1917"></td>
        <td id="LC1917" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.text <span class="pl-k">=</span> text</td>
      </tr>
      <tr>
        <td id="L1918" class="blob-num js-line-number" data-line-number="1918"></td>
        <td id="LC1918" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.fontSize <span class="pl-k">=</span> fontSize</td>
      </tr>
      <tr>
        <td id="L1919" class="blob-num js-line-number" data-line-number="1919"></td>
        <td id="LC1919" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1920" class="blob-num js-line-number" data-line-number="1920"></td>
        <td id="LC1920" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1921" class="blob-num js-line-number" data-line-number="1921"></td>
        <td id="LC1921" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.layer <span class="pl-k">=</span> layer</td>
      </tr>
      <tr>
        <td id="L1922" class="blob-num js-line-number" data-line-number="1922"></td>
        <td id="LC1922" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.font <span class="pl-k">=</span> font</td>
      </tr>
      <tr>
        <td id="L1923" class="blob-num js-line-number" data-line-number="1923"></td>
        <td id="LC1923" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1924" class="blob-num js-line-number" data-line-number="1924"></td>
        <td id="LC1924" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#add to the total layout</span></td>
      </tr>
      <tr>
        <td id="L1925" class="blob-num js-line-number" data-line-number="1925"></td>
        <td id="LC1925" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell()</td>
      </tr>
      <tr>
        <td id="L1926" class="blob-num js-line-number" data-line-number="1926"></td>
        <td id="LC1926" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1927" class="blob-num js-line-number" data-line-number="1927"></td>
        <td id="LC1927" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1928" class="blob-num js-line-number" data-line-number="1928"></td>
        <td id="LC1928" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L1929" class="blob-num js-line-number" data-line-number="1929"></td>
        <td id="LC1929" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.chipText(<span class="pl-v">self</span>.coords, <span class="pl-v">self</span>.text, <span class="pl-v">self</span>.fontSize,</td>
      </tr>
      <tr>
        <td id="L1930" class="blob-num js-line-number" data-line-number="1930"></td>
        <td id="LC1930" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.font, <span class="pl-v">self</span>.layer, <span class="pl-v">self</span>.rot)</td>
      </tr>
      <tr>
        <td id="L1931" class="blob-num js-line-number" data-line-number="1931"></td>
        <td id="LC1931" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1932" class="blob-num js-line-number" data-line-number="1932"></td>
        <td id="LC1932" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1933" class="blob-num js-line-number" data-line-number="1933"></td>
        <td id="LC1933" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1934" class="blob-num js-line-number" data-line-number="1934"></td>
        <td id="LC1934" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">CrossArray</span>:</td>
      </tr>
      <tr>
        <td id="L1935" class="blob-num js-line-number" data-line-number="1935"></td>
        <td id="LC1935" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1936" class="blob-num js-line-number" data-line-number="1936"></td>
        <td id="LC1936" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">placeInfo</span>):</td>
      </tr>
      <tr>
        <td id="L1937" class="blob-num js-line-number" data-line-number="1937"></td>
        <td id="LC1937" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1938" class="blob-num js-line-number" data-line-number="1938"></td>
        <td id="LC1938" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1939" class="blob-num js-line-number" data-line-number="1939"></td>
        <td id="LC1939" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1940" class="blob-num js-line-number" data-line-number="1940"></td>
        <td id="LC1940" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1941" class="blob-num js-line-number" data-line-number="1941"></td>
        <td id="LC1941" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1942" class="blob-num js-line-number" data-line-number="1942"></td>
        <td id="LC1942" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1943" class="blob-num js-line-number" data-line-number="1943"></td>
        <td id="LC1943" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1944" class="blob-num js-line-number" data-line-number="1944"></td>
        <td id="LC1944" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1945" class="blob-num js-line-number" data-line-number="1945"></td>
        <td id="LC1945" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1946" class="blob-num js-line-number" data-line-number="1946"></td>
        <td id="LC1946" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1947" class="blob-num js-line-number" data-line-number="1947"></td>
        <td id="LC1947" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell()</td>
      </tr>
      <tr>
        <td id="L1948" class="blob-num js-line-number" data-line-number="1948"></td>
        <td id="LC1948" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L1949" class="blob-num js-line-number" data-line-number="1949"></td>
        <td id="LC1949" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1950" class="blob-num js-line-number" data-line-number="1950"></td>
        <td id="LC1950" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>):</td>
      </tr>
      <tr>
        <td id="L1951" class="blob-num js-line-number" data-line-number="1951"></td>
        <td id="LC1951" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.crossArray(<span class="pl-v">self</span>.coords)</td>
      </tr>
      <tr>
        <td id="L1952" class="blob-num js-line-number" data-line-number="1952"></td>
        <td id="LC1952" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1953" class="blob-num js-line-number" data-line-number="1953"></td>
        <td id="LC1953" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1954" class="blob-num js-line-number" data-line-number="1954"></td>
        <td id="LC1954" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">FourPoint</span>:</td>
      </tr>
      <tr>
        <td id="L1955" class="blob-num js-line-number" data-line-number="1955"></td>
        <td id="LC1955" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1956" class="blob-num js-line-number" data-line-number="1956"></td>
        <td id="LC1956" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1957" class="blob-num js-line-number" data-line-number="1957"></td>
        <td id="LC1957" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1958" class="blob-num js-line-number" data-line-number="1958"></td>
        <td id="LC1958" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Currently all options are hardcoded in fourPoint, </span></td>
      </tr>
      <tr>
        <td id="L1959" class="blob-num js-line-number" data-line-number="1959"></td>
        <td id="LC1959" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        but they are ready to be adapted to here</span></td>
      </tr>
      <tr>
        <td id="L1960" class="blob-num js-line-number" data-line-number="1960"></td>
        <td id="LC1960" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1961" class="blob-num js-line-number" data-line-number="1961"></td>
        <td id="LC1961" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#attributes</span></td>
      </tr>
      <tr>
        <td id="L1962" class="blob-num js-line-number" data-line-number="1962"></td>
        <td id="LC1962" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1963" class="blob-num js-line-number" data-line-number="1963"></td>
        <td id="LC1963" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1964" class="blob-num js-line-number" data-line-number="1964"></td>
        <td id="LC1964" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1965" class="blob-num js-line-number" data-line-number="1965"></td>
        <td id="LC1965" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1966" class="blob-num js-line-number" data-line-number="1966"></td>
        <td id="LC1966" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1967" class="blob-num js-line-number" data-line-number="1967"></td>
        <td id="LC1967" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L1968" class="blob-num js-line-number" data-line-number="1968"></td>
        <td id="LC1968" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L1969" class="blob-num js-line-number" data-line-number="1969"></td>
        <td id="LC1969" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1970" class="blob-num js-line-number" data-line-number="1970"></td>
        <td id="LC1970" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L1971" class="blob-num js-line-number" data-line-number="1971"></td>
        <td id="LC1971" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L1972" class="blob-num js-line-number" data-line-number="1972"></td>
        <td id="LC1972" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1973" class="blob-num js-line-number" data-line-number="1973"></td>
        <td id="LC1973" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1974" class="blob-num js-line-number" data-line-number="1974"></td>
        <td id="LC1974" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.fourPoint(<span class="pl-v">self</span>.coords, rot) </td>
      </tr>
      <tr>
        <td id="L1975" class="blob-num js-line-number" data-line-number="1975"></td>
        <td id="LC1975" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1976" class="blob-num js-line-number" data-line-number="1976"></td>
        <td id="LC1976" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#=========================================================================</span></td>
      </tr>
      <tr>
        <td id="L1977" class="blob-num js-line-number" data-line-number="1977"></td>
        <td id="LC1977" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#---------------------OXFORDIAN STRUCTURES--------------------------------</span></td>
      </tr>
      <tr>
        <td id="L1978" class="blob-num js-line-number" data-line-number="1978"></td>
        <td id="LC1978" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#=========================================================================</span></td>
      </tr>
      <tr>
        <td id="L1979" class="blob-num js-line-number" data-line-number="1979"></td>
        <td id="LC1979" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1980" class="blob-num js-line-number" data-line-number="1980"></td>
        <td id="LC1980" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1981" class="blob-num js-line-number" data-line-number="1981"></td>
        <td id="LC1981" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">ThinTenna</span>:</td>
      </tr>
      <tr>
        <td id="L1982" class="blob-num js-line-number" data-line-number="1982"></td>
        <td id="LC1982" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1983" class="blob-num js-line-number" data-line-number="1983"></td>
        <td id="LC1983" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>, <span class="pl-smi">placeInfo</span>, <span class="pl-smi">totLen</span>, <span class="pl-smi">thinLen</span>, <span class="pl-smi">thin</span>, <span class="pl-smi">tapLen</span>, <span class="pl-smi">preLen</span>, <span class="pl-smi">a1</span>, <span class="pl-smi">b1</span>, <span class="pl-smi">flip</span>, <span class="pl-smi">rot</span>):</td>
      </tr>
      <tr>
        <td id="L1984" class="blob-num js-line-number" data-line-number="1984"></td>
        <td id="LC1984" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1985" class="blob-num js-line-number" data-line-number="1985"></td>
        <td id="LC1985" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#attributes</span></td>
      </tr>
      <tr>
        <td id="L1986" class="blob-num js-line-number" data-line-number="1986"></td>
        <td id="LC1986" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.thin <span class="pl-k">=</span> thin</td>
      </tr>
      <tr>
        <td id="L1987" class="blob-num js-line-number" data-line-number="1987"></td>
        <td id="LC1987" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.preLen <span class="pl-k">=</span> preLen</td>
      </tr>
      <tr>
        <td id="L1988" class="blob-num js-line-number" data-line-number="1988"></td>
        <td id="LC1988" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.totLen <span class="pl-k">=</span> totLen</td>
      </tr>
      <tr>
        <td id="L1989" class="blob-num js-line-number" data-line-number="1989"></td>
        <td id="LC1989" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.thinLen <span class="pl-k">=</span> thinLen</td>
      </tr>
      <tr>
        <td id="L1990" class="blob-num js-line-number" data-line-number="1990"></td>
        <td id="LC1990" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.tapLen <span class="pl-k">=</span> tapLen</td>
      </tr>
      <tr>
        <td id="L1991" class="blob-num js-line-number" data-line-number="1991"></td>
        <td id="LC1991" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.a1 <span class="pl-k">=</span> a1</td>
      </tr>
      <tr>
        <td id="L1992" class="blob-num js-line-number" data-line-number="1992"></td>
        <td id="LC1992" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.b1 <span class="pl-k">=</span> b1</td>
      </tr>
      <tr>
        <td id="L1993" class="blob-num js-line-number" data-line-number="1993"></td>
        <td id="LC1993" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.flip <span class="pl-k">=</span> flip</td>
      </tr>
      <tr>
        <td id="L1994" class="blob-num js-line-number" data-line-number="1994"></td>
        <td id="LC1994" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.rot <span class="pl-k">=</span> rot</td>
      </tr>
      <tr>
        <td id="L1995" class="blob-num js-line-number" data-line-number="1995"></td>
        <td id="LC1995" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L1996" class="blob-num js-line-number" data-line-number="1996"></td>
        <td id="LC1996" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Decide if we have coordinates or connection</span></td>
      </tr>
      <tr>
        <td id="L1997" class="blob-num js-line-number" data-line-number="1997"></td>
        <td id="LC1997" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">type</span>(placeInfo) <span class="pl-k">==</span> <span class="pl-c1">str</span>:</td>
      </tr>
      <tr>
        <td id="L1998" class="blob-num js-line-number" data-line-number="1998"></td>
        <td id="LC1998" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its a connection: get the coordinates!</span></td>
      </tr>
      <tr>
        <td id="L1999" class="blob-num js-line-number" data-line-number="1999"></td>
        <td id="LC1999" class="blob-code blob-code-inner js-file-line">            comp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(sampleX, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L2000" class="blob-num js-line-number" data-line-number="2000"></td>
        <td id="LC2000" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.cp <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(comp, placeInfo.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L2001" class="blob-num js-line-number" data-line-number="2001"></td>
        <td id="LC2001" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#Adjust for size of device</span></td>
      </tr>
      <tr>
        <td id="L2002" class="blob-num js-line-number" data-line-number="2002"></td>
        <td id="LC2002" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.flip:</td>
      </tr>
      <tr>
        <td id="L2003" class="blob-num js-line-number" data-line-number="2003"></td>
        <td id="LC2003" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.totLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)),</td>
      </tr>
      <tr>
        <td id="L2004" class="blob-num js-line-number" data-line-number="2004"></td>
        <td id="LC2004" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.totLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L2005" class="blob-num js-line-number" data-line-number="2005"></td>
        <td id="LC2005" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2006" class="blob-num js-line-number" data-line-number="2006"></td>
        <td id="LC2006" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords <span class="pl-k">=</span> (<span class="pl-v">self</span>.cp[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.totLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(<span class="pl-v">self</span>.rot)),</td>
      </tr>
      <tr>
        <td id="L2007" class="blob-num js-line-number" data-line-number="2007"></td>
        <td id="LC2007" class="blob-code blob-code-inner js-file-line">                        <span class="pl-v">self</span>.cp[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.totLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(<span class="pl-v">self</span>.rot)))</td>
      </tr>
      <tr>
        <td id="L2008" class="blob-num js-line-number" data-line-number="2008"></td>
        <td id="LC2008" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2009" class="blob-num js-line-number" data-line-number="2009"></td>
        <td id="LC2009" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#its coordinates</span></td>
      </tr>
      <tr>
        <td id="L2010" class="blob-num js-line-number" data-line-number="2010"></td>
        <td id="LC2010" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">self</span>.coords <span class="pl-k">=</span> placeInfo</td>
      </tr>
      <tr>
        <td id="L2011" class="blob-num js-line-number" data-line-number="2011"></td>
        <td id="LC2011" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2012" class="blob-num js-line-number" data-line-number="2012"></td>
        <td id="LC2012" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2013" class="blob-num js-line-number" data-line-number="2013"></td>
        <td id="LC2013" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Connectors</span></td>
      </tr>
      <tr>
        <td id="L2014" class="blob-num js-line-number" data-line-number="2014"></td>
        <td id="LC2014" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectA <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.totLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)),</td>
      </tr>
      <tr>
        <td id="L2015" class="blob-num js-line-number" data-line-number="2015"></td>
        <td id="LC2015" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.totLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L2016" class="blob-num js-line-number" data-line-number="2016"></td>
        <td id="LC2016" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.connectB <span class="pl-k">=</span> (<span class="pl-v">self</span>.coords[<span class="pl-c1">0</span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.totLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.cos(rad(rot)), </td>
      </tr>
      <tr>
        <td id="L2017" class="blob-num js-line-number" data-line-number="2017"></td>
        <td id="LC2017" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">self</span>.coords[<span class="pl-c1">1</span>] <span class="pl-k">-</span> <span class="pl-v">self</span>.totLen<span class="pl-k">/</span><span class="pl-c1">2.</span><span class="pl-k">*</span>np.sin(rad(rot)))</td>
      </tr>
      <tr>
        <td id="L2018" class="blob-num js-line-number" data-line-number="2018"></td>
        <td id="LC2018" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2019" class="blob-num js-line-number" data-line-number="2019"></td>
        <td id="LC2019" class="blob-code blob-code-inner js-file-line">        <span class="pl-c">#Make the Cell</span></td>
      </tr>
      <tr>
        <td id="L2020" class="blob-num js-line-number" data-line-number="2020"></td>
        <td id="LC2020" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.makeCell(sampleX)</td>
      </tr>
      <tr>
        <td id="L2021" class="blob-num js-line-number" data-line-number="2021"></td>
        <td id="LC2021" class="blob-code blob-code-inner js-file-line">        sampleX.topCell.add(<span class="pl-v">self</span>.Cell)</td>
      </tr>
      <tr>
        <td id="L2022" class="blob-num js-line-number" data-line-number="2022"></td>
        <td id="LC2022" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2023" class="blob-num js-line-number" data-line-number="2023"></td>
        <td id="LC2023" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L2024" class="blob-num js-line-number" data-line-number="2024"></td>
        <td id="LC2024" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">makeCell</span>(<span class="pl-smi">self</span>, <span class="pl-smi">sampleX</span>):</td>
      </tr>
      <tr>
        <td id="L2025" class="blob-num js-line-number" data-line-number="2025"></td>
        <td id="LC2025" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2026" class="blob-num js-line-number" data-line-number="2026"></td>
        <td id="LC2026" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        make the cad Cell reference of the CPW</span></td>
      </tr>
      <tr>
        <td id="L2027" class="blob-num js-line-number" data-line-number="2027"></td>
        <td id="LC2027" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2028" class="blob-num js-line-number" data-line-number="2028"></td>
        <td id="LC2028" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>drawing a thinTenna!!!, it has a <span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.thin<span class="pl-k">/</span><span class="pl-c1">1e3</span>, <span class="pl-s"><span class="pl-pds">&#39;</span> um centerConductor<span class="pl-pds">&#39;</span></span> </td>
      </tr>
      <tr>
        <td id="L2029" class="blob-num js-line-number" data-line-number="2029"></td>
        <td id="LC2029" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">self</span>.Cell <span class="pl-k">=</span> md.thinTenna(<span class="pl-v">self</span>.coords,<span class="pl-v">self</span>.totLen, <span class="pl-v">self</span>.thinLen,</td>
      </tr>
      <tr>
        <td id="L2030" class="blob-num js-line-number" data-line-number="2030"></td>
        <td id="LC2030" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">thin</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.thin, <span class="pl-smi">tapLen</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.tapLen, <span class="pl-smi">preLen</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.preLen, </td>
      </tr>
      <tr>
        <td id="L2031" class="blob-num js-line-number" data-line-number="2031"></td>
        <td id="LC2031" class="blob-code blob-code-inner js-file-line">                <span class="pl-smi">a1</span> <span class="pl-k">=</span> <span class="pl-v">self</span>.a1, <span class="pl-smi">b1</span><span class="pl-k">=</span><span class="pl-v">self</span>.b1, <span class="pl-smi">rot</span><span class="pl-k">=</span><span class="pl-v">self</span>.rot)</td>
      </tr>
      <tr>
        <td id="L2032" class="blob-num js-line-number" data-line-number="2032"></td>
        <td id="LC2032" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L2033" class="blob-num js-line-number" data-line-number="2033"></td>
        <td id="LC2033" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2034" class="blob-num js-line-number" data-line-number="2034"></td>
        <td id="LC2034" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2035" class="blob-num js-line-number" data-line-number="2035"></td>
        <td id="LC2035" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#==========================================================================</span></td>
      </tr>
      <tr>
        <td id="L2036" class="blob-num js-line-number" data-line-number="2036"></td>
        <td id="LC2036" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#-------------------------------UTILITIES----------------------------------</span></td>
      </tr>
      <tr>
        <td id="L2037" class="blob-num js-line-number" data-line-number="2037"></td>
        <td id="LC2037" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#==========================================================================</span></td>
      </tr>
      <tr>
        <td id="L2038" class="blob-num js-line-number" data-line-number="2038"></td>
        <td id="LC2038" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L2039" class="blob-num js-line-number" data-line-number="2039"></td>
        <td id="LC2039" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">rad</span>(<span class="pl-smi">degrees</span>):</td>
      </tr>
      <tr>
        <td id="L2040" class="blob-num js-line-number" data-line-number="2040"></td>
        <td id="LC2040" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2041" class="blob-num js-line-number" data-line-number="2041"></td>
        <td id="LC2041" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    translates degrees to radians</span></td>
      </tr>
      <tr>
        <td id="L2042" class="blob-num js-line-number" data-line-number="2042"></td>
        <td id="LC2042" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2043" class="blob-num js-line-number" data-line-number="2043"></td>
        <td id="LC2043" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> degrees <span class="pl-k">*</span> <span class="pl-c1">2</span> <span class="pl-k">*</span> np.pi <span class="pl-k">/</span> <span class="pl-c1">360.</span></td>
      </tr>
      <tr>
        <td id="L2044" class="blob-num js-line-number" data-line-number="2044"></td>
        <td id="LC2044" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2045" class="blob-num js-line-number" data-line-number="2045"></td>
        <td id="LC2045" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2046" class="blob-num js-line-number" data-line-number="2046"></td>
        <td id="LC2046" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">arcrad</span>(<span class="pl-smi">radians</span>):</td>
      </tr>
      <tr>
        <td id="L2047" class="blob-num js-line-number" data-line-number="2047"></td>
        <td id="LC2047" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2048" class="blob-num js-line-number" data-line-number="2048"></td>
        <td id="LC2048" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    translates degrees to radians</span></td>
      </tr>
      <tr>
        <td id="L2049" class="blob-num js-line-number" data-line-number="2049"></td>
        <td id="LC2049" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2050" class="blob-num js-line-number" data-line-number="2050"></td>
        <td id="LC2050" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> radians <span class="pl-k">*</span> <span class="pl-c1">360</span> <span class="pl-k">/</span> <span class="pl-c1">2</span> <span class="pl-k">/</span> np.pi </td>
      </tr>
      <tr>
        <td id="L2051" class="blob-num js-line-number" data-line-number="2051"></td>
        <td id="LC2051" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>
      <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.22287s from github-fe123-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-808fcfcd63c9ecba3e84453f540cb1cbafde48c6b30c1d51ebd4e67e88ff66bd.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github/index-d235b6c3e48ba9782d3a995ac5332f39a20f29dbe928d28495d7299b2b32c25b.js"></script>
      
      
  </body>
</html>

