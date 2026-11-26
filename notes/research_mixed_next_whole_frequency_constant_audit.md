# Quantitative constants in the cubic whole-frequency bound

Private static source audit and written bounds, 9 November 2026.
The adopted whole-frequency theorem has a positive coefficient in
terms of the single-vertex envelope constants. The existing source
proof does not assign numerical values to that complete complex
envelope triple. This note identifies its quantitative dependencies,
extracts a real angular coefficient, and gives a constructive
one-free-boundary strip formula in terms of a still unquantified
full-packet radius.

No mathematical numerical evaluation, saved-enclosure arithmetic,
certificate replay or frozen-source edit is used.

## 1. What the inherited statement specifies

Let \(Q_N(u)=P_{3,N}(0,u)\) be the full canonical inner source,
with \(M_3=\Re S_3(0,0)\). The
[single-vertex theorem, Theorem 1, equation (3)](research_all_nonzero_degree_two_fillings.md)
proves the existence of \(c_3,B_3,b_3>0\) with
\[
|Q_N(x+iy)|\le C N^A
 e^{N\{M_3-c_3(1-\cos x)+B_3y^2\}},
\qquad |x|\le\pi,\quad |y|\le b_3 .                                \tag{1}
\]
It does not specify a numerical admissible triple. Section 5
gives an explicit real-contour loss, then uses a local nonzero
packet and sufficiently small fixed complex neighborhoods.
The [scaled contour theorem, Section 7](research_scaled_wire_contour_lifting.md)
uses the same neighborhood argument.

The internal root radius \(2^{-100}\) in the
[degree-two certificate proof](research_internal_degree_two_contour_certificates.md)
is a Rouché radius for the complete internal root. It is not a
radius of an outgoing complex neighborhood on which the full
quantum packet has been bounded. Its certified complete-boundary
surface gaps likewise are not, without a perturbation estimate,
such an outgoing radius.

The coefficient \(1/100\) in the
[network boundary theorem](research_network_whole_boundary_decay.md)
cannot be imported as a cubic envelope constant: its Section 1
lists source classes with larger power or degree hypotheses.
Its Laurent argument is reusable, but those source hypotheses
do not include the isolated cubic vertex.

## 2. An explicit coefficient for the whole real period

There is nevertheless a written admissible real coefficient
\[
                              c_{\mathrm R}=\frac1{200}.
                                                                    \tag{2}
\]
More precisely, for some finite \(A\),
\[
|Q_N(x)|\le C N^A
       e^{N\{M_3-c_{\mathrm R}(1-\cos x)\}},
                          \qquad |x|\le\pi,                        \tag{3}
\]
through both level parities.

To verify this coefficient, the actual wire cutoffs in the
single-vertex proof are \(\alpha=1/32,\ \beta=15/32\).
Its equation (22), coming from
[the zero-safe factorial lemma, equation (6)](research_uniform_factorial_and_boundary_decay.md),
retains on every wire current the angular coefficient
\[
\gamma_{\mathrm{wire}}
 =\min_{\alpha\le\xi\le\beta}
      \frac{\sin(2\pi\xi)}{4\pi\cosh^2(\pi h_x)} .
                                                                    \tag{4}
\]
The original critical-point guard is
\(0<h_x<H_3/(2\pi)\). The
[cubic continuation](research_mixed_next_inner_three_cubic_continuation.md)
identifies this original branch and proves \(H_3<1\).
The elementary series bound
\(\cosh(1/2)<8/7\) is written in
[the complete-action estimate, equation (10)](research_inner_three_complete_action_upper_bound.md).
Concavity of sine gives \(\sin(\pi/16)\ge1/8\). Hence
\[
\gamma_{\mathrm{wire}}
 >\frac{49}{2048\pi}
 >\frac{49}{8192}
 >\frac1{200}.                                                     \tag{5}
\]
The last two comparisons use \(\pi<4\) and \(9800>8192\).
No saved root value was used.

The original discarded-wire rate has gap greater than \(1/4\)
by equation (17) of the single-vertex proof. Its discarded
angular rate is below \(8/5\), whereas the selected action is
greater than \(9/5\). These are uniform bounds for the original
finite source at all real free angles. Even with both free
angles present, the loss requested by (2) is at most
\(4c_{\mathrm R}=1/50<1/5\), so those discarded groups
retain a strict reserve. All retained groups have (5).
The original polynomial finite-source costs can therefore be
kept without decreasing (2). This proves (3).

This is a real-period bound. The number in (2) alone is not
an admissible triple for (1).

## 3. A constructive strip family and its missing input

Let \(r\) be any fixed radius satisfying
\[
0<r\le\frac14
\]
such that the original full nonzero packet
\[
Q_N(u)=C_{N,3}N^{-3/2}A(u)e^{NS(u)}
                              (1+O(N^{-1}))                       \tag{6}
\]
holds uniformly on a neighborhood of the closed disk
\(|u|\le r\), with \(A\) holomorphic and nonzero there.
The source theorem proves that some such radius exists.
It does not exhibit one quantitatively.

For every eligible \(r\), the following explicit replacements
are admissible for the one-free-boundary estimate (1):
\[
\boxed{\quad
c_3^{\mathrm a}=\frac1{400},\qquad
B_3^{\mathrm a}=\frac12+50\pi^2,\qquad
b_3^{\mathrm a}(r)
 =\min\left\{\frac r2,\frac{1-\cos(r/2)}{402}\right\}.
\quad}                                                            \tag{7}
\]
In particular these are formulas in an eligible full-source
radius, not a numerical certification of that radius.

We first record the required phase bound
\[
                         |S''(u)|<1,\qquad |u|\le1/4.              \tag{8}
\]
This uses the explicit original cubic phase, independently of
whether the finite packet has been proved on that whole disk.
Write \(v=2\cos(t_*(u)/2)\), \(c=v/2\). The cubic continuation
gives
\[
v^3-2iv^2-3v+2i-2\cos(u/2)=0,\qquad
\Re v>\frac32,\quad \frac13<\Im v<\frac23,\quad |c|<1,
\]
and
\[
S'(u)=-\frac1\pi\operatorname{arsinh}\{c(u)\tan(u/2)\}.             \tag{9}
\]
If \(\Delta=3v^2-4iv-3\), then
\[
\Re\Delta
 =3(\Re v)^2-3(\Im v-2/3)^2-\frac53>\frac{19}{4},
\qquad c'=-\frac{\sin(u/2)}{2\Delta}.                              \tag{10}
\]
For \(|u|\le1/4\), the absolute sine series, the positive
hyperbolic-sine series and the cosine bound give
\[
|\sin(u/2)|\le\sinh(1/8)
 \le\frac{1/8}{1-1/384}=\frac{48}{383}<\frac17,\qquad
|\cos(u/2)|\ge\cos(1/8)\ge\frac{127}{128}.
\]
Thus \(|\tan(u/2)|<1/6\), \(|\sec^2(u/2)|<4/3\), and
\(|c'|<1/4\). Set \(w=c\tan(u/2)\). Then
\[
|w|<\frac16,\qquad
|w'|<\frac1{24}+\frac23<\frac34,\qquad
|1+w^2|^{1/2}>\frac56 .
\]
The original principal branch in (9) consequently yields
\(|S''|<9/(10\pi)<1\), proving (8).

For real \(|x|\le r\), the nonzero packet (6) and (3)
imply, by taking the exponential rate,
\[
                 \Re S(x)\le M_3-c_{\mathrm R}(1-\cos x).
                                                                    \tag{11}
\]
Evenness gives \(S'(0)=0\), and (8) gives
\(|S'(x)|\le|x|\). If \(|x|,|y|\le r/2\), vertical
Taylor expansion stays in \(|u|\le r\), and gives
\[
\Re S(x+iy)\le
M_3-c_{\mathrm R}(1-\cos x)+|xy|+\frac{y^2}{2}.
\]
Use \(1-\cos x\ge2x^2/\pi^2\) and Young's inequality
on half the real angular loss. The result is
\[
\Re S(x+iy)\le
 M_3-\frac{c_{\mathrm R}}2(1-\cos x)
             +\left(\frac12+\frac{\pi^2}{4c_{\mathrm R}}\right)y^2 .
                                                                    \tag{12}
\]
The bounded exact packet multiplier in (6) transfers (12)
to the full finite source on this local rectangle.

For completeness, the rest of the period has an explicit
continuation estimate. Write \(z=e^{iu}\); the even Laurent
polynomial \(Q_N(z)\) has degrees between \(-D\) and \(D\).
The function
\[
                  z^D Q_N(z)e^{-Nc_{\mathrm R}z}
\]
is holomorphic on the unit disk. Its boundary norm is at most
\(CN^A e^{N(M_3-c_{\mathrm R})}\) by (3).
The maximum principle and evenness therefore give, with
\(s=|y|\),
\[
|Q_N(x+iy)|
\le CN^A\exp N\{M_3-c_{\mathrm R}
                      +c_{\mathrm R}e^{-s}\cos x+s\}
\le CN^A\exp N\{M_3-c_{\mathrm R}(1-\cos x)
                                      +(1+c_{\mathrm R})s\}.
                                                                    \tag{13}
\]
This is the exact Laurent mechanism in Section 4 of the
network boundary proof; only its elementary polynomial
argument, not its source-specific coefficient, is used.

If \(|x|\ge r/2\) and
\[
s\le\frac{c_{\mathrm R}(1-\cos(r/2))}
                              {2(1+c_{\mathrm R})}
 =\frac{1-\cos(r/2)}{402},
\]
the last positive term in (13) is at most half the real
angular loss. Thus (13) gives (1) outside the local interval
with coefficient \(c_{\mathrm R}/2\), even without its
positive quadratic allowance. Combining this with (12) and
(6) proves exactly (7), through both parities.

## 4. What would quantitatively settle the comparison

For the explicit family (7), the
[whole-frequency theorem](research_full_single_vertex_whole_frequency_cosine_bound.md)
gives the admissible response coefficient
\[
\boxed{\quad
\gamma_{3,3}(r)
 =\min\left\{\frac{b_3^{\mathrm a}(r)}2,\,
                    \frac1{902+200\pi^2},\,\frac1{1600}\right\}.
\quad}                                                            \tag{14}
\]
If a specific \(r_0>0\) is proved eligible for the full
packet, (14) is an explicit positive admissible lower
bound for the coefficient one may use. Until then it is
a constructive dependence on an existential radius. The
phase's larger analytic rectangle, a root-isolation radius,
or an arbitrarily chosen small number cannot supply this
missing full-source eligibility.

The [adopted outgoing action loss](research_mixed_next_outgoing_sharper_tail_and_ellipse.md)
states
\[
\mathcal E(1/2+t,Z)\le \mathcal E(1/2,Z)-c_0t,
\qquad 0\le t\le1/2,\qquad c_0=\frac{205}{1134}.                   \tag{15}
\]
Let \(E_0(Z)=\mathcal E(1/2,Z)\) and
\(\mathcal X(Z)=M_3+E_0(Z)-\Lambda(Z)\).
For any \(0<\gamma\le c_0\), (15) proves the exact
variational identity
\[
\max_{0\le t\le1/2}
 \left\{M_3+\mathcal E(1/2+t,Z)
                              -\gamma(1/2-t)^2-\Lambda(Z)\right\}
                         =\mathcal X(Z)-\frac\gamma4 .             \tag{16}
\]
Indeed the expression is bounded above by
\(\mathcal X-c_0t-\gamma(1/2-t)^2\); this quadratic is
nonincreasing on \([0,1/2]\) because its derivative is
\(\gamma-c_0-2\gamma t\le0\). At \(t=0\) the upper
bound is attained by the original expression.

The coefficient (14) satisfies
\(\gamma_{3,3}(r)\le1/1600<c_0\). Consequently this
particular whole-frequency criterion is equivalent to
\[
                       \mathcal X(Z)<\frac{\gamma_{3,3}(r)}4 .
                                                                    \tag{17}
\]
Positive input rate tolerances require a corresponding
strict reserve in (17). On an actual compact reference
family, a uniform strict inequality is required.

Two distinct pieces of evidence would establish (17):

* an explicit eligible full-packet radius, or another
  quantitatively proved complex-envelope triple;
* a sufficiently sharp original-action comparison for
  \(\mathcal X\), on the actual reference family.

The existing statements read here do not establish this
comparison. A future certificate would need its own frozen
protocol and original action/branch normalization; no such
evaluation is performed or inferred here. Conversely,
failure of (17) for the conservative family (7) would not
exclude a sharper envelope, a sharper response theorem,
or cancellation in the actual complete observation.

## 5. Frozen source bindings

| Source | SHA-256 |
|---|---|
| Full single-vertex theorem | 7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c |
| Uniform factorial and real angular loss | 4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11 |
| Scaled contour source theorem | b1a9429031499098756b725757f54c46b7fdaa4033845f1dc56fa162ec80aa10 |
| Degree-two certificate proof | 954ff66b16b74aaa24a107cd2184a774ec7a0f97acf7d58d8f8aabd1a58288ec |
| Cubic phase continuation | 8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a |
| Complete-action estimate | 7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d |
| Network boundary theorem and Laurent argument | 962ea7b42aaba6ef356209c012a0df222102523ece088d60c04e83bbd67e31e1 |
| Whole-frequency observation | 24ed707af29a5a15e5f2302210ae492d8256c5b5548145dce31de19dbbd2c489 |
| Original outgoing action loss | fab5571d039f9fa4e36c0b6ca981f4ebbd2e7384923249882cf22e58eccc8ba3 |
