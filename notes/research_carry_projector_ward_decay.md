# Exponential coherent decay of the actual carry-projector Ward currents

Private written proof, 19 November 2026.

The low/high pair-degree projectors have exact threshold Ward currents.
Their normalized ordinary-binomial coherent kernels are exponentially
small on the explicit \(\Gamma<1\) chamber of S. The estimate holds at
resolved zero coordinates as well as on nonzero-coordinate charts, and
retains every fixed true meridian derivative. This is a kernel estimate
for the projector currents themselves, not an operator-norm estimate
or an estimate after composition with an unspecified crossing or word.

## 1. Literal arrows, kernels, and the exact currents

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(M=e^\mu\), \(x=-M/q\). The quantum root is held fixed. F supplies
the finite physical arrows
\[
 Ew_a=(MQ^{-a}-M^{-1})w_{a-1}\quad(a>0),\quad Ew_0=0,\qquad
 Fw_a=(1-Q^{a+1})w_{a+1},\qquad Kw_a=xQ^{-a}w_a .
 \tag{1}
\]
The upper \(F\) arrow is zero, since \(1-Q^N=0\).
On two heads put
\[
 E_{\rm p}=E_1K_2+E_2,\qquad
 F_{\rm p}=F_1+K_1^{-1}F_2,\qquad J=J_1+J_2,\qquad
 \Pi_0=\mathbf1_{J\le d},\quad \Pi_1=I-\Pi_0.
 \tag{2}
\]
All thresholds are exact integer occupations. Direct degree counting,
including the endpoint zeros in (1), gives S(18a--b):
\[
 [E_{\rm p},\Pi_0]=-E_{\rm p}\mathbf1_{J=N},\qquad
 [F_{\rm p},\Pi_0]=F_{\rm p}\mathbf1_{J=d}.
 \tag{3}
\]
The high-projector currents have the opposite signs. In particular,
for a scalar mark \(\zeta\),
\[
 [E_{\rm p},\Pi_0+\zeta\Pi_1]
       =(\zeta-1)E_{\rm p}\mathbf1_{J=N},\qquad
 [F_{\rm p},\Pi_0+\zeta\Pi_1]
       =(1-\zeta)F_{\rm p}\mathbf1_{J=d}.
 \tag{4}
\]
There is no approximation in these identities or their meridian jets.

For a two-head matrix \(A\), use the actual input-binomial convention
\[
 K_A(z,w)=\sum_{a,b,c,e=0}^{d}
       A_{(c,e),(a,b)}\binom da\binom db z_1^cz_2^e w_1^aw_2^b .
 \tag{5}
\]
Put \(v_i=z_iw_i\) and
\(I_N=K_I=(1+v_1)^d(1+v_2)^d\). Only \(1+v_i\ne0\) is required
to define the normalized kernels
\[
 \mathcal E_N=\frac{K_{E_{\rm p}\mathbf1_{J=N}}}{I_N},
 \qquad
 \mathcal F_N=\frac{K_{F_{\rm p}\mathbf1_{J=d}}}{I_N}.
 \tag{6}
\]
The symbols \(\mathcal E_N,\mathcal F_N\) here denote currents, not
external framing lines.

At \(z_1z_2\ne0\), the exact finite formulas are
\[
 \mathcal E_N=\frac1{I_N}\sum_{a+b=N}
 \binom da\binom db v_1^av_2^b
 \left[\frac{xQ^{-b}(MQ^{-a}-M^{-1})}{z_1}
            +\frac{MQ^{-b}-M^{-1}}{z_2}\right],
 \tag{7}
\]
\[
 \mathcal F_N=\frac1{I_N}\sum_{a+b=d}
 \binom da\binom db v_1^av_2^b
 \left[z_1(1-Q^{a+1})
            +z_2x^{-1}Q^a(1-Q^{b+1})\right].
 \tag{8}
\]
All indices in these sums remain between zero and \(d\). In (7)
the threshold forces \(a,b\ge1\); thus the displayed divisions by
\(z_i\) are removable in the original polynomial kernel. In (8)
the factors \(1-Q^N\) kill precisely the forbidden upper arrows.
No occupation cap has been extended.

## 2. Exact shell bounds, including zero coordinates

Write \(X=|v_1|\), \(Y=|v_2|\), and
\[
 \Gamma(v_1,v_2)
   =\frac{(\sqrt X+\sqrt Y)^2}{|1+v_1|\,|1+v_2|},\qquad
 S_\ell(X,Y)=\sum_{a+b=\ell}\binom da\binom db X^aY^b .
 \tag{9}
\]
For any \(R>0\), positivity of the coefficients gives
\[
 S_\ell(X,Y)\le R^{-\ell}(1+RX)^d(1+RY)^d.
 \tag{10}
\]
If \(XY>0\), choose \(R=(XY)^{-1/2}\). Since
\((1+RX)(1+RY)/R=(\sqrt X+\sqrt Y)^2\), this proves
\[
 \frac{S_{d+1}}{|I_N|}\le\sqrt{XY}\,\Gamma^d,\qquad
 \frac{S_d}{|I_N|}\le\Gamma^d .
 \tag{11}
\]
Neither inequality requires \(XY<1\) or \(XY>1\).
At \(XY=0\), the first shell vanishes and the second inequality
holds by continuity, including \(X=Y=0\).

A second estimate removes the \(z_i^{-1}\) factors in (7).
The polynomial \(S_{d+1}(X,Y)\) is divisible by \(XY\). Reindexing
\(a'=a-1\), using
\(\binom da=(d/a)\binom{d-1}{a-1}\le d\binom{d-1}{a-1}\),
and applying (10) to degree \(d\), gives
\[
 \frac{S_{d+1}(X,Y)/X}{|I_N|}
 \le \frac{d\,\Gamma^d}{1+RX}\le d\Gamma^d,\qquad
 \frac{S_{d+1}(X,Y)/Y}{|I_N|}\le d\Gamma^d .
 \tag{12}
\]
The first displayed denominator uses the same optimizing \(R\);
the second follows by exchanging the heads. The final bounds extend
continuously to \(XY=0\), since the quotients are polynomials.
This argument estimates the absolute coefficients of the divided
shell, so it applies unchanged with the unit \(Q\)-phases in (7).

Fix a finite \(\eta>0\) and restrict to \(|N\mu|\le\eta\).
Every coefficient in the brackets of (7)--(8), after removing
the displayed coordinate factors, has a uniform bound \(C_\eta\).
Indeed \(|Q|=1\), \(|M|^{\pm1}\le e^{\eta/2}\), and \(x=-M/q\).
Equations (7)--(12) therefore prove
\[
 |\mathcal E_N|
   \le C_\eta d(|w_1|+|w_2|)\Gamma^d,\qquad
 |\mathcal F_N|
   \le C_\eta(|z_1|+|z_2|)\Gamma^d .
 \tag{13}
\]
These inequalities hold at all coordinates with \(1+v_i\ne0\),
including \(z_i=0\). In deriving the first one,
\(z_i^{-1}v_i=w_i\) is used before taking that zero value.
On the smaller chart \(z_1z_2\ne0\), the sharper alternative is
\[
 |\mathcal E_N|\le C_\eta
       (|z_1|^{-1}+|z_2|^{-1})\sqrt{XY}\,\Gamma^d .
 \tag{14}
\]
When \(v_i=0\) because \(z_i=0\) but \(w_i\ne0\), the \(E\)-current
need not vanish. Formula (13), rather than division by that zero
coordinate or differentiation of the factor \(\sqrt{XY}\), is the
appropriate statement.

## 3. Genuine meridian and coherent jets

At fixed \(z,w\), every fixed meridian derivative satisfies the
same bounds (13)--(14), with \(C_\eta\) replaced by
\(C_{\eta,k}\), uniformly in \(N\). To see this directly, the
first coefficient of (7) is
\[
 xQ^{-b}(MQ^{-a}-M^{-1})
       =-q^{-1}\big(M^2Q^{-a-b}-Q^{-b}\big).
 \tag{15}
\]
The other coefficient uses only \(M,M^{-1}\), while (8) uses
only constants and \(M^{-1}\). Thus \(\partial_\mu^k\) multiplies
these finitely many Laurent monomials by powers of \(0,\pm1,2\);
one may take \(C_{\eta,k}\le C_\eta(1+2^k)\).
The identity kernel is meridian independent. No \(N^k\) loss is
needed for these fixed-coordinate currents.

Let \(\mathcal K\) be any compact subset of
\[
 \mathcal U=\{(z,w)\in\mathbb C^4:
                   1+z_iw_i\ne0,\ \Gamma(z_1w_1,z_2w_2)<1\}.
 \tag{16}
\]
There is a fixed complex neighborhood of \(\mathcal K\), with
bounded coordinates, nonzero incidence denominators, and
\(\Gamma\le\gamma<1\). Apply (13) and its meridian derivatives
on that neighborhood, and then use the ordinary multivariable
Cauchy estimate. For every fixed coordinate multi-index \(\alpha\)
and fixed \(k\ge0\),
\[
 \sup_{\substack{(z,w)\in\mathcal K\\|N\mu|\le\eta}}
 \left(
 |\partial_{z,w}^{\alpha}\partial_\mu^k\mathcal E_N|
 +|\partial_{z,w}^{\alpha}\partial_\mu^k\mathcal F_N|
 \right)
       \le C_{\mathcal K,\alpha,k,\eta}\,d\,\gamma^d .
 \tag{17}
\]
In particular every such jet is exponentially small as \(N\to\infty\).
The exponent uses the buffered \(\gamma\); it is not a claim that
coordinate derivatives preserve the pointwise factor \(\Gamma(v)^d\).
The conclusion includes resolved zero coordinates in \(\mathcal K\).
It applies to both projector currents by (3), and to (4) for
\(\zeta\) in a fixed compact set.

Fixed integer powers of the physical \(K_1,K_2\) placed on either
side of these currents preserve the same conclusion: they only
multiply each occupation coefficient by a unit \(Q\)-phase and a
fixed Laurent power of \(M\). Their fixed meridian derivatives change
the constants. This assertion does not include arbitrary moving
factorial gauges or coordinates.

## 4. Meaning and limitation

This proves local almost-intertwining in the specific sense of
normalized binomial coherent kernels on (16). The exact finite
operators (3) are still present; no exponentially small operator
norm is asserted. Even the exact identity
\([E_{\rm p},R(\Pi_0+\zeta\Pi_1)]
       =R[E_{\rm p},\Pi_0+\zeta\Pi_1]\)
does not turn (17) into a kernel estimate for that product by
pointwise multiplication of normalized symbols.

A contracting coherent chain, its remaining density, and its boundary
currents require separate estimates before (17) bounds an inserted
current in an original source. No membership of an arbitrary geometric
point in (16), localized source/axis correspondence, geometric cycle
coefficient, or lower bound for a closed period is inferred.

## Complete proof directs

* S: notes/research_crossing_wall_degree_sectors.md, 532 lines,
  SHA256 638e7feb66eeb4671775f6df57f3994b4139f5be95263247956dece538cb0636.
* F: notes/research_actual_meridian_source_frames.md, 506 lines,
  SHA256 6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976.

Both complete directs were whole-read nontruncated in this active
author/review sequence, every used implication was checked, and their
matching pins are retained. Only written mathematics and text/hash
operations were used; frozen and public files were not edited.
