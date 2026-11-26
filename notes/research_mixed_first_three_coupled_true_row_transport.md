# Uniform coupled transport of the true last row after a type-three cap

Research deduction, 7 November 2026. The true last-row alternative
of the first adjoining own-four factor has strictly positive
transport along the entire actual early first-minimum taper,
including both incidences of the changing neighbor height.
For a first cap of type three, its rate derivative is greater
than \(1/100\), uniformly over the full following regular
index rectangle.

This pays this entire endpoint branch, rather than only a seam
collar. Interior high physical rows and a following factor's
other profiles remain separate. No calibrated whole-boundary
sign is asserted.

## 1. Original endpoint allocation and actual heights

Keep the exact source and true-row rate of
[the last-row transport theorem](research_mixed_first_attached_true_last_row_transport.md).
The first cap has own type three and the moving neighbor
has own type four. On an active first-minimum segment write
\[
 \begin{gathered}
 d=x-.1,\quad .1\le x\le.22,\quad x\le z\le.5,\qquad
 a=x-i\lambda_a d,\quad b=z-i\lambda_b d,\\
 -7/40\le\lambda_a\le3/5,\qquad
 0\le\lambda_b\le17/20,\qquad
 e\in[.27,.49],\\
 t=w+i\zeta,\qquad .22\le w\le.49,\qquad
                       -.108\le\zeta\le.068 .
 \end{gathered}                                                \tag{1}
\]
The same original \(\lambda_b=-c_bR(z)/.12\) occurs in
the height and its derivative. The actual upper cutoff,
the active-minimum condition, and the following ordinary
source eligibility are those of the
[coupled seam theorem](research_mixed_first_attached_coupled_seam_transport.md).
No following endpoint cap or Fourier endpoint is substituted.

Put
\[
 p_e=g'(e+a)-g'(a),\qquad
 B_{\rm end}(t;z,h)
       =\Im\{g'(t+z+ih)-2g'(z+ih)+2\pi it\}.
 \tag{2}
\]
The exact derivative of the regular cap, first ordinary
true row and following regular profile is
\[
 \mathcal H_{\rm end}=
 \begin{cases}
 \Re p_e+\lambda_a\Im p_e+2\pi\lambda_a
                 +\lambda_bB_{\rm end}(t;z,-\lambda_bd),
                                      &\lambda_a\ge0,\\
 \Re p_e+\lambda_a\Im p_e
                 +\lambda_bB_{\rm end}(t;z,-\lambda_bd),
                                      &\lambda_a\le0 .
 \end{cases}                                                  \tag{3}
\]
The two formulas agree at \(\lambda_a=0\).
They retain the original true-row term \(2\pi(-\Im a)_+\),
the two halves at \(b\), and the following chirp.
The right derivative of \(2\pi(\Im b)_+\) is zero,
since the actual neighbor moves into nonpositive height.

## 2. The first part dominates its zero-height logarithm

**Lemma 1.** The first part of (3), before its neighboring
term, is at least
\[
                      f_e(x)=\log\frac{\sin\pi(e+x)}{\sin\pi x}.
 \tag{4}
\]

*Proof.* Temporarily vary the first height coefficient
\(\lambda\) between zero and its actual \(\lambda_a\),
keeping \(x\) fixed. This stays in the already proved
first-taper cotangent domain. Section 1 of the
[actual eligibility theorem](research_mixed_first_attached_taper_root_eligibility.md)
gives \(|\Im\cot\pi a|<1\) on this entire interval.
The own angular cosine is positive and the shifted angular
cosine is negative. Their imaginary cotangents have the
same signed hyperbolic numerator, so the shifted one
has smaller modulus.
Consequently, exactly
\[
 \left|\frac{\partial}{\partial\lambda}\Re p_e\right|
 =\pi d\,|\Im\cot\pi(e+a)-\Im\cot\pi a|
                                                   <\pi d .
 \tag{5}
\]
Thus \(\Re p_e(\lambda_a)\ge f_e(x)-\pi d|\lambda_a|\).

The original rotated-ratio identity, with its fixed logarithmic
lift, gives
\[
 \lambda_a\ge0\Longrightarrow\Im p_e\ge-\pi e,\qquad
 \lambda_a\le0\Longrightarrow\Im p_e\le-\pi e .
 \tag{6}
\]
For \(\lambda_a\ge0\), the first part of (3) is therefore
at least \(f_e(x)+\pi\lambda_a(2-e-d)\).
For \(\lambda_a\le0\), it is at least
\(f_e(x)+\pi|\lambda_a|(e-d)\).
Both added terms are nonnegative:
\(d\le.12<e\) and \(e+d<2\).
This proves (4), including \(\lambda_a=0\). \(\square\)

The sine in the numerator of (4) is positive and concave
as a function of \(e\). It suffices to bound
\(f_{.27}\) and \(f_{.49}\).
Both are strictly convex in \(x\), since
\[
 f_e''(x)=\pi^2\{\csc^2(\pi x)-\csc^2(\pi(e+x))\}>0 .
 \tag{7}
\]
Indeed \(\sin\pi(e+x)>\sin\pi x\) throughout the stated
real intervals.
At \(x=.22\), the original trigonometric witnesses give
\[
 \begin{array}{c|cc}
 e& f_e(.22)&-f'_e(.22)\\ \hline
 .49&>21/100&>197\pi/100\\
 .27&>11/25&>7\pi/6 .
 \end{array}                                                  \tag{8}
\]
Here are explicit witnesses. The bounds
\(\cos(.21\pi)>7899/10000\),
\(\sin(.22\pi)<319/500\),
\(\tan(.21\pi)>77/100\), and
\(\cot(.22\pi)>6/5\) are proved in Section 3 of the
[own-four moving comparison](research_mixed_first_four_moving_height_comparison.md).
They imply
\[
 f_{.49}(.22)>
  2\frac{7899-6380}{7899+6380}
       =\frac{3038}{14279}>\frac{21}{100},
 \qquad -f'_{.49}(.22)>\frac{197\pi}{100}.
 \tag{9}
\]
For the other endpoint,
\(\cos(.01\pi)>999/1000\) and
\(\cot(.49\pi)=\tan(.01\pi)<1/30\), by the elementary
sine/cosine bounds, give
\[
 f_{.27}(.22)>
  2\frac{999-638}{999+638}=\frac{722}{1637}>\frac{11}{25},
 \qquad -f'_{.27}(.22)>\frac{7\pi}{6}.
 \tag{10}
\]
The logarithmic inequality is
\(\log u>2(u-1)/(u+1)\) for \(u>1\).
Convexity and (8) now give the full-interval lower bounds
\[
 \begin{split}
 f_{.49}(x)&>\frac{21}{100}
                     +\frac{197\pi}{100}\left(\frac3{25}-d\right),\\
 f_{.27}(x)&>\frac{11}{25}
                     +\frac{7\pi}{6}\left(\frac3{25}-d\right).
 \end{split}                                                  \tag{11}
\]

## 3. Both neighboring incidences, including all following heights

For \(z\ge.28\), every following shifted real argument
\(y=w+z\) belongs to \([.5,.99]\).
The original radial bounds give
\[
 A(y,R)\ge\pi(1-2y)\quad(R>0),\qquad
 A(z,r_b)\le\pi(.5-z)\quad(0<r_b\le1).
 \tag{12}
\]
Thus
\[
 B_{\rm end}(t;z,h)
      =A(w+z,e^{2\pi(h+\zeta)})-2A(z,e^{2\pi h})+2\pi w
                                                         \ge0 .
 \tag{13}
\]
This retains both incidences and permits positive following
index height.

Suppose now that \(z<.28\).
The exact
[following-index elimination](research_mixed_first_attached_following_index_elimination.md)
shows that at neighbor height zero only its lower following
branch can be negative. The upper branch is already
nonnegative by (12). For the lower one put
\(R_-=e^{-.216\pi}\).
Its value is
\[
                   C(z)=\pi(2z-.56)+A(.22+z,R_-).
 \tag{14}
\]
The derivative of \(2\pi z+A(.22+z,R_-)\) is
\[
       \frac{2\pi(1-R_-\cos2\pi(.22+z))}
              {1+R_-^2-2R_-\cos2\pi(.22+z)}>0 .
 \tag{15}
\]
Since \(z\ge x\), it suffices to bound \(C(x)\).
On \(y\in[.32,.44]\), \(A(y,R_-)\) decreases in \(y\),
because its angular cosine is negative and
\(\Im\cot\pi(y-.108i)<1\).
Also \(R_->1/2\), and
\[
                         A(.44,R_-)>\frac19 .
 \tag{16}
\]
For a direct witness, use
\(\sin(.12\pi)>\sin(3/8)>375/1024>9/25\).
At radius \(1/2\), the argument tangent is greater
than \(3/25\), and both components have the required
positive signs. Therefore
\[
 A(.44,R_-)>
      \arctan(3/25)>
        \frac3{25}-\frac{(3/25)^3}{3}
                         =\frac{1866}{15625}>\frac19 .
 \tag{17}
\]
Here \(R_->1/2\) follows from the previously proved
\(.216\pi<\log2\).
Equations (14)--(17), including the nonnegative upper
following branch, give
\[
                     B_{\rm end}(t;z,0)>
                              \pi(2x-.56)+\frac19 .
 \tag{18}
\]
The right side is negative on the entire \(x\) interval.

The actual negative neighbor height supplies a favorable
quadratic credit. From the original derivative identity,
\[
 -\partial_hB_{\rm end}/\pi
   =2\Re\cot\pi(z+ih)
       -\Re\cot\pi(w+z+i(h+\zeta))>\frac9{10},
                         \qquad z<.28,\quad -.108\le h\le0 .
 \tag{19}
\]
For completeness, the three real ranges used in the
[uniform-credit proof](research_mixed_first_attached_uniform_neighbor_credit.md)
give respectively the strict lower bounds
\[
 116/67-2/3=214/201,\qquad
 32/19-1/2=45/38,\qquad
 36/29-1/3=79/87 ,
 \tag{20}
\]
on \(z\in[.1,.15]\), \([.15,.2]\), \([.2,.28]\).
All exceed \(9/10\), uniformly in \(\zeta\).
Integration at the same actual \(h=-\lambda_bd\)
therefore yields
\[
 \lambda_bB_{\rm end}(t;z,-\lambda_bd)
 >
 \lambda_b\left\{\pi(2x-.56)+\frac19\right\}
                       +\frac{9\pi}{10}\lambda_b^2d ,
 \tag{21}
\]
with the nonstrict version understood at \(\lambda_b=0\).

## 4. Exact payment on the entire taper

For \(z\ge.28\), Lemma 1, (11) and (13) already give
\(\mathcal H_{\rm end}>21/100\).
For \(z<.28\), combine each line of (11) with (21).
At fixed \(\lambda_b\), each resulting lower expression
is affine in \(d\). It therefore suffices to check
\(d=0\) and \(d=3/25\); minimizing on this containing
interval is conservative even when the actual \(x\le z\)
restriction gives a shorter interval.

At \(d=0\), the coefficient of \(\lambda_b\) is negative,
so the minimum is at \(17/20\).
The right private endpoint gives
\[
 \frac{21}{100}+\frac{17}{180}-\frac{87\pi}{1250}
                      >\frac1{12}.
 \tag{22}
\]
For example, \(\pi<22/7\) reduces the last comparison to
the positive cross-product difference
\(199\cdot4375-957\cdot900=9325\).
The left private endpoint gives
\[
 \frac{11}{25}+\frac{17}{180}-\frac{83\pi}{500}
            >\frac{401}{31500}>\frac1{100}.
 \tag{23}
\]

At \(d=3/25\), either private endpoint has the form
\[
 c+\frac{27\pi}{250}\lambda_b^2
                  -\left(\frac{3\pi}{25}-\frac19\right)\lambda_b,
 \qquad c\in\{21/100,11/25\}.
 \tag{24}
\]
Its quadratic minimum, even over all real \(\lambda_b\),
exceeds \(c-1/16\). Indeed its quadratic coefficient is
greater than \(8/25\), while its positive linear magnitude
is less than \(27/100\); the maximum loss is less than
\[
                   \frac{(27/100)^2}{4(8/25)}
                          =\frac{729}{12800}<\frac1{16}.
 \tag{25}
\]
Both \(21/100-1/16=59/400\) and
\(11/25-1/16=151/400\) exceed \(1/100\).
Equations (22)--(25) prove the following.

**Theorem 2.** On the full actual domain (1), with the original
following regular profile and all its indicated heights,
\[
                         \boxed{\ \mathcal H_{\rm end}>1/100.\ }
 \tag{26}
\]
No radius or coefficient has been selected independently
of its occurrence in the source.

The
[own-three endpoint payment](research_mixed_first_three_early_endpoint_payment.md)
already absorbs every true-end cap alternative into the
real-private cap envelope on this actual taper.
Adding the same ordinary true-row rate and following
profile preserves that pointwise domination.
Thus (26) applies to the complete first-cap envelope on
this ordinary endpoint branch.
Integration followed by maximization over the unchanged
private and following profile intervals preserves its
strict slope. No smooth maximizing index is required.

This proof does not pay interior high physical rows, a
following factor's additional physical-tail profiles, or
an independently unproved following finite-source domain.
It also does not identify the transported endpoint value
with the calibrated boundary value.
The original middle compensation, complex marginals,
relative pinning fee, physical zeros and both parity
conventions remain those of the unchanged source theorems.
