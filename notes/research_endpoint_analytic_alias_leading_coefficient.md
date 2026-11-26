# The leading coefficient of the actual analytic endpoint alias

Private written proof, 16 November 2026.

The moderate alias coefficient in the exact pre-turn decomposition
has an explicit leading term through the real physical interval and
its fold. The proof combines the actual fixed-height source
asymptotic with a thin-rectangle maximum principle. It does not
change the baseline, its normalization, or its symmetric repair
when the comparison height is chosen.

## 1. The fixed actual decomposition

Retain
\[
 h=N^{-1},\quad q=e^{\pi ih},\quad C_N(x)=2\cos(2\pi x+\pi h),\quad
 R_Nx=1-h-x,\quad w_N(\alpha)=2\cosh(\alpha h),
\]
\[
 P_N(C)=2T_N(C/2)+2,\qquad
 p_N(x)=P_N(C_N(x))=4\sin^2(\pi Nx).
 \tag{1}
\]
Here \(T_N\) in (1) is the Chebyshev polynomial. The source is the
ordinary kernel
\[
 K_N(w,C)=\sum_{k=0}^{N-1}e_k(w)e_k(C)
 \tag{2}
\]
with the original Newton normalization of the pinned sources.

Fix bounded complex microscopic parameters, a buffered symmetric
bulk rectangle of any prescribed finite height, and a positive
real error rate \(\gamma\) allowed by the pre-turn theorem. On
each of its finitely many local parameter charts fix once and
for all that theorem's actual decomposition
\[
 K_N(w_N(\alpha),C_N(x))
                    =V_N(x,\alpha)+p_N(x)Q_N(x,\alpha)+E_N(x,\alpha).
 \tag{3}
\]
The baseline \(V_N\) uses its original two-value physical anchor.
The repair is the specified symmetric finite sum
\[
 E_N(x)=\sum_{j=j_0}^{N-1-j_0}
        [e_j+d_j(x-x_j)]\operatorname{sinc}^2(N(x-x_j)),
 \qquad x_j=j/N,
\]
\[
 |e_j|+|d_j|\le CN^b e^{-\gamma N},\qquad
 \frac{E_N(x)}{p_N(x)}
       =\sum_{j=j_0}^{N-1-j_0}
          \frac{e_j+d_j(x-x_j)}{4\pi^2N^2(x-x_j)^2}.
 \tag{4}
\]
The sum \(V_N+E_N\) has exactly the original angular value and
first derivative at every covered node. At a double spectral
node these are the original value and first normal; the odd
simple node carries only its value.

The functions \(V_N,Q_N,E_N\) are invariant under \(R_N\) and
descend spectrally through \(C=-2\). The coefficient \(Q_N\)
is polynomially bounded on a larger fixed rectangle, and
\(V_N\) is moderate there. Fix such a rectangle and fix constants
\[
             |Q_N|+|V_N|\le C N^{b_0}
 \tag{5}
\]
before making any choice of the thin height below. The constants
are uniform on larger parameter-chart neighborhoods. Smaller
rectangles and spectral images are reserved for derivatives.
Neither the functions in (3) nor the exponent \(b_0\) will be
changed when that height is reduced.

Define the entire even function and its centered spectral form
\[
 A(\alpha)=\frac{\cosh^2(\alpha/2)}{\pi^2+\alpha^2},\qquad
 \mathcal R(C,\alpha)=-\frac{4A(\alpha)}{2-C}.
 \tag{6}
\]
At \(\alpha=\pm i\pi\) the numerator has a double zero and
the denominator a simple zero, so the singularities in \(A\)
are removable. All the spectral domains under discussion
avoid \(C=2\) by a fixed positive distance.

**Theorem 1.** On every smaller buffered rectangle, and its
spectral image including the fold, for each fixed
\(\varepsilon>0\) and each fixed number of spatial and \(\alpha\)-parameter
derivatives,
\[
 \boxed{\quad
 Q_N(C,\alpha)=\frac{\mathcal R(C,\alpha)}{N^2}
                           +O_{\rm hol}(N^{-3+\varepsilon}).
 \quad}
 \tag{7}
\]
The constants are uniform on bounded complex parameter compacts,
using the finite local charts. The estimate is absolute also at
all physical imaginary parameter marks. No relative unit
assertion is made there.

## 2. Actual horizontal data and the thin rectangle

The fixed-height source theorem states, uniformly on every band
\(0<H_0\le|\Im x|\le H_1<\infty\), that
\[
 \frac{N^2K_N(w_N(\alpha),C_N(x))}{p_N(x)}
       =-A(\alpha)\csc^2(\pi x)+O_{\rm hol}(N^{-1}).
 \tag{8}
\]
It holds for all bounded complex \(\alpha\), not only where
\(P_N(w_N(\alpha))\ne0\). Its actual period inversion and
parameter-circle removal are part of the pinned proof.
Since
\[
 \mathcal R(C_N(x),\alpha)
                  =-A(\alpha)\csc^2(\pi(x+h/2)),
 \tag{9}
\]
the centered expression differs from the leading term in (8)
by \(O_{\rm hol}(N^{-1})\) on such bands.

At any fixed nonzero height, \(N^2V_N/p_N\) is exponentially
small: \(V_N\) is polynomial and
\(|p_N|\ge4\sinh^2(\pi N|\Im x|)\). Formula (4), with
distance to every \(x_j\) at least \(|\Im x|\), shows that
\(N^2E_N/p_N\) is polynomial times \(e^{-\gamma N}\).
Consequently the actual holomorphic function
\[
             F_N(x,\alpha)=N^2Q_N(x,\alpha)
                                     -\mathcal R(C_N(x),\alpha)
 \tag{10}
\]
satisfies
\[
                     |F_N|\le C_{\rho}N^{-1}
                         \quad\text{on }\Im x=\pm\rho
 \tag{11}
\]
for every sufficiently small fixed \(\rho>0\), uniformly over
the full buffered real width. These are data for the fixed
coefficient in (3), not a new normalization of it.

Choose vertical sides \(a_N,b_N=R_Na_N\) strictly inside the
larger rectangle, with fixed real width bounded away from zero.
The desired inner real interval is separated from these sides
by a fixed distance \(d>0\). Equation (5) gives
\[
                         |F_N|\le C N^B
 \tag{12}
\]
on the whole larger rectangle, for a fixed \(B\ge0\).
Choose \(B\) now, independently of \(\rho\). Constants in (11)
may depend on \(\rho\); its choice is always fixed as \(N\to\infty\).

Let \(\omega_N\) be the harmonic measure of the two vertical
sides in the thin rectangle
\[
                  a_N<\Re x<b_N,\qquad |\Im x|<\rho.
 \tag{13}
\]
An explicit comparison gives, whenever the real coordinate is
at least \(d\) from the vertical sides,
\[
                   \omega_N(x)\le
                     2\sqrt2\,e^{-\pi d/(4\rho)}.
 \tag{14}
\]
Indeed set \(L_N=b_N-a_N\), \(c_N^*=(a_N+b_N)/2\), and
\(k=\pi/(4\rho)\). The harmonic function
\[
 \sqrt2\,
 \frac{\cosh(k(\Re x-c_N^*))}{\cosh(kL_N/2)}
                                      \cos(k\Im x)
 \tag{15}
\]
is at least one on the vertical sides and nonnegative on the
horizontal sides. It dominates \(\omega_N\) by the maximum
principle. On the stated inner real interval its value is at
most the right side of (14), by the elementary bound for the
ratio of the two hyperbolic cosines. This is uniform in the
allowed \(N\)-dependent placement of the sides.

It suffices to prove (7) for \(0<\varepsilon<1\). Choose
\(\rho\) so small that the bound in (14) is at most
\(\varepsilon/(B+1)\). Applying the two-constants maximum
principle to the subharmonic function \(\log|F_N|\), with
(11) on the horizontal sides and (12) on the vertical sides,
gives throughout the inner part of (13)
\[
 |F_N|\le C_\rho
          N^{-(1-\omega_N)+B\omega_N}
                   \le C_\rho N^{-1+\varepsilon}.
 \tag{16}
\]
Zeros are harmless: apply the subharmonic argument by a
regularization, or the usual maximum principle for its harmonic
majorant. Corner boundary values do not affect the harmonic
measure assertion.

On the rest of the desired tall rectangle, where
\(|\Im x|\ge\rho/2\), equations (8)--(10) already give the
stronger \(O(N^{-1})\) estimate. These two regions overlap.
Thus (16) holds on the whole smaller tall rectangle. The
spatial and parameter bounds may first be proved on larger
reserved buffers and chart neighborhoods, so Cauchy's formula
retains the exponent for every fixed derivative.

For spectral derivatives at the fold, all terms of (10) have
the exact reflection \(R_N\). Their even power series about
\((1-h)/2\) descend by
\[
              C_N(x)+2=4\sin^2(\pi(x-(1-h)/2)).
 \tag{17}
\]
A fixed angular disk about that point maps onto a spectral
neighborhood of \(C=-2\) with a uniform smaller radius.
Cauchy's formula in that spectral neighborhood proves the
same derivative bound. Away from the fold ordinary local
inversion applies. Dividing (16) by \(N^2\) proves (7).

The argument works on the larger parameter neighborhoods and
then on their finite smaller cover, so it includes every bounded
complex parameter compact. In the chart at zero the construction
is even in \(\alpha\). Therefore fixed original \(w\)-derivatives
can also be taken: away from zero \(dw_N/d\alpha\) has size
comparable to \(N^{-2}\), and at zero the regular coordinate
is \(\alpha^2\), with
\(d(w_N-2)/d(\alpha^2)=N^{-2}(1+O(N^{-2}))\).
Each such derivative costs at most the corresponding polynomial
factor \(N^2\); in particular the error in (7) becomes
\(O(N^{-3+2j+\varepsilon})\) after \(j\) input spectral
derivatives. The centered leading term is differentiated in
that same local coordinate. This completes the proof.

## 3. Exact consequences for ordinary divided-difference channels

Use the ordinary half-step operators from the pre-turn source:
\[
 C=v+v^{-1},\quad C_\pm=q^{\pm1}v+q^{\mp1}v^{-1},\qquad
 \mathcal Df=\frac{f(C_+)-f(C_-)}{C_+-C_-},\quad
 \mathcal Sf=\frac{f(C_+)+f(C_-)}2.
 \tag{18}
\]
They are applied to ordinary functions before the prescribed
canonical reduction. Coincident-color values have their
removable spectral meaning.

The exact alias identities are
\[
 P_N(C_\pm)=4-P_N(C),\qquad
 \mathcal D(pf)=(4-p)\mathcal Df,\quad
 \mathcal S(pf)=(4-p)\mathcal Sf,\qquad p=P_N(C).
 \tag{19}
\]
Let \(\mathcal W\) be any fixed word of length \(\ell\) in
\(\mathcal D,\mathcal S\), and let \(d(\mathcal W)\) be its
number of divided differences. Repeated use of (19) gives
the exact ordinary identity
\[
 \boxed{\quad
 \mathcal W K_N
   =\mathcal W V_N+
       \begin{cases}
          p\,\mathcal WQ_N,&\ell\text{ even},\\
          (4-p)\,\mathcal WQ_N,&\ell\text{ odd}
        \end{cases}
       +\mathcal W E_N .
 \quad}                                                     \tag{20}
\]
In particular the coefficient of \(p^0\) is
\(\mathcal WV_N\) for an even-length word and
\(\mathcal WV_N+4\mathcal WQ_N\) for an odd-length word.
There has been no replacement of \(K_N\) by its baseline
before taking the half shifts.

On fixed buffered holomorphic spectral domains,
\(\mathcal D=\partial_C+O(h^2)\) and
\(\mathcal S=I+O(h^2)\) when applied to a bounded holomorphic
function with its reserved derivatives. For example
\((C_++C_-)/2=\cos(\pi h)C=C+O(h^2)\) and
\((C_+-C_-)^2=O(h^2)\); Taylor expansion about their mean
proves both assertions, including the coincident-color limit.
The error in (7) remains of its stated order after any fixed
word, by the bounded holomorphic divided-difference operators.
Consequently
\[
 \mathcal WQ_N
  =\frac{1}{N^2}\partial_C^{d(\mathcal W)}\mathcal R(C,\alpha)
                         +O_{\rm hol}(N^{-3+\varepsilon}),
 \qquad
 \partial_C^d\mathcal R
              =-\frac{4A(\alpha)d!}{(2-C)^{d+1}}.
 \tag{21}
\]
The fixed-word error from replacing \(\mathcal D,\mathcal S\)
by their limits is \(O(N^{-4})\), which fits the error shown.

Thus an odd-length word has the actual constant alias correction
\[
              -\frac{16A(\alpha)d(\mathcal W)!}
                         {N^2(2-C)^{d(\mathcal W)+1}}
                         +O_{\rm hol}(N^{-3+\varepsilon}).
 \tag{22}
\]
For example this applies to both \(\mathcal DK_N\) and
\(\mathcal SK_N\). The word \(\mathcal S\mathcal D\) has even
length, so (20) retains its alias entirely in the \(p\) channel.
All these formulas include fixed parameter and spectral derivatives.

On real buffered physical rows, \(\mathcal WE_N\) and its fixed
spectral derivatives remain polynomial times \(e^{-\gamma N}\).
At double nodes \(p=p'=0\), so (20) gives the original value
and first-normal consequence with this error; at the odd simple
node it gives the value consequence. No extra spectral normal
is imposed at that node. These observations concern the actual
unturned channels only. Formula (22) supplies no lower bound
after cancellations with \(\mathcal WV_N\), multiplication, or
subsequent source operations.

## 4. Scope and complete direct sources

The leading term (7) is independent of the chosen local parameter
chart although the exact baselines and alias coefficients are
chosen chartwise. No transition estimate or global choice of
basis is needed. It identifies a coefficient in an exact source
decomposition, not a freely normalized homogeneous solution.
The physical mark zeros of \(A\) are retained; the estimate is
absolute there.

No physical-turn bound, closed-trace estimate, or filled-action
comparison follows from this theorem. In particular the
polynomial alias correction in (22) is not discarded when the
source is subsequently contracted.

The following complete direct sources were read at their matching
pins, with all used implications checked:

* [Exact pre-turn analytic alias class](research_endpoint_pre_turn_analytic_alias_class.md),
  SHA256 3d428bccbedf95055229596fd4774c4d0f09842b6e6e43db9249cf69d01c5012.
* [Actual fixed-height forced source asymptotic](research_unturned_endpoint_forced_off_real_asymptotic.md),
  SHA256 022c86dc122a647cb09cd2233292094501cf25719f87d928d019f03423f09f33.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build, or
compilation was run. Adopted notes and public manuscripts are unchanged.
