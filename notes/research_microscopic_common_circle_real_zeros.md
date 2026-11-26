# Actual real zeros at a microscopic common-circle insertion

Private written proof, 16 November 2026.

Uniform polynomial lower bounds do not hold for the whole upper-packet
class, even for a common zero-power filling of sufficiently many bare
edges and one microscopic insertion. The original scalar is real for
real marks. Its actual leading coefficient oscillates through both
signs, so the complete finite trace has real zeros at bounded
level-dependent marks.

This is a statement about a family of original sources, not a knot
classification or a geometric filling counterexample. A separate
corollary constructs a fixed real mark with very small subsequences;
it makes no assertion about prescribed algebraic or discrete marks.

## 1. The exact real source and its common saddle

Put \(h=N^{-1}\), \(\eta=(-1)^{N-1}\), and retain
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_k(C)=S_k^{-2}\prod_{j<k}(c_j-C),\qquad
 S_k=\prod_{\ell=1}^k2\sin(\pi\ell/N),
\]
\[
 K_N(C,Z)=\sum_{k=0}^{N-1}e_k(C)e_k(Z),\qquad
 w_N(\alpha)=2\cosh(\alpha/N).
 \tag{1}
\]
The original full trace is
\[
 \phi_N(f)=\eta\sum_{j<\lfloor N/2\rfloor}
       \{(4-c_j^2)f'(c_j)-c_jf(c_j)\}
              +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{2}
\]
Fix an integer \(m\) sufficiently large for the upper-packet
composition theorem with incoming bare edges and one microscopic
factor. In particular take its explicit threshold after fixing a
small fold cap and its sharp repair saving. The number \(m\) is fixed
before \(N\) varies. The actual scalar is
\[
 Z_{N,m}(\alpha)=
 \phi_N^{(C)}\!\left[
 K_N(w_N(\alpha),C)\,K_N(C,-2)^m\right].
 \tag{3}
\]
The central crossing power is exactly zero. No first normal or
simple-node value is removed from (3). Every coefficient in (1)--(2)
is real. Consequently (3) is a real polynomial in \(w_N(\alpha)\)
for real \(\alpha\), is continuous there, and is an even entire
function of \(\alpha\).

The bare-edge packet has, on its fixed complete chart,
\[
 K_N(-2\cos t,-2)=N^{-3/2}a(t)e^{N\psi(t)}[1+O_{\rm hol}(N^{-1})],
 \qquad a(t)\ne0 ,
 \tag{4}
\]
with the original phase normalization
\[
 \psi'(t)=-\pi^{-1}\operatorname{asinh}(\tan(t/2)),
 \qquad
 \psi(0)=\frac4\pi\int_0^{\pi/4}\log\cot s\,ds .
 \tag{5}
\]
The complete bare-edge theorem also supplies the whole-period
upper envelope required by the composition theorem.

The selected common phase is
\[
 \Phi_m(t)=m\psi(t)-it.
 \tag{6}
\]
Its critical point is purely imaginary:
\[
 t_*=-iH_m,\qquad
 \tanh(H_m/2)=\sin(\pi/m),\qquad H_m>0 .
 \tag{7}
\]
Indeed \(\operatorname{asinh}(\tan(-iH/2))
=-i\arcsin(\tanh(H/2))\), on the original strip, so
\(\Phi_m'(-iH)=0\) is precisely (7).
The high-curvature threshold places this point and its buffered
horizontal neighborhood inside the chart of (4). Write
\[
 M_m=\Phi_m(t_*)=m\psi(-iH_m)-H_m\in\mathbb R,\qquad
 \lambda_m=-\Phi_m''(t_*)
             =\frac{m}{2\pi\cosh(H_m/2)}>0 .
 \tag{8}
\]
The amplitude at this saddle is positive. In fact for
\(C=-2\cosh H_m<-2\), every \(e_k(C)\) is positive and every
\(e_k(-2)\) is nonnegative; at least the \(k=0\) term is positive.
Thus the exact kernel in (4) is positive. The phase in (4) is
real there and the nonzero limit defining \(a(t_*)\) is positive.
Define the fixed positive constant
\[
 D_m=\sqrt{\frac2\pi}\,
       \frac{\sinh H_m\,a(t_*)^m}{\sqrt{\lambda_m}}>0,
 \qquad
 s_m=\frac{\cosh(H_m/2)}{\pi}>0.
 \tag{9}
\]

## 2. The actual coefficient formula at the centered fold

For \(\nu=\alpha/\pi\ne0\), put
\[
 k_\pm(\nu)=
 \frac{\Gamma(\pm i\nu)}
      {\Gamma(1/2\pm i\nu/2)^4},\qquad
 g_\alpha(S)=k_+S^{-1+i\nu}+k_-S^{-1-i\nu}.
 \tag{10}
\]
At zero use its removable real combination:
\[
 g_0(S)=\frac{2}{\pi^2S}
                \{\log S+\gamma_E+4\log2\}.
 \tag{11}
\]
The logarithm is real for \(S>0\).

The actual fold baseline \(V_N\) is the one with cutoff
\(\lfloor N/4\rfloor\) and the two original physical anchor values
specified in the fold theorem. Its scalar coordinate is
\[
 C_N(x)=2\cos(2\pi x+\pi h),\qquad
 t=\pi-2\pi x-\pi h .
 \tag{12}
\]
The relevant point is
\[
 x_*=\frac{1-h}{2}+\frac{iH_m}{2\pi},\qquad
 \sin\bigl(\pi(x_*+h/2)\bigr)=\cosh(H_m/2).
 \tag{13}
\]
It is important that its centered real part is exactly \(1/2\).
The nonreal unequal-mode lower bound is not applicable here.

Nevertheless the actual coefficient formula extends to this point:
for every bounded real parameter interval there is \(\epsilon>0\)
such that
\[
 V_N(x,\alpha)=
 g_\alpha\!\left(\frac N\pi
                   \sin\bigl(\pi(x+h/2)\bigr)\right)
                    +O_{\rm hol,x}(N^{-1-\epsilon})
 \tag{14}
\]
on a fixed neighborhood of \(x_*\).
All fixed spatial derivatives are included. In particular,
\[
 V_N(x_*,\alpha)=g_\alpha(Ns_m)+O(N^{-1-\epsilon}),\qquad
 |\partial_x^qV_N|\le C_q(1+\log N)/N.
 \tag{15}
\]
Here and below uniformity includes real parameters depending on \(N\).

We justify this extension, rather than continuing a pointwise error
from the left half of the fold. Choose a fixed reference interval
strictly between \(1/4\) and \(1/2\), close enough to the fold that
\(I_{1/4}\) is positive on a larger fixed real buffer. Choose one
physical reference \(x_b=j_b/N\) in that interval at every level.
On that buffer the actual connection theorem gives the
two-value balanced state with error \(O(N^{-1-\epsilon})\).
Its explicit leading coefficients in the coalesced sine basis
have norm between \(c/N\) and \(C(1+\log N)/N\), uniformly through
\(\alpha=0\).

For cutoff \(1/4\) the fold modes have the same centered expansion
\[
 H_{0,N}=
 \frac{\cos(\nu\log\sin\pi(x+h/2))}{\sin\pi(x+h/2)}
       +O_{\rm hol}(h^2),\qquad
 H_{1,N}=
 \frac{\sin(\nu\log\sin\pi(x+h/2))}
      {\nu\sin\pi(x+h/2)}
       +O_{\rm hol}(h^2).
 \tag{16}
\]
The second quotient is removable at zero. The fold source proves
these estimates on a symmetric buffered rectangle through \(1/2\)
at any fixed height; the two modes have a uniformly invertible
divided-color frame there. At \(x_b\) its balanced value frame is
also uniformly invertible. Comparing the actual two anchor values
with (16) therefore gives the same Gamma coefficients as in (10),
with error \(O(N^{-1-\epsilon})\). The shift from \(x\) to \(x+h/2\)
changes their comparison by at most \(O((1+\log N)/N^2)\).

Finally compare that reference normalization with the actual fold
anchor. The exact coefficient recurrence at physical rows has
increment bounded by a polynomial times \(e^{-NI_{1/4}(x_j)}\).
The action increases towards the fold, so summing from \(x_b\)
to the fold changes the actual coefficient vector exponentially.
This is the source-specific anchor comparison of the fold proof;
it imposes no additional normal at the odd simple node.
Multiplying the resulting coefficient vector by the bounded modes
on the tall rectangle proves (14), including derivatives by the
same explicit mode estimates. This also explains why the vanishing
angular Wronskian at the real fold does not enter the argument.

Let \(H_N^+\) be the exact designated-half representative on this
cap. The fold theorem gives \(H_N^+-V_N=O(N^p e^{-\gamma N})\)
with fixed spatial derivatives there, for some \(\gamma>0\).
Thus (14)--(15) hold with \(H_N^+\) as well. These are statements
about a representative of the original full jets, not about the
canonical polynomial at nonphysical colors.

## 3. The whole scalar, including its complements

There is a uniform absolute asymptotic
\[
 \boxed{\quad
 Z_{N,m}(\alpha)=
 D_m N^{3(1-m)/2}e^{NM_m}
        \{g_\alpha(Ns_m)+O(N^{-1}\varepsilon_N)\},
 \qquad \varepsilon_N\longrightarrow0 ,
 \quad}
 \tag{17}
\]
on every bounded real parameter interval. One may take
\[
 \varepsilon_N=C\{N^{-\epsilon}+(1+\log N)/\sqrt N\}.
 \tag{18}
\]
No division by a potentially zero microscopic factor is made.

Here is the full-source argument. Apply the exact mirror-normalized
fold identity to the microscopic insertion, retaining
\(K_N(C,-2)^m\) as the actual received spectator and the central
power zero. Its two reflected favored local integrals add. The
sine changes sign under reflection and so does the differential;
the two half-prefactors recover exactly
\[
 \frac{iN^2}{\pi}
 \int_{-a}^{a}
 \sin t\,K_N(-2\cos t,-2)^m H_N^+(x(t),\alpha)
       \frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,ds,
 \qquad t=t_*+s .
 \tag{19}
\]
This normalization also applies when the real part of \(t_*\)
is zero. The two contributing points lie on the distinct lower
and upper half-contours; their addition does not introduce another
factor two.

All other currents have a fixed strict gap below \(M_m\). More
explicitly, the upper composition proof bounds the original outer
physical rows using the received whole-period decay and polynomial
microscopic physical jets. The two baseline vertical sides have
strictly smaller real and top endpoint rates, and convexity bounds
their complete integrals. Both baseline horizontals away from
the selected neighborhoods have a strict gap by real concavity.
The designated corrections are exponentially small. The real
interface has rate at most
\[
 m\psi(0)-\gamma
          \le M_m+L_*/m-\gamma<M_m ,
 \tag{20}
\]
by the explicit enlarged threshold. Every rational alias of (19)
other than its selected character loses the fixed positive height
\(H_m\). Thus the complete source differs from (19) by
\(O(N^p e^{N(M_m-c)})\) for some \(c>0\), uniformly on the
parameter compact. Every original first normal, odd simple value,
vertical side, interface and alias is still accounted for.

In (19), substitute (4), retaining its \(m\) actual factors, and
replace the rational denominator by one with its exponentially
small error. The phase is (6); the normalized bare amplitude is
bounded with fixed derivatives and has a nonzero value at \(t_*\).
The microscopic representative and its first derivative are
\(O((1+\log N)/N)\) on the fixed local neighborhood by (15).
Taylor subtraction of its value at \(t_*\), followed by the
absolute Gaussian bound, therefore costs
\[
 O\!\left(N^{3(1-m)/2}e^{NM_m}
                   \frac{1+\log N}{N\sqrt N}\right).
 \tag{21}
\]
The ordinary local phase and bare-amplitude Gaussian errors have
the same or a smaller bound. Equation (14) replaces its saddle
value with \(g_\alpha(Ns_m)\), with error \(O(N^{-1-\epsilon})\).
The exact factor \(i\sin t_*=\sinh H_m\), the Gaussian
\(\sqrt{2\pi/(N\lambda_m)}\), and the powers
\(N^2N^{-3m/2}N^{-1/2}\) give exactly the positive constant
and power in (17). The exponentially smaller complements are
absorbed in (18). This proves the asserted uniform absolute
formula at both parities.

## 4. Exact real zeros and failure of a uniform lower bound

**Theorem.** For every \(0<a<b<\infty\), the exact scalar
\(Z_{N,m}\) has a real zero in \((a,b)\) for every sufficiently
large integer \(N\). This holds separately along either level
parity. More precisely its number of sign-changing zero intervals
in any such fixed interval tends to infinity.

For \(\nu>0\), choose a continuous argument
\(\vartheta(\nu)=\arg k_+(\nu)\) on
\([a/\pi,b/\pi]\). The Gamma factors are nonzero, so this argument
is smooth with bounded derivative there. Real parameters satisfy
\(k_-=\overline{k_+}\), and hence
\[
 g_\alpha(Ns_m)=
 \frac{2|k_+(\alpha/\pi)|}{Ns_m}
       \cos\Theta_N(\alpha),\qquad
 \Theta_N(\alpha)=\frac{\alpha}{\pi}\log(Ns_m)
                        +\vartheta(\alpha/\pi).
 \tag{22}
\]
Uniformly on \([a,b]\),
\[
 \Theta_N'(\alpha)=\pi^{-1}\log(Ns_m)+O(1)>0
 \tag{23}
\]
for large \(N\), and the range length tends to infinity.
There are therefore successive interior points where the cosine
is \(+1,-1,+1,\ldots\). At these points its coefficient in (22)
has modulus at least \(c/N\), uniformly. The error in (17) is
\(o(1/N)\), and its outside prefactor is positive. Thus the
actual real scalar has the corresponding alternating signs.
The intermediate value theorem gives an exact zero between each
successive pair. The proof is uniform through all sufficiently
large levels and does not use a parity subsequence.

In particular no estimate
\[
 |Z_{N,m}(\alpha)|\ge N^{-p}e^{NM_m}
 \tag{24}
\]
with finite \(p\) can hold uniformly over arbitrary bounded real,
level-dependent marks, even if the allowed compact contains zero.
Its failure is not a failure of the input source bounds or of the
nonzero microscopic germ: it occurs in the original scalar closing.
Keeping finitely many amplitude jets cannot establish (24) on
this full class, because its exact scalar has the zeros just proved.
This statement does not say that every Gaussian expansion
coefficient vanishes at one fixed parameter independently of \(N\).
Indeed, at any of the exact zeros in a fixed positive compact,
(17),(22) imply \(\cos\Theta_N=o(1)\). Differentiating (14) in
the angular variable, using
\(S_N(t)=(N/\pi)\cos(t/2)\), gives there
\[
 \partial_tH_N^+(x(t_*),\alpha)=
 -\frac{i\nu|k_+(\nu)|\tanh(H_m/2)}{Ns_m}
                  \sin\Theta_N(\alpha)+o(N^{-1}).
 \tag{24a}
\]
Its modulus is bounded below by \(c/N\). Thus even an actual
nonzero first amplitude jet can coexist with an exactly zero
original scalar.

**Corollary (marks tending to zero).** For every sufficiently large
level one can choose an exact real zero \(\alpha_N>0\) of (3) such that
\[
                    \alpha_N\log N\longrightarrow\pi^2 .
 \tag{24b}
\]
The conclusion holds at both parities. In particular merely requiring
the continuous mark to converge to zero does not give a uniform lower
bound; the value at the mark exactly zero remains positive to leading
order by (11),(17).

To prove this, put \(L=\log N\) and \(\alpha=c/L\). The uniform
coalescence expansion of (10) gives, on every bounded real \(c\)-interval,
\[
 \frac N{L}\,g_{c/L}(Ns_m)\longrightarrow
       \frac{2\sin(c/\pi)}{\pi c s_m},
 \tag{24c}
\]
with removable value \(2/(\pi^2s_m)\) at \(c=0\). Indeed
\(k_+(\nu)=-i/(\pi^2\nu)+O(1)\), with its conjugate for \(k_-\);
the singular terms combine into
\(2\sin(\nu\log(Ns_m))/(\pi^2\nu Ns_m)\).
Their removable combination and the bounded remainder make this
limit uniform through \(c=0\). The error in (17), multiplied by
\(N/L\), tends to zero as well.

For each fixed \(0<\delta<\pi^2\), the right side of (24c) is positive
at \(c=\pi^2-\delta\) and negative at \(c=\pi^2+\delta\).
The actual source therefore has a zero between the corresponding
marks for every sufficiently large \(N\). Choose
\(\delta_k\downarrow0\) and increasing starting levels so these two
signs hold for all subsequent levels at the \(k\)-th bracket.
Use that bracket until the next starting level, and choose one of
its exact zeros. This diagonal choice proves (24b), without a
subsequence or a parity restriction.

## 5. A fixed real mark with different lower and upper subsequences

The preceding result also has a separate fixed-mark consequence.
First, for each fixed \(\alpha>0\),
\[
        \limsup_{N\to\infty}N^{-1}\log|Z_{N,m}(\alpha)|=M_m.
 \tag{25}
\]
The upper inequality follows from the actual complex-parameter
upper packet bound. For the other inequality let
\(\nu=\alpha/\pi\), \(\vartheta=\vartheta(\nu)\), and choose
integers \(N_k\) of either prescribed parity nearest to
\[
       s_m^{-1}\exp((2\pi k-\vartheta)/\nu).
 \tag{26}
\]
The logarithmic rounding error is \(O(N_k^{-1})\), so
\(\cos\Theta_{N_k}(\alpha)\to1\). Equations (17)--(22) give a
positive polynomial multiple of \(e^{N_kM_m}\), proving (25).
At \(\alpha=0\), (11),(17) instead give a positive leading
\((\log N)/N\) factor and the ordinary rate limit \(M_m\).

**Corollary.** In every interval \((a,b)\) with \(0<a<b\) there
exists one fixed real \(\alpha_*\) such that
\[
 \liminf_{N\to\infty}N^{-1}\log|Z_{N,m}(\alpha_*)|=-\infty,
 \qquad
 \limsup_{N\to\infty}N^{-1}\log|Z_{N,m}(\alpha_*)|=M_m.
 \tag{27}
\]
We use \(\log0=-\infty\).

Choose a compact interval inside \((a,b)\). The actual upper
composition bound holds on a fixed larger complex parameter set,
with phase \(M_m\) independent of that parameter. Cauchy's formula
therefore gives
\[
             |\partial_\alpha Z_{N,m}(\alpha)|
                          \le CN^p e^{NM_m}
 \tag{28}
\]
on that compact interval.
Inductively choose increasing levels \(N_k\), of one prescribed
parity if desired, and a zero \(\alpha_k\) in the interior of
the previous closed interval. The theorem permits this at every
sufficiently large future level. Around \(\alpha_k\) choose a
nondegenerate closed interval \(I_k\) contained in that interior,
of radius at most \(e^{-N_k^2}\). Their nested intersection is a
single point \(\alpha_*\) in \((a,b)\). By (28),
\[
 |Z_{N_k,m}(\alpha_*)|
       \le CN_k^p e^{N_kM_m-N_k^2}.
 \tag{29}
\]
This proves the lower-subsequence assertion. The fixed positive
mark result (25) proves its upper-subsequence assertion.
No rational-approximation property of \(\alpha_*\) is claimed.

## 6. Scope, coverage and direct sources

The old nonreal insertion theorem separates the two modal
magnitudes when the imaginary part of \(\log\sin(\pi x)\)
is nonzero. At the present centered imaginary common saddle
that logarithm is real. Its actual conjugate modes can therefore
interfere with equal magnitudes. The new content is the resulting
sign comparison for the complete original trace, with all
complementary currents estimated, and its exact real zeros.

These marks are arbitrary real microscopic boundary data.
The theorem does not identify them with the discrete or algebraic
data of a particular marked filling. It does not disprove a
geometric volume conjecture, or a lower theorem under additional
source-specific restrictions on the boundary marks or closing.
It does show why the whole arbitrary-real upper class cannot
be promoted to a uniformly nonzero class merely by using more
amplitude jets or a positive common Hessian.

All four complete direct source texts were read at the following
matching pins, with the used source, anchor, contour and coefficient
implications checked:

* [Actual upper-packet composition and every current](research_microscopic_upper_packet_composition.md),
  SHA256 e72d9cf866330433cb19a2b809f46c3680f944d0af0fab18066622c83f72e911.
* [Actual bare-edge initial packet](research_uniform_terminal_family_and_star_fillings.md),
  SHA256 d9da305e1567393f5f714f11bd646cd2dca37b7d7569b9ab12d6a63014ece4f9.
* [Centered fold modes, actual anchor and full trace](research_endpoint_uniform_fold_cap.md),
  SHA256 5cdb59337b9e9cccac8bc94fb250106ed6cfc63db7f023ba564e715d8d2900eb.
* [Actual Gamma coefficients and their uniform errors](research_endpoint_nonreal_insertion_lower_bound.md),
  SHA256 ab3b4687b53c2168d22342c0e822b243a563f716d2a7a0de18d87c372546d7d0.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build or
compilation was run. Adopted notes and public manuscripts are unchanged.
