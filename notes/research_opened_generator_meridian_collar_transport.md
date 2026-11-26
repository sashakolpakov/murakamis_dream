# Transport on the actual meridian collar

Private written proof, 19 November 2026.

The weighted opened-crossing estimate extends to the scaled complex
meridian collar used by the original source. In this parameter range
there is no need to move the occupation contour: the exact meridian
dependence is a bounded diagonal factor. This also gives estimates for
the genuine meridian derivatives of the crossing and its window error.
The prescribed crossing scalar is retained explicitly throughout.

The complete directs are W, the weighted transport theorem, and R,
the actual reduced braid representation. Both are pinned below. This
note does not continue occupation variables to fixed nonreal values.

## 1. The exact meridian dependence

Fix the root quantum parameter and the physical degree:
\[
 q=e^{\pi i/N},\qquad Q=q^2,\qquad d=N-1,\qquad 0\le T\le d.
\]
Keep the common meridian \(M\) variable near one. R gives
\[
 X(M)=\mathcal B_3(R_1;M)=\kappa(M)S_2(M)D(M),
\]
\[
 S_2(M)=\sum_{n=0}^d\frac{(x^{-1}L_1F_2)^n}{f_n},\qquad
 x=-M/q,\quad f_n=(Q;Q)_n,
 \qquad D_a(M)=(-1)^a q^{a(a+1)}M^{-2a}.
 \tag{1}
\]
The basis of degree \(T\) is \(|a,T-a\rangle\), \(0\le a\le T\).
Here \(F_2\), \(L_1\), and the factorials are independent of \(M\).
Only the transfer \(n=a-c\) reaches row \(c\) from column \(a\).
It follows exactly, including both physical caps, that
\[
 \boxed{\quad
 \kappa(M)^{-1}X_{c,a}(M)
      =M^{c-3a}\kappa(1)^{-1}X_{c,a}(1).
 \quad}                                                       \tag{2}
\]
Both sides are zero unless \(0\le c\le a\le T\).
Indeed \(x^{-(a-c)}\) contributes \(M^{-(a-c)}\), while
\(D_a\) contributes \(M^{-2a}\). This is an identity of the
actual finite meridian family, rather than a derivative of an
identity known only at \(M=1\).

Write \(M=e^{u/N}\). For a complex number \(v\), let
\(E_N(v)=\operatorname{diag}(e^{va/N})_{a=0}^T\). Then (2) is
\[
 \kappa(e^{u/N})^{-1}X(e^{u/N})
   =E_N(u)\,[\kappa(1)^{-1}X(1)]\,E_N(-3u).
 \tag{3}
\]
In particular all additional diagonal factors and their inverses
are bounded on every fixed disk \(|u|\le U\), uniformly in \(N\).
The scalar \(\kappa\) remains outside these auxiliary normalized
matrices; none of its derivatives is set equal to zero.

## 2. A sharp estimate throughout the collar

Use W's protected parameters and its exact grid centers
\[
 \tau=T/N,\qquad \xi_*=c_*/N,\qquad
 \eta_*=(a_0+L/2)/N,\qquad 0<\xi_*<\eta_*<\tau<1.
\]
They range over a fixed compact subset of this open region.
Keep W's real diagonal frames \(D_{\rm in},D_{\rm out}\),
unit packet \(b\), weighted maximum \(S_*\), positive amplitude
\(\mathcal A\), and complex Gaussian coefficient \(\Gamma\),
where \(\operatorname{Re}\Gamma>0\). These frames and the packet
are fixed as \(u\) varies. Define
\[
 \widehat Y_N(u)=\kappa(e^{u/N})^{-1}
           D_{\rm out}X(e^{u/N})D_{\rm in},\qquad
 w_N(u)=\widehat Y_N(u)b.
 \tag{4}
\]
Since the diagonal frames commute with \(E_N\), equation (3) gives
\(\widehat Y_N(u)=E_N(u)\widehat Y_N(0)E_N(-3u)\).
W's entire-matrix bound therefore implies
\[
 \|\widehat Y_N(u)\|_2\le C_U e^{NS_*}\qquad(|u|\le U).
 \tag{5}
\]
It also gives the row estimate
\[
 |w_N(u)_c|\le C_U N^{-1/4}e^{NS_*}
                         e^{-c_1(c-c_*)^2/N}.                 \tag{6}
\]
For (6), multiply W's Gaussian matrix bound by its packet bound
and sum over the actual input interval. The extra factors have
modulus at most \(e^{4U\tau}\). Neither estimate changes a cap.

Put \(z_c=(c-c_*)/\sqrt N\) and define the explicit leading row
from W without its relative error:
\[
 L_{N,c}=(-1)^c q^{-(T+1)c}
       e^{i\pi(c-c_*)\eta_*}
       N^{-1/4}e^{NS_*}\mathcal A e^{-\Gamma z_c^2/2},
 \qquad \theta_N=\xi_*-3\eta_*.
 \tag{7}
\]
For every fixed \(U,R\), uniformly on \(|u|\le U\) and
\(|z_c|\le R\),
\[
 \boxed{\quad
 w_N(u)_c=e^{u\theta_N}L_{N,c}
                              (1+O_{U,R}(N^{-1/2})).
 \quad}                                                       \tag{8}
\]
To check it, use exactly W's Gaussian sum. Its additional multiplier
from (2), on writing \(a=N\eta_*+y\sqrt N\), is
\[
 e^{u(c-3a)/N}
   =e^{u\theta_N}e^{u(z_c-3y)/\sqrt N}.
\]
On the central range the last factor is
\(1+O_U((1+|y|)/\sqrt N)\), integrably against W's Gaussian
majorant. On its complement the same Gaussian bounds apply with
a bounded factor. W's original Taylor and lattice errors thus
remain \(O_{U,R}(N^{-1/2})\). The Gaussian coefficient in (7)
does not vanish, so the error is relative, uniformly on the disk.

Equations (6),(8), by first summing on bounded \(z_c\) and then
letting that range increase, give
\[
 \|w_N(u)\|_2=
 |e^{u\theta_N}|e^{NS_*}\mathcal A
       \left(\frac{\pi}{\operatorname{Re}\Gamma}\right)^{1/4}
       (1+o_U(1)).                                          \tag{9}
\]
In particular the lower bound \(\|w_N(u)\|_2\ge c_U e^{NS_*}\)
holds on the full complex disk. This uses its bounded radius,
not a claim about a fixed-size disk in \(\log M\).

## 3. The original windows and all fixed meridian derivatives

Keep W's incoming and outgoing radial annuli, with fixed positive
margins around \(\eta_*\) and \(\xi_*\). Their literal partial
coherent resolutions are denoted by \(W_{\rm in},W_{\rm out}\).
These are the same fixed diagonal contractions as in W.
Their binomial tail estimate for \(b\), together with (6),(9), gives
\[
 \|(I-W_{\rm in})b\|_2\le Ce^{-cN},\qquad
 \|(I-W_{\rm out})w_N(u)\|_2\le C_U e^{-cN}e^{NS_*}.
\]
The entire-matrix upper bound (5) pays the incoming error. Hence
\[
 \begin{split}
 &\|(W_{\rm out}\widehat Y_N(u)
                 -\widehat Y_N(u)W_{\rm in})b\|_2\\
 &\quad+
 \|W_{\rm out}\widehat Y_N(u)W_{\rm in}b-w_N(u)\|_2
       \le C_U e^{-cN}\|w_N(u)\|_2 .
 \end{split}                                                \tag{10}
\]
Thus the window estimate is uniform on a complex collar for the
actual meridian family, not only at its central value.

There are useful derivative statements as well. For every fixed
integer \(k\ge0\), vector-valued Cauchy estimates on a slightly
larger fixed \(u\)-disk give
\[
 \|\partial_u^k\widehat Y_N(0)\|_2\le C_k e^{NS_*},
 \tag{11}
\]
\[
 \left\|\left.\partial_u^k
       (W_{\rm out}\widehat Y_N(u)
                  -\widehat Y_N(u)W_{\rm in})b\right|_{u=0}
       \right\|_2\le C_k e^{-cN}e^{NS_*}.                  \tag{12}
\]
The window-insertion difference in the second line of (10) obeys
the same derivative bound. One may prove these Cauchy estimates
by integrating the finite matrix or vector on a circle and applying
its displayed norm bound; no differentiation of a norm is used.
The holomorphic relative remainder in (8) also satisfies Cauchy's
estimate. Consequently on bounded \(z_c\),
\[
 [\partial_u^k w_N(0)]_c
    =L_{N,c}\bigl(\theta_N^k+O_{k,R}(N^{-1/2})\bigr).
 \tag{13}
\]
The error here is additive in the parentheses.

For the genuine logarithmic meridian \(\mu=\log M\), one has
\(u=N\mu\). Thus (11),(12) acquire precisely the factor \(N^k\)
when written for \(\partial_\mu^k\) of the scalar-normalized
actual operator. Equivalently, entrywise at \(\mu=0\),
\[
 \partial_\mu^k[\kappa(e^\mu)^{-1}X(e^\mu)]_{c,a}
     =(c-3a)^k[\kappa(1)^{-1}X(1)]_{c,a}.                 \tag{14}
\]
For the actual unnormalized operator put
\(\kappa_\mu^{(j)}=\left.\partial_\mu^j\kappa(e^\mu)\right|_0\).
The exact restoration formula is
\[
 \left.\partial_\mu^k
     [D_{\rm out}X(e^\mu)D_{\rm in}]\right|_0
 =\sum_{j=0}^k\binom kj\kappa_\mu^{(j)}N^{k-j}
                           \partial_u^{k-j}\widehat Y_N(0).
 \tag{15}
\]
The same product rule restores the scalar in the window current.
No growth assumption about its omitted derivatives is required,
because they have not been omitted. Any further prescribed framing
scalar is handled by its own product rule.

## 4. Scope

This proves a uniform local crossing and window estimate on every
fixed scaled meridian disk, with its true fixed-order meridian jets.
The frames have been fixed explicitly; a meridian-dependent choice
of other frames would contribute its own derivatives. No quantum
parameter is varied.

The collar \(|\log M|\le U/N\) does not move the leading occupation
saddle a fixed distance into complex occupation space. In particular
it does not put a faithful loxodromic total-product point into real
occupation coordinates. Nor does it prove that the packet belongs
to the complementary Gauss range, that successive local frames sew,
or that the specified closed source has a nonzero leading coefficient.
A linear combination of meridian derivatives in that source can
still cancel. These assertions require separate proofs.

## Complete proof directs

* W: notes/research_weighted_reduced_generator_window_transport.md,
  419 lines, SHA256
  800cd02115245208e2f37e688590ad00b0a44b6a274d973cf8c12dd8df6cc2be.
* R: notes/research_actual_reduced_braid_source.md,
  330 lines, SHA256
  9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.

Only written mathematics and text/hash operations are used. Both
complete directs were freshly read nontruncated in this active
author sequence. Author readback and renewed pins, followed by
independent matching-final and complete-direct review, are required
before adoption. Frozen manuscripts and public files are unchanged.
