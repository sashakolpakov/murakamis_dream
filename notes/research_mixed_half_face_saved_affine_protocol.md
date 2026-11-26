# A saved-data test for the correlated half-face affine comparison

Analytic reduction and proposed protocol, 7 November 2026. This is an
unrun proposal. It uses the already certified following-reference sheet,
the saved circle root boxes and preconditioners, and the saved bare
prefix actions. No root, inclusion, Hessian, inverse, primitive, or
action is to be evaluated again.

The saved records do not separately contain \(g(q)\). We therefore keep
the existing elementary lower bound for its real halfweight. We do not
replace that missing value by a new finite dilogarithm calculation.
The proposed test can be inconclusive. No sign of its margins has been
evaluated or is asserted here. A checker, its independent reviews, a
frozen manifest, and the root's explicit execution instruction would
still be required before any numerical work.

## 1. The actual following coordinate and the four scalar tests

Use the original five-variable sheet of
[the following critical-curve theorem](research_mixed_three_four_following_critical_curve.md).
To match the saved data, write its coordinates as
\[
                 v(c)=(e(c),a(c),u(c),s(c),q(c)).
 \tag{1}
\]
The fourth and fifth coordinates are named t,z in the saved checker.
The external \(c\) is the input to this initial \(34\) half-chain.
For the actual next ordinary vertex it is \(s_3^*\), not the further
external coordinate \(s_4^*\); this is exactly the distinction in
[the allocated-action theorem, Section 1](research_mixed_next_allocated_action_floor.md).
Cover the two complete reduced disks
\[
 \begin{split}
 P_3&=\{|c-(7/20-i/100)|\le83/1000\},\\
 P_4&=\{|c-(3/10-13i/250)|\le3/50\}.
 \end{split}                                                     \tag{2}
\]
They contain the required \(O_3,O_4\), as well as the attached
following domains. The original root sheet is holomorphic on
neighborhoods of these full disks. Its two last coordinates lie
strictly in the proved own-four domain. All occurrences of
\(g',g''\) below use the original strip branches.

Let \(\mathscr P(c)\) denote the absolute bare \(34\) action after
removing the actual final Gram term, exactly as saved. Define
\[
 \begin{split}
 \mathscr F(c)&=\mathscr P(c)-\tfrac12 g(q(c)),\\
 h(c)&=g'(s(c)+q(c))-\tfrac32g'(q(c)),\\
 A(c)&=\Re\mathscr F(c),\qquad p(c)=\Re h(c).
 \end{split}                                                     \tag{3}
\]
Stationary differentiation of the original action gives
\[
             \mathscr F'(c)=h(c)q'(c).
 \tag{4}
\]
No source normalization, endpoint constant, or halfweight has
changed in (3).

The [scalar-envelope theorem](research_mixed_half_face_scalar_envelope_obstruction.md),
equations (18), supplies two affine costs at selected height
\(H=1/100\). Put
\[
 \widehat M=\frac{203}{200}-\frac{1303}{7680000},
       \qquad \bar c=\frac{73}{500}.
 \tag{5}
\]
The cap theorem proves \(M_{\rm half}<\widehat M\), and the unchanged
[endpoint seam majorants](research_mixed_endpoint_seam_majorants.md)
give \(c_0=-J(1/4)<\bar c\), since \(-4J(1/4)<73/125\).
Use the slightly larger, entirely specified costs
\[
 \begin{split}
 \bar L_{\rm fac}(x)&=\widehat M+\tfrac{11}{2}\bar c
       +\tfrac14\log2\,(x-\tfrac14)+\frac{\pi}{400}+\frac7{250},\\
 \bar L_{\rm force}(x)&=\widehat M+5\bar c
       +\tfrac12\log2\,(x-\tfrac14)+\frac{\pi}{100}+\frac7{250}.
 \end{split}                                                     \tag{6}
\]
Both alternatives are retained. In particular the selected halfweight
debit is \(3\pi H/4\), which leaves \(\pi H/4\) in the first line
after the conditional radius cost. These are upper costs, not
evaluated critical actions.

For \(j\in\{\mathrm{fac},\mathrm{force}\}\) define the exact deficit
\[
 D_{j,x}(c)=\bar L_j(x)-A(c)-p(c)(x-\Re q(c)).
 \tag{7}
\]
For each fixed \(c,j\), this is affine in \(x\). Therefore
\[
 \max_{11/50\le x\le9/20}D_{j,x}(c)
       =\max\{D_{j,11/50}(c),D_{j,9/20}(c)\}.
 \tag{8}
\]
There are exactly four tests: both displayed endpoints for both
Fourier alternatives. Negative upper bounds for these four deficits
on (2) would prove the actual half-face affine comparison, using
the full conditional plane already proved for either next type.
This would not pay a macroscopic first incoming arc or its vertical
join.

## 2. Exact angular transport and a full-disk barrier

Primes in this section mean derivatives with respect to the complex
external coordinate \(c\). Set
\[
 \begin{split}
 G_1(c)&=g''(s+q),\\
 G_2(c)&=g''(s+q)-\tfrac32g''(q).
 \end{split}
 \qquad
               h'=G_1s'+G_2q'.
 \tag{9}
\]
These require only elementary functions, since
\(g''(z)=\pi(\cot\pi z-i)\).
On a circle \(c(\theta)=c_\nu+\rho_\nu e^{i\theta}\),
write \(c_\theta=i(c-c_\nu)\). Direct differentiation of (7) and
(4) gives
\[
 \frac{dD_{j,x}}{d\theta}
   =\Re\{[-i\,\Im h\,q'-(x-\Re q)h']c_\theta\}.
 \tag{10}
\]
Indeed the \(p\,\Re(q'c_\theta)\) term cancels the real-\(h\) part
of \(\Re(hq'c_\theta)\). The remaining expression is independent
of the cost label \(j\). Its sign and this cancellation should be
retained in interval transport.

The Laplacian in the \(c\)-plane is also exact:
\[
                  \Delta D_{j,x}=2\Re(h'\overline{q'}).
 \tag{11}
\]
To see this, \(\Re\mathscr F\) and \(\Re h\) are harmonic, and
the only nonharmonic term is \((\Re h)(\Re q)\). Its Laplacian
is twice the dot product of their gradients.

Although (11) has no prescribed sign, it gives a useful finite
barrier. The function \(h'q'\) is holomorphic on a neighborhood of
each closed disk. Thus, if a complete boundary cover proves
\[
                 |h'(c)q'(c)|\le B_\nu
                                      \quad(c\in\partial P_\nu),
 \tag{12}
\]
the maximum-modulus principle gives the same bound throughout
\(P_\nu\). In particular \(\Delta D_{j,x}\ge-2B_\nu\).
Apply the subharmonic maximum principle to
\(D_{j,x}(c)+(B_\nu/2)|c-c_\nu|^2\). It proves
\[
 \boxed{\quad
 D_{j,x}(c)\le
   \max_{\partial P_\nu}D_{j,x}
      +\frac{B_\nu}{2}\{\rho_\nu^2-|c-c_\nu|^2\}
 \le \max_{\partial P_\nu}D_{j,x}
      +\frac{\rho_\nu^2B_\nu}{2}.
 \quad}                                                         \tag{13}
\]
The lower Laplacian bound, rather than an assumed subharmonicity of
\(D\), is what justifies the positive debit in (13). The holomorphic
product in (12) controls \(|h'||q'|\); no holomorphy is attributed to
\(h'\overline{q'}\).

## 3. Both response coordinates from the saved inclusion

The original boundary bank stores, for each circle cell, a rational
matrix \(Y_k\) and certified row bounds
\[
 E=I-Y_kH,\qquad \sum_j|E_{ij}|\le k_i,\qquad
                 k=\max_i k_i<1 .
 \tag{14}
\]
Here \(H\) is the original five-variable Hessian, and (14) holds
for all actual roots throughout that cell. All five \(k_i\), the
whole last column of \(Y_k\), and the uniform root boxes are saved.
No new Hessian enclosure or matrix inversion is needed.

Differentiating the original equations gives
\[
 Hv'=-\gamma e_4,\qquad
 \gamma=\frac{2\pi i}{1-e^{-2\pi iq}e^{-2\pi ic}},
 \tag{15}
\]
where \(e_4\) is the last coordinate in zero-based order. Let
\(m\) be the saved outward upper bound for
\(\max_i|(Y_k)_{i4}|\). Exactly as in the completed
[saved-response proof](research_mixed_three_four_following_saved_response_protocol.md),
\[
 v'=-\gamma Y_ke_4+Ev',\qquad
                \|v'\|_\infty\le\frac{|\gamma|m}{1-k}.
 \tag{16}
\]
It follows separately in rows \(3,4\) that
\[
 \begin{split}
 s'&=s'_0+\epsilon_s,\qquad
             s'_0=-\gamma(Y_k)_{34},\qquad
             |\epsilon_s|\le r_s:=\frac{|\gamma|k_3m}{1-k},\\
 q'&=q'_0+\epsilon_q,\qquad
             q'_0=-\gamma(Y_k)_{44},\qquad
             |\epsilon_q|\le r_q:=\frac{|\gamma|k_4m}{1-k}.
 \end{split}                                                     \tag{17}
\]
The completed response bank already contains an enclosure of
\(\gamma,q'_0,r_q\), along with \(k_i,k,m\) and the exact last
inverse column. These may be safely decoded and used directly.
Only \(s'_0,r_s\) need the new row-specific algebra in (17).
The two error disks are not asserted independent; the following
triangle inequalities are valid without such an assertion.

For example define
\[
 h'_0=G_1s'_0+G_2q'_0,\qquad
                 r_h=|G_1|r_s+|G_2|r_q.
 \tag{18}
\]
An outward bound for the holomorphic product needed in (12) is
\[
 |h'q'|
 \le |h'_0q'_0|+|h'_0|r_q+|q'_0|r_h+r_hr_q.
 \tag{19}
\]
All coefficients in this formula are enclosed on the saved whole-cell
root boxes. Take the maximum of the 512 outward upper endpoints in
each circle to define \(B_\nu\). This covers the whole boundary and
therefore proves (12), including the common cell endpoints.

For signed transport in (10), put
\[
 \begin{split}
 C_q&=-i\,\Im h-(x-\Re q)G_2,\\
 C_s&=-(x-\Re q)G_1 .
 \end{split}
 \tag{20}
\]
A valid real derivative enclosure is
\[
 \Re\{(C_qq'_0+C_ss'_0)c_\theta\}
 +[-|c_\theta|(|C_q|r_q+|C_s|r_s),
     |c_\theta|(|C_q|r_q+|C_s|r_s)].
 \tag{21}
\]
This retains the signed central response. It uses complex-disk error
radii directly and does not introduce a Cartesian-square
\(\sqrt2\) loss. Dependence among the boxed coefficients is forgotten
only outward.

## 4. The missing primitive value is replaced by a proved lower bound

The original action bank saves
\[
             \mathscr P(c_k),\quad
             \mathscr P(c_k)+G(q(c_k),c_k),\quad
             G(q(c_k),c_k)
 \tag{22}
\]
at each circle midpoint. It does not save \(g(q(c_k))\) separately.
The last two entries of (22) do not determine this missing primitive.
Consequently this protocol does not claim to decode \(A(c_k)\)
exactly from those actions.

For \(0<\Re q<1/2,\ \Im q<0\), the original
[Fourier-weight inequality (26)](research_mixed_fourier_weight_continuation.md)
instead gives
\[
 \frac{\nu(q)}2\ge
 \ell(q):=
 \frac{\sin(2\pi\Re q)}{4\pi}
                    \log(1+e^{2\pi\Im q}).
 \tag{23}
\]
This follows by integrating
\(\arg(1-te^{-i\theta})\ge t\sin\theta/(1+t)\); it is not
a new approximation to a dilogarithm. Both variables satisfy the
stated inequalities on the saved midpoint boxes.

At each midpoint use the conservative margin
\[
 \widetilde m_{j,x,k}
  =\Re\mathscr P(c_k)+\ell(q(c_k))
             +\Re h(c_k)(x-\Re q(c_k))-\bar L_j(x).
 \tag{24}
\]
It is a lower bound for the true midpoint margin
\(-D_{j,x}(c_k)\). The bare action is decoded from the saved
full lower/upper displays. The value of \(h(c_k)\) uses only
the original elementary logarithms on the saved midpoint boxes:
\[
 h=g'(s+q)-\tfrac32g'(q),\qquad
 g'(z)=\Log(2\sin\pi z)+\frac{i\pi}{2}(1-2z).
 \tag{25}
\]
No primitive in (22) is evaluated again.

Let \(L_{x,k}\) be the absolute upper bound of the real derivative
interval (21), and use the saved angular halfwidth
\(\omega=\pi/512\). Then
\[
 -D_{j,x}(c)\ge
       \underline{\widetilde m}_{j,x,k}-\omega L_{x,k}
              \qquad(c\hbox{ in cell }k).
 \tag{26}
\]
Combining the full circle inventory with (13), it suffices that
every one of the four comparisons in every cell of circle \(\nu\)
has strictly positive lower certificate
\[
 \boxed{\quad
 \underline{\widetilde m}_{j,x,k}
       -\omega L_{x,k}-\frac{\rho_\nu^2B_\nu}{2}>0.
 \quad}                                                         \tag{27}
\]
This is a finite saved-data calculation. If it succeeds, (8) and
(13) prove the full selected-\(x\) affine comparison throughout
both disks. If it fails, that is only insufficiency of these
conservative certificates. Even a strictly negative enclosure
of the proxy in (27) is not a disproof of the actual source
inequality.

## 5. Fixed proposed inventory and execution boundary

The inputs are the unchanged original boundary attempt

[boundary-cover-attempt01](../repro/results/research-mixed-three-four-following-boundary-cover-attempt01.json),
SHA256
e2a6f208dd59f9e2d8044619aa70532c7945972b8d499af3e00880f9e580449b,

and its completed saved-only response

[saved-response-attempt01](../repro/results/research-mixed-three-four-following-saved-response-attempt01.json),
SHA256
5bc3e5ff76ab5371e76bddb8d8fc32512ef16d9571d1991fb0c5f57dd39867c3.

Retain the exact 512 closed cells in each circle, with all type-three
cells followed by all type-four cells, in the original order. There
are 1,024 response/product enclosures and exactly 4,096 final
comparisons. The four comparisons within a cell have the fixed order
factorial at \(11/50\), factorial at \(9/20\), forcing at \(11/50\),
forcing at \(9/20\). The two angular-derivative enclosures may be
reused between cost labels, since (10) is independent of that label.
There is no subdivision, changed radius, root proposal, or replacement
of a failed cell.

A future standalone checker must first validate the full original
and response inventories, both inclusion-radius inventories, all
successful original inclusion checks, the recorded direct-inverse
failure in the old attempt, and all response checks and provenance.
Bind both manifests, both protocols/checkers, all inherited author and
replay records and their transitive dependency edges, together with
this note and every source used in (3), (6), (9), (13), and (23).
Check that the exact inverse column and cell identifiers agree in
the two banks. The old attempt remains failed; its successful
inclusions are used through their original proof, not promoted to
a successful direct interval inverse.

Use 256-bit outward ball arithmetic. Decode each saved lower and
upper display as a full ball, retaining any printed radius,
and take their union. Do not use the coarser display-only ball
field or a binary64 conversion. Parse saved rational quantities
exactly. Recheck the decoded contraction and inclusion inequalities
without recomputing their original gradients or Hessians. Maxima
of finite upper bounds are selected using exact dyadic endpoints.
All elementary logarithms and cotangents must retain the original
regular-strip checks; any decode or domain failure is recorded.

The only new permitted arithmetic is the fixed elementary formulas
(6), (9), (17)--(21), and (23)--(27), plus safe interval decoding and
provenance validation. In particular a finite Fourier or dilogarithm
series for \(\nu\), new action quadrature, recomputed Hessians,
matrix inverses, or altered response estimates are outside this
proposal. No preliminary evaluation of the proposed margins is
authorized.

The checker would have two deterministic arithmetic stages in a
single run: retain every cell's data and product bound (19), then
form the two finite maxima \(B_\nu\) and apply the fixed debit in
(27). A missing or failed cell leaves its entire circle uncertified;
it cannot be dropped from the maximum or from the final verdict.
Save every midpoint proxy, derivative interval, response center and
radius, product bound, circle maximum and witness, debit, final
certificate interval, check and exception. Preserve every
insufficient comparison, and list any unprocessed identifiers.

Use a distinct exclusive output and retain prefix failure records.
Rehash every input and the new manifest at completion. Any changed
input invalidates the result. Explicit counters for new roots,
inclusions, Hessians, inverses, actions, dilogarithms, source replays,
retries and subdivisions must all remain zero. A successful
conclusion requires all 4,096 strict positive certificates; otherwise
the conclusion is inconclusive for this proposed full-disk method.

No checker or manifest is supplied by this analytic note, and no
execution is authorized. Its proved content is the exact transport
and disk reduction, together with the identification of sufficient
saved fields. It makes no claim that the pending comparisons pass.
