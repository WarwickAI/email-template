import dataclasses


@dataclasses.dataclass
class Item:
  title: str
  subtitle: str
  content: str


@dataclasses.dataclass
class Email:
  title: str
  subtitle: str
  first_line: str
  announcement_title: str
  announcements: list[Item]
  events_title: str
  events: list[Item]
  footer: str


def generate(email: Email):
  result = generate_html(email)
  result = " ".join(result.split())
  result = result.replace("> <", "><")
  return result


def generate_html(email: Email):
  return (
      f"""
<!doctype html>
<html>
  {head(email)}
  <body>
    <div class="root">
      <table
        align="center"
        width="100%"
        style="margin: 0 auto; max-width: 800px; border-radius: 0"
        role="presentation"
        cellspacing="0"
        cellpadding="0"
        border="0"
      >
        <tbody>
          <tr style="width: 100%">
            <td>
              <div class="flex" style="padding-left: 16px; padding-right: 16px">
                <div class="logo" style="width: 100px; margin: auto 0">
                  <img src="https://raw.githubusercontent.com/WarwickAI/email-template/main/images/logo.svg" alt="logo"/>
                </div>
                <div>
                  <h1 style="padding-bottom: 0px">{email.title}</h1>
                  <h1 style="padding-top: 0px; padding-bottom: 0px">{email.subtitle}</h1>
                </div>
              </div>

              <div style="padding: 0px 0px 0px 0px">
                <table
                  align="center"
                  width="100%"
                  cellpadding="0"
                  border="0"
                  style="table-layout: fixed; border-collapse: collapse"
                >
                  <tbody style="width: 100%">
                    <tr style="width: 100%">
                      <td class="left-column" style="width: 100px"></td>
                      <td class="right-column">
                        <div class="normal-text" style="text-align: right">
                          {email.first_line}
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

              {large_divider()}
              <h2>{email.announcement_title}</h2>

              {items_to_list(email.announcements)}

              {large_divider()}

              <h2>{email.events_title}</h2>

              {items_to_list(email.events)}

              {large_divider()}

              <div class="normal-text" style="text-align: right">
                {email.footer}
              </div>

              {large_divider()}

              <!-- Footer -->
              <div style="padding: 16px 24px 16px 24px">
                <table
                  align="center"
                  width="100%"
                  cellpadding="0"
                  border="0"
                  style="table-layout: fixed; border-collapse: collapse"
                >
                  <tbody style="width: 100%">
                    <tr style="width: 100%">
                      <td class="left-column">
                        <div class="round-button">
                          <a href="https://warwick.ai" target="_blank">
                            <span>
                              <!--[if mso]>
                                <i
                                  style="
                                    letter-spacing: 20px;
                                    mso-font-width: -100%;
                                    mso-text-raise: 30;
                                  "
                                  hidden
                                  >&nbsp;</i
                                >
                              <![endif]-->
                            </span>
                            <span>Website</span>
                            <span>
                              <!--[if mso]>
                                <i
                                  style="
                                    letter-spacing: 20px;
                                    mso-font-width: -100%;
                                  "
                                  hidden
                                  >&nbsp;
                                </i>
                              <![endif]-->
                            </span>
                          </a>
                        </div>
                      </td>
                      <td class="right-column">
                        <div class="round-button">
                          <a
                            href="https://discord.gg/UmEEW37FKn"
                            target="_blank"
                          >
                            <span>
                              <!--[if mso]>
                                <i
                                  style="
                                    letter-spacing: 20px;
                                    mso-font-width: -100%;
                                    mso-text-raise: 30;
                                  "
                                  hidden
                                  >&nbsp;</i
                                >
                              <![endif]-->
                            </span>
                            <span>Discord</span>
                            <span>
                              <!--[if mso]>
                                <i
                                  style="
                                    letter-spacing: 20px;
                                    mso-font-width: -100%;
                                  "
                                  hidden
                                  >&nbsp;
                                </i>
                              <![endif]-->
                            </span>
                          </a>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>
"""
  )


def style():
  return (
      """
<style>
.large-divider {
  padding: 4px 0px 4px 0px;
}
.large-divider hr {
  width: 100%;
  border: none;
  border-top: 4px solid #6d60c1;
  margin: 0;
}

.small-divider {
  padding: 16px 80px 16px 80px;
}
.small-divider hr {
  width: 100%;
  border: none;
  border-top: 2px solid #6d60c1;
  margin: 0;
}

.round-button {
  text-align: center;
  padding: 16px 24px 16px 24px;
}
.round-button a {
  color: #ffffff;
  font-size: 16px;
  font-weight: bold;
  background-color: #6d60c1;
  border-radius: 64px;
  display: inline-block;
  padding: 12px 20px;
  text-decoration: none;
}

.left-column {
  box-sizing: content-box;
  vertical-align: middle;
  padding-left: 0;
  padding-right: 8px;
}
.right-column {
  box-sizing: content-box;
  vertical-align: middle;
  padding-left: 8px;
  padding-right: 0;
}
body {
  margin: 0;
  padding: 0;
  background-color: #e0e0e0;
}

a {
  text-decoration: none;
}

h1 {
  font-weight: bold;
  text-align: right;
  margin: 0;
  font-size: 32px;
  padding: 16px 0px 16px 16px;
}

h2,
h3 {
  font-weight: bold;
  margin: 0;
  padding: 16px 24px 0px 24px;
}
h2 {
  font-size: 24px;
}
h3 {
  font-size: 20px;
}

.location-text {
  font-weight: normal;
  font-style: italic;
  padding: 0px 24px 0px 24px;
}

.normal-text {
  font-weight: normal;
  padding: 16px 24px 16px 24px;
}

.root {
  color: #3c3c3c;
  padding-top: 64px;
  font-family: "Courier Prime", "Nimbus Mono PS", "Courier New", "Cutive Mono", monospace;
  font-size: 16px;
  font-weight: 400;
  letter-spacing: 0.15008px;
  line-height: 1.5;
  margin: 0;
  min-height: 100%;
  width: 100%;
}

.logo {
  padding: 0px;
}

.flex {
  display: flex;
  justify-content: space-between;
}

@media (max-width: 600px) {
  .root {
    font-size: 14px;
  }
  h1 {
    font-size: 24px;
  }
  h2 {
    font-size: 20px;
  }
  h3 {
    font-size: 16px;
  }
}

@media (max-width: 400px) {
  .root {
    font-size: 12px;
  }
  h1 {
    font-size: 20px;
  }
  h2 {
    font-size: 16px;
  }
  h3 {
    font-size: 12px;
  }
}

@media (prefers-color-scheme: dark) {
  body {
    background-color: #1a1a1a;
  }
  .root {
    color: #e0e0e0;
  }
  h1,
  h2,
  h3 {
    color: #ffffff;
  }
}
</style>
"""
  )


def head(email: Email):
  return (
      f"""
  <head>
    <title>{email.title}: {email.subtitle}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;1,400;1,700&display=swap" rel="stylesheet">
    <link href="https://raw.githubusercontent.com/WarwickAI/email-template/main/images/logo.svg" rel="preload" as="image">
    {style()}
  </head>
"""
  )


def small_divider():
  return """<div class="small-divider"><hr /></div>"""


def large_divider():
  return """<div class="large-divider"><hr /></div>"""


def item_template(item: Item):
  return (
      f"""
<h3>{item.title}</h3>
<div class="location-text">{item.subtitle}</div>
<div class="normal-text">
  {item.content}
</div>
"""
  )


def items_to_list(items: list[Item]):
  # For each item in the list, apply the item_template function, then join the
  # results together with a small divider
  return small_divider().join(map(item_template, items))
