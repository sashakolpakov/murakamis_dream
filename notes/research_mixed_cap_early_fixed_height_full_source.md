# The complete early cap at independent fixed heights

Research deduction, 10 November 2026. The original five-current cap
bound extends to the independent early outgoing rectangle. A positive
type-three height can create a physical upper-row maximum, so the
extension retains that maximum. Its excess over the old right cut is
less than \(1/200\), and is zero when the outgoing real part is at least
\(4/25\). This is a complete finite-source bound, not a calibrated
supporting-plane comparison. No numerical evaluation or replay is used.

## 1. The unchanged source and the additional physical profile

Use the source and specified interpolation of the
[early five-current theorem](research_mixed_cap_early_taper_complex_profiles.md):
\[
\begin{split}
 U_{\alpha,N}(w,X)
 &=\sum_{i=0}^{N-1}\frac{H_N(w,r^{-i})p_i(X)}{P_i^{1+\alpha}},
 \qquad r=e^{-2\pi i/N},\quad X=e^{-2\pi iz},\quad\alpha=0,1,\\
 A_{\alpha,N}(e,z,w)
 &=D_N(e)^{-1}C_N(e,w)
 \frac{\widehat P_N(N(e+z))}
      {\widehat P_N(Nz)\widehat P_N(Ne)^\alpha}.
\end{split}\tag{1}
\]
At a physical private index \(e=i/N\), the second line is exactly
its summand in the first. The whole coherent coefficient, its phase
factor \(D_N^{-1}\), and the own type-four factorial are unchanged.
Set
\[
 E_c=[27/100,49/100]+i[-11/200,1/25],\qquad
 Z_0=[1/10,11/50]+i[-27/250,21/1000].                 \tag{2}
\]
The outgoing height is independent of its real coordinate. Put
\[
\begin{split}
 \Psi_\alpha(e,z)&=S(e)+J(e+z)-J(z)-i\pi ez-\alpha g(e),\\
 R_\alpha(s,z)&=\lambda(s)+\int_0^s
       \log|1-e^{-2\pi i(z+t)}|\,dt-\alpha J(s),
       \qquad\lambda(s)=\Re S(s).
\end{split}\tag{3}
\]
All phases retain the original branches and constants. The integrated
logarithm includes revived rows beyond a real product zero. On the
regular real private interval, \(R_\alpha(s,z)=\Re\Psi_\alpha(s,z)\).

For a private main height \(h_e\in(-11/200,1/25)\), retain the five
original profiles
\[
\begin{split}
 A_{\alpha,0}(z;h_e)&=\max_{.27\le u\le.49}
                         \Re\Psi_\alpha(u+ih_e,z),\\
 A_{\alpha,L}(z)&=\Re\Psi_\alpha(.27,z),\qquad
 A_{\alpha,R}(z)=\Re\Psi_\alpha(.49,z),\\
 A_{\alpha,-}(z)&=\max_{.27\le u\le.49}
                   \Re\Psi_\alpha(u-.055i,z)-.11\pi,\\
 A_{\alpha,+}(z)&=\max_{.27\le u\le.49}
                   \Re\Psi_\alpha(u+.04i,z)-.08\pi .
\end{split}\tag{4}
\]
The real cuts still have height zero. Define
\[
\begin{split}
 T_0(z)&=\max_{49/100\le s\le3/5}R_0(s,z),\qquad
 T_1(z)=A_{1,R}(z),\\
 d(z)&=\lambda'(49/100)+
       \log|1-e^{-2\pi i(49/100+z)}|,\\
 \Delta_0(z)&=\frac{15}{14\pi}\max\{d(z),0\}^2,\qquad
 \Delta_1(z)=0.
\end{split}\tag{5}
\]
The logarithm in (5) is regular on (2). Let
\(\mathscr A_\alpha(z;h_e)\) be the maximum of (4) and \(T_\alpha(z)\).
These definitions use the original action; no new root is proposed.

## 2. The complete upper physical tail

**Lemma 1.** On \(Z_0\),
\[
 \sup_{49/100\le s<1}R_0(s,z)=T_0(z),\qquad
 A_{0,R}(z)\le T_0(z)\le A_{0,R}(z)+\Delta_0(z),\qquad
 0\le\Delta_0(z)<\frac1{200}.                           \tag{6}
\]
Moreover \(\Delta_0(z)=0\) if either
\[
 \Re z\ge\frac4{25},\qquad\text{or}\qquad
 \Im z\le\frac7{40}(\Re z-1/10).                        \tag{7}
\]
For type four the whole upper physical tail decreases from its old
cut \(49/100\), at every height in (2).

*Proof.* The exact identity of
[the early real-row proof](research_mixed_cap_early_taper_real_rows.md),
equation (4), continues through the midpoint as
\[
 -\frac{\lambda''(s)}\pi
 =\cot\pi s+\frac2{\sin\pi s}
                \Re\frac1{\sqrt{2-e^{-2\pi is}}}.        \tag{8}
\]
Indeed the [full-index theorem](research_complete_boundary_full_index_interval.md)
continues the same \(S(e)=F(e,u_c(e))\) holomorphically along \(0<e<1\),
agreeing with the old action below one half. The squared radical in
(8) has real part at least one on that real interval. Its positive-real
root is holomorphic on a neighborhood of \([.49,.6]\).
Both sides of the complex identity underlying (8) are holomorphic
on a common connected neighborhood, after shrinking it; the identity
theorem fixes the original branch through the midpoint.

For \(49/100\le s\le3/5\),
\[
 \cot\pi s\ge-\tan(\pi/10)>-\frac13,\qquad
 \frac2{\sin\pi s}\Re\frac1{\sqrt{2-e^{-2\pi is}}}
       >\sqrt{\frac23}>\frac45.                        \tag{9}
\]
The first bound follows from
\(\cos(\pi/5)=(1+\sqrt5)/4>4/5\) and the half-angle formula.
For the second, the radical has argument of absolute value less
than \(\pi/4\) and modulus at most \(\sqrt3\), while
\(0<\sin\pi s\le1\).
Also \(59/100\le s+\Re z\le41/50\), so
\(\Re\cot\pi(s+z)<0\). Thus
\[
                  R_0''(s,z)<-\frac{7\pi}{15}
                       \quad(.49\le s\le.6).           \tag{10}
\]
The original bridge estimate is
\(\lambda'(.49)<-\log2+19/500\). Throughout (2),
\[
                 \frac12<r_h=e^{2\pi\Im z}<\frac{23}{20}.
                                                               \tag{11}
\]
For completeness, the elementary witnesses in
[the real-private half-stencil proof](research_mixed_cap_real_private_half_stencil.md)
use \(2\pi h\le33/250\) and
\(e^v\le1+v+v^2/[2(1-v/3)]\) for the upper bound, and
\(.216\pi<56/81<\log2\) for the lower bound.
Consequently
\[
 d(z)<\frac{19}{500}+\log\frac{43}{40}<\frac{113}{1000}.
                                                               \tag{12}
\]
Taylor's integral inequality gives
\[
 R_0(s,z)-R_0(.49,z)
 \le d(z)(s-.49)-\frac{7\pi}{30}(s-.49)^2
 \le\Delta_0(z).
                                                               \tag{13}
\]
Using \(\pi>3\), its upper allowance is strictly less than
\[
 \frac5{14}\left(\frac{113}{1000}\right)^2
       =\frac{63845}{14000000}<\frac1{200}.              \tag{14}
\]

The original upper-index identity in
[the full real-row theorem](research_mixed_outer_cap_real_tails.md)
is \(\lambda'(s)-J'(s)\le-\log4\) for \(1/2\le s<1\).
For \(3/5\le s<1\) and \(1/10\le x\le11/50\),
\[
             \sin\pi s\,|\sin\pi(s+x)|<\frac{13}{16}.
                                                               \tag{15}
\]
Before \(s+x=1\), this product decreases in \(s\), because
\(2s+x\in(1,2)\); at \(s=3/5\) it decreases in \(x\).
Its upper bound is therefore
\(\sin(3\pi/5)\sin(7\pi/10)<(1+\sqrt5)/4<13/16\).
After the wall its absolute maximum is at most
\((1-\cos\pi x)/2<1/2\). The exact radial expression now gives
\[
\begin{split}
 e^{2R_0'(s,z)}
 &\le r_h\sin^2\pi s\sin^2\pi(s+x)
             +\frac{(r_h-1)^2}{4}\sin^2\pi s\\
 &<\frac{169}{256}r_h+\frac{(r_h-1)^2}{4}
 \le\frac{19579}{25600}<1.
\end{split}\tag{16}
\]
The last quadratic increases for \(r_h\ge1/2\), its derivative
being at least \(105/256\); use its value at \(23/20\).
Thus the tail decreases beyond \(3/5\). At a product zero, integrate
on the adjoining intervals and use continuity of (3).
This proves (6).

Suppose now \(x\ge4/25\). On \(.49\le s\le.5\),
\(.65\le s+x\le.72\), whence
\[
 |1-r_he^{-2\pi i(s+x)}|^2
 <1+r_h^2+\frac{59}{50}r_h<\frac{7359}{2000}.            \tag{17}
\]
Here \(\cos(3\pi/10)<59/100\): square the identity
\(\cos^2(3\pi/10)=(5-\sqrt5)/8\), using
\(\sqrt5>223/100\). The bridge estimate and
\(\log(1-v)\le-v\) yield
\[
 R_0'(s,z)<\frac{19}{500}
           +\frac12\log\frac{7359}{8000}
          \le-\frac{33}{16000}<0.                      \tag{18}
\]
Above one half use the usual bound
\(\sin\pi s|\sin\pi(s+x)|\le\cos\pi x\). It gives
\[
 e^{2R_0'}\le\frac{1+r_h^2+2r_h\cos(2\pi x)}4
              <\frac{1481}{1600}<1,                   \tag{19}
\]
since \(\cos(2\pi x)\le\cos(8\pi/25)<\cos(3\pi/10)<3/5\).
In particular \(d(z)<0\), proving the first clause in (7).
The second is exactly the old early-taper upper-tail theorem,
which also gives \(d(z)<0\). It includes every negative height.

For type four, the unchanged bridge bounds
\(\lambda'<-3/5\), \(J'>3/5\), and
\(\log(1+r_h)<\log(9/4)<6/5\) give \(R_1'<0\).
Above one half the upper-index identity gives
\(R_1'<\log(9/16)<0\). Only (11) is used, so these statements
hold on the independent rectangle. This proves Lemma 1. \(\square\)

## 3. All finite currents, rows, colors and parities

**Theorem 2.** There is \(c>0\) such that for every \(\tau>0\),
\[
 |U_{\alpha,N}(-2\cos\theta,e^{-2\pi iz})|
 \le C_\tau N^{b_\tau}
 \left[
 e^{N\{\mathscr A_\alpha(z;h_e)-c(1-\cos\theta)+\tau\}}
 +e^{N\{E_{\rm end}(\Im z)+\tau\}}
 \right],                                             \tag{20}
\]
uniformly on (2), for \(-\pi\le\theta\le\pi\), both parities,
and private main heights in any fixed compact subinterval of
\((-11/200,1/25)\), where
\[
 E_{\rm end}(h)=\frac35+2\pi h_++\frac1{100}\log4
                       <\frac{373}{500}.              \tag{21}
\]
Every fixed ordinary-color derivative has the same exponents with
polynomial cost. One may replace \(\mathscr A_\alpha\) by the maximum
of (4), with only \(A_{\alpha,R}\) increased by \(\Delta_\alpha(z)\).

*Proof.* The exact row (1) is regular on a fixed neighborhood of
\(E_c\times Z_0\): the real parts of \(e,z,e+z\) lie in
\([.27,.49],[.1,.22],[.37,.71]\). The
[joint early curvature theorem](research_mixed_cap_joint_early_horizontal_concavity.md)
gives strict private vertical convexity on this independent product.
Apply the old residue identity at half-grid cuts tending to \(.27,.49\).
Its zero mode has density \(+N\). Move it to \(h_e\), retaining both
unweighted joins. Retain the two horizontal aliases and all four
vertical alias halves with their original \(2\pi|\Im e|\) penalties.
Vertical convexity bounds each join by its real-cut or main endpoint
and each alias half by its real-cut or horizontal endpoint. These are
exactly (4), with no scalar, sign or logarithmic lift changed.

The [whole real-color endpoint theorem](research_mixed_endpoint_real_color_decay.md)
supplies \(\Re S(e)-c_E(1-\cos\theta)\) on the retained rectangle.
All other factors are color independent. Its separate physical-index
theorem supplies a common \(c_I>0\) on \([.01,.99]\), across one half.
The original zero-safe factorial estimate then gives rate (3).
The compact lower tail increases toward \(.27\), with derivative
greater than \(13/100\), by Corollary 2 of the early real-row proof;
that assertion allows every finite outgoing height. Lemma 1 gives
precisely the additional upper physical profile (5). This proves the
first exponent of (20), with \(c\le\min(c_E,c_I)\).

No packet is extrapolated to a true index end. For \(i/N\le.01\),
the original finite Newton estimate retains rate \(1/4\).
For \(i/N=1-\delta\ge.99\), its all-real coefficient entropy is at
most \(3/5+\delta\log2\). The exact identity
\[
 p_i(X)=\frac{1-X^N}{\prod_{j=i+1}^{N}(1-r^jX)}          \tag{22}
\]
has denominator arguments modulo one in \([.09,.22]\).
Each factor is greater than \(1/2\), uniformly in its radius.
It therefore costs at most \(2\pi h_++\delta\log2\) in rate.
The remaining reciprocal own factorial has nonpositive rate in
this sector. These are the literal estimates of Section 4 of the
early real-row proof; they use only \(h\le.021\), not its taper
correlation. They give (21), including all revived rows, odd zeros
and their ordinary derivatives. The all-real Newton inequalities
used are \(V_\theta\le V_0\) below the half point and
\(V_\theta\le0\) above it.

Symbol errors, half-grid shifts and the finite row/current count fit
in one common tolerance \(\tau\), with polynomial prefactors.
The source coefficient bounds include fixed ordinary derivatives;
equivalently, the original polynomial degree and an ordinary-color
circle of radius \(N^{-2}\) give polynomial derivative cost.
No finite zero is divided out. Lemma 1 proves the replacement
assertion. \(\square\)

## 4. The repair is not the calibrated boundary comparison

The independent-height monotonicity claim really would be false:
at \(z=1/10+(21/1000)i\), let \(v=e^{21\pi/500}>9/8\), using
\(\pi>3\) and \(e^x>1+x\). Since \(\cos(\pi/5)>4/5\),
\[
 |1+ve^{-i\pi/5}|^2>1+\frac{81}{64}+\frac95
                    =\frac{1301}{320}>4.
\]
The exact value \(\lambda'(1/2)=-\log2\) therefore gives
\(R_0'(1/2,z)>0\), also at nearby strict interior points.
This containing-box point is not asserted to belong to an actual
correlated reference image; no signed-cap lower bound is inferred.

For an actual reference, joint concavity calibrates its unchanged
private main-height profile against the original supporting plane.
It does not transfer that comparison to the real cuts, aliases,
additional \(T_0\), or true-end sector. Their comparison must keep
the actual stationary marginals and any adjoining source.
In particular \(1/200\) cannot be absorbed into a smaller previously
proved gap without a new inequality.

The bound concerns the bare literal cap. External Fourier weights
and half allocations must still be multiplied exactly; no type-four
weight is divided away. No nonzero cap asymptotic, whole-word lower
bound or short-partial-filling conclusion is asserted.

## Source bindings

All are unchanged private sources, read directly for this proof.

| Source | SHA-256 |
|---|---|
| research_mixed_cap_early_taper_complex_profiles.md | 6a7b8cd841d89690a9733c1005a2449ce808ba20a875c2d1f8d8ca0b0a769138 |
| research_mixed_cap_early_taper_real_rows.md | d82b0506e7e156463360773bc8ab0e798334ee3a733ce9e6275215027c9c7ebc |
| research_mixed_outer_cap_real_tails.md | 17148159a21dc7d6e74dd92e4dcd8f5e62d91be1b01bd559c2566cdf66fb8b94 |
| research_complete_boundary_full_index_interval.md | 450cd41db9c49049e9b80a41c83828a2f0fafa43f986803bc57b93be580a57ef |
| research_mixed_endpoint_real_color_decay.md | 44921926dbdccef49c84e02566e86cf175979c8f189e62c7ba2e9b92c0d577eb |
| research_mixed_cap_joint_early_horizontal_concavity.md | 1b623741d70402af77287b287aa1e2636b0b8d1abcb7275d5347f14ac75dbb20 |
| research_mixed_cap_real_private_half_stencil.md | dc2cc1737bd7c424d050c2f5e7f30d4ede4e541707cfe73567ffb9a3ac548ac0 |
