# The normalized outgoing source and its frozen compatibility

Private finite-source deduction, 9 November 2026. After division by
its literal first complete row, the entire attached outgoing
polynomial has a uniform rational limit on a fixed spectral ellipse.
Its actual positive Fourier coefficients therefore determine the
first-crossing frozen compatibility to relative order \(N^{-1}\).
That compatibility has a uniformly nonzero limiting factor and the
original outgoing half-input action.

This rules out exponential smallness of this specified frozen
functional on the actual complete source. It does not estimate the
correlated finite boundary responses or the signed inner observation.
In particular the frozen forward half-line is not identified with
the reversed hard endpoint of the finite compression. No mathematical
numerical evaluation or frozen-source edit is used.

## 1. Complete source and existing finite estimates

Retain
\[
 D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M,\quad
 q=e^{i\pi/N},\quad r=q^{-2},\quad
 s_b=2\sin(\pi b/N),\quad c_b=2\cos((2b+1)\pi/N).
 \tag{1}
\]
The output domain is the original closed rectangle
\[
 z_*=u+ih,\qquad
 3/10\le u\le39/100,\quad-3/100\le h\le1/50,\qquad
 Z=e^{-2\pi i z_*}.
 \tag{2}
\]
Both parities and all these outputs are included in what follows.
Use the complete outgoing source and exact radical quotients
\[
 \begin{split}
 C_{b,N}(Z)
   &=\sum_{j=0}^{D}
       \frac{r^{-bj}(r^{b+1};r)_j(rZ;r)_j}{(r;r)_j^2},\\
 \alpha_{b,N}(Z)&=(-q)^bC_{b,N}(Z),\\
 P_b^{\rm rad}(X)&=
       \prod_{h=M}^{b-1}\frac{c_h-X}{s_{h+1}^2},\\
 F_N^+(X,Z)&=\sum_{b=M}^{D}\alpha_{b,N}(Z)P_b^{\rm rad}(X).
 \end{split}
 \tag{3}
\]
The literal stop in the first sum is \(D-b\). Its denominators
are nonzero; its vanishing incoming numerator factors, empty
products, and last row \(C_{D,N}=1\) are unchanged.
These are the source polynomials of
[the complete trailing theorem](research_mixed_next_outgoing_trailing_determinants.md)
and [the attached Green theorem](research_mixed_next_outgoing_action_weighted_green_ellipse.md).

Let \(\mathcal L(a,Z)\) be the selected complete unsigned ratio
of the [absolute anchor](research_mixed_next_outgoing_absolute_anchor.md),
and put
\[
 L_0(Z)=\mathcal L(1/2,Z),\qquad E_0(Z)=\mathcal E(1/2,Z).
 \tag{4}
\]
All complete denominators \(C_{b,N}\) used here are nonzero.
The adopted finite ratio estimates give, uniformly on the
middle interval,
\[
 \frac{C_{b,N}}{C_{b-1,N}}
       =\mathcal L(b/N,Z)(1+O(N^{-1})),\qquad
 \sqrt{s_b}\left|\frac{C_{b,N}}{C_{b-1,N}}\right|
                         \le\frac{251}{252}.
 \tag{5}
\]
The function \(\mathcal L\) has a bounded first derivative on
a fixed neighborhood of \(a=1/2\) in this real parameter
interval. Its selected root is nonzero there. The original
action interpretation also gives
\[
                  |L_0|<\frac{125}{126\sqrt2}<\frac34 .
 \tag{6}
\]
The last comparison follows from \(\sqrt2>4/3\), and uses
no evaluation of a reference value.

The two-sided absolute anchor and its one additional ratio
from \(M-1\) to \(M\) imply
\[
 cN^{-1/2}e^{NE_0(Z)}
       \le|\alpha_{M,N}(Z)|
       \le CN^{-1/2}e^{NE_0(Z)}.
 \tag{7}
\]
Indeed (5) is uniformly bounded above and below at that
single step, and the boundary estimate for \(C_{M-1,N}\)
already includes both parity-dependent half steps.

We will also use the full-range consequence
\[
 \left|\frac{\alpha_{b,N}}{\alpha_{M,N}}\right|
            \le CN^A e^{-c_0(b-M)},\qquad
 c_0=\frac{205}{1134},\qquad M\le b\le D.
 \tag{8}
\]
To see this directly from the adopted sources, the absolute
anchor gives the ratio up to polynomial factors at rate
\(\mathcal E(b/N,Z)-E_0(Z)\). Its denominator at \(M\)
has the lower bound (7). The
[sharper action loss](research_mixed_next_outgoing_sharper_tail_and_ellipse.md)
bounds that difference above by
\(-c_0(b/N-1/2)\). Since \(M\ge N/2\), (8) follows.
In particular this relative tail estimate does not replace the
anchor by a one-sided upper bound.

## 2. A uniform rational limit on a fixed ellipse

Let \(\mathcal E_h\) be the filled spectral ellipse with
boundary \(X=2\cos(\vartheta+ih)\), and fix
\[
                            h=\frac18.
 \tag{9}
\]
Define
\[
 \mathcal R(X,Z)=
             \frac1{1-L_0(Z)(X+2)/4}.
 \tag{10}
\]

**Normalized-source theorem.** Uniformly for \(X\in\mathcal E_{1/8}\),
outputs (2), and both parities,
\[
 \boxed{\quad
 \frac{F_N^+(X,Z)}{\alpha_{M,N}(Z)}
                   =\mathcal R(X,Z)+O(N^{-1}).
 \quad}
 \tag{11}
\]
The denominator in (10) is nonzero on this filled ellipse.

Here is a proof retaining the entire finite sum. Put
\(k_0=\lfloor N/24\rfloor\). For \(1\le k\le k_0\), set
\[
 Q_{k,N}(X,Z)=
   (-q)\frac{C_{M+k,N}}{C_{M+k-1,N}}
                       \frac{c_{M+k-1}-X}{s_{M+k}^2}.
 \tag{12}
\]
The \(k\)-th normalized summand in (3) is exactly
\(\prod_{j=1}^{k}Q_{j,N}\); the \(k=0\) summand is one.

For sufficiently large \(N\), \(b=M+k\) in this range satisfies
\[
 0\le b/N-1/2\le1/16,\qquad s_b>19/10.
 \tag{13}
\]
For example \(M/N\le1/2+1/(2N)\), and \(N\ge24\) suffices
for the first inequality. For the second, \(\pi/16<1/5\)
and \(\cos x\ge1-x^2/2\) give
\(2\cos(\pi/16)>49/25>19/10\).
Equation (5) now implies
\[
 |C_{b,N}/C_{b-1,N}|<\sqrt{10/19}<3/4,
 \tag{14}
\]
where \(160<171\) proves the last squared comparison.

On the fixed ellipse,
\[
 |c_{b-1}-X|\le2+2\cosh(1/8)<33/8.
 \tag{15}
\]
The last bound follows already from the written
\(\cosh(1/4)<17/16\) witness in the original cubic source.
Combining (12)--(15) proves
\[
 |Q_{k,N}|
       <\frac{2475}{2888}<\frac78,\qquad1\le k\le k_0.
 \tag{16}
\]
The final rational comparison is \(19800<20216\).
The limiting increment
\[
                    x(X,Z)=L_0(Z)(X+2)/4
 \tag{17}
\]
also satisfies \(|x|<99/128<7/8\), by (6),(15).
This proves the denominator assertion in (10).

The ratio estimate (5), bounded first derivative of \(\mathcal L\),
and elementary derivatives of the trigonometric coefficients give
\[
                  |Q_{k,N}-x|\le C(k+1)/N
                       \qquad(1\le k\le k_0).
 \tag{18}
\]
More explicitly, \(-q=-1+O(N^{-1})\),
\(\mathcal L((M+k)/N,Z)=L_0+O((k+1)/N)\), and
\[
 \frac{c_{M+k-1}-X}{s_{M+k}^2}
                      =-\frac{X+2}{4}+O((k+1)/N)
 \tag{19}
\]
uniformly on the ellipse. Its denominator is bounded below
by (13), so these are additive uniform estimates at either
parity. The two minus signs in (12),(19) produce the positive
limiting factor in (17).

The telescoping difference of two products and (16)--(18) give
\[
 \left|\prod_{j=1}^{k}Q_{j,N}-x^k\right|
       \le \frac{Ck(k+1)}N(7/8)^{k-1}.
 \tag{20}
\]
Summing these bounds through \(k_0\) costs \(O(N^{-1})\).
The omitted infinite geometric tail of \(\sum_{k\ge0}x^k\)
is exponentially small.

It remains to justify the omitted actual summands
\(k>k_0\). The adopted physical Newton bound and exact
cardinal interpolation give
\(\|P_{M+k}^{\rm rad}\|_{[-2,2]}\le CN^A\)
uniformly through \(k=U\). Its degree is exactly \(k\).
The elementary Chebyshev coefficient estimate therefore gives
\[
               \|P_{M+k}^{\rm rad}\|_{\mathcal E_h}
                            \le CN^{A'}e^{hk}.
 \tag{21}
\]
This argument retains the literal zero values used in the
physical bound and includes the last Newton quotient.
Equations (8),(21) imply
\[
 \sum_{k>k_0}
  \left\|\frac{\alpha_{M+k,N}}{\alpha_{M,N}}
                        P_{M+k}^{\rm rad}\right\|_{\mathcal E_h}
       \le CN^{A''}e^{-(c_0-h)k_0}.
 \tag{22}
\]
Here \(c_0>h=1/8\). This tail is exponentially small relative
to the actual \(\alpha_{M,N}\), not merely absolutely small
at an unrelated rate. Combining (20)--(22) proves (11).

## 3. The actual positive Fourier coefficients of the limit

Put
\[
 d(Z)=\sqrt{1-L_0(Z)},\qquad
 \omega(Z)=\frac{d(Z)-1}{d(Z)+1},
 \tag{23}
\]
with the principal square root. By (6),
\[
 \Re d>1/2,\qquad |d|<3/2,\qquad
 |\omega|=\frac{|L_0|}{|d+1|^2}<1/3.
 \tag{24}
\]
Indeed \(\Re(1-L_0)>1/4\) implies \(\Re d>1/2\);
\(|1-L_0|<7/4\) implies \(|d|<3/2\).
All branch and denominator guards in (23) are thus strict.

In the original angular variable \(X=-2\cos u\), direct
factorization of the denominator in (10) gives
\[
 \boxed{\quad
 \mathcal R(-2\cos u,Z)
     =\frac1d\left[1+\sum_{k\ge1}\omega^k
                                      (e^{iku}+e^{-iku})\right].
 \quad}
 \tag{25}
\]
For example its denominator is
\(1-L_0/2+(L_0/2)\cos u\).
Using \(L_0=1-d^2\) and (23) reduces it to the
Poisson-kernel identity in (25). The series converges on
a neighborhood of the closed strip in (9), by (24).

Let \(d_{k,N}(Z)\) be exactly the positive Fourier coefficients
of the complete source, as normalized in the
[root-evaluation theorem, (15)--(17)](research_mixed_next_outer_fredholm_root_evaluations.md).
Thus the nonzero cosine coefficients are twice \(d_{k,N}\),
with the original \((-1)^k\) already included.
Cauchy's Fourier coefficient estimate applied to (11) on
the closed strip of height \(h=1/8\) gives
\[
 \boxed{\quad
 \left|\frac{d_{k,N}(Z)}{\alpha_{M,N}(Z)}
                           -\frac{\omega(Z)^k}{d(Z)}\right|
       \le \frac CN e^{-hk},\qquad k\ge0.
 \quad}
 \tag{26}
\]
For \(k>U\), define \(d_{k,N}=0\). The same estimate holds
there, since it is still the corresponding coefficient of
the difference in (11). Both Fourier signs in (25) are
retained; no positive-frequency part is identified with
the full spectral evaluation.

## 4. A nonzero frozen compatibility at the half-action scale

Use the first-crossing full-symbol functional and its
unshifted root multiset
\(\sigma_1(\tau),\ldots,\sigma_{12}(\tau)\) from
[the root-evaluation theorem](research_mixed_next_outer_fredholm_root_evaluations.md).
Shrink its left endpoint neighborhood, if necessary, so that
\[
                  0<h_1(\tau)<1/16 .
 \tag{27}
\]
For any allowed constant shift
\(h_1(\tau)<\lambda<h_2(\tau)\), the shifted roots are
\(\rho_j=e^{-\lambda}\sigma_j\), and
\(\max_j|\sigma_j|=e^{h_1(\tau)}\).
Fix any \(0<\alpha_0<1/2\), and retain all truncations
\[
                       \alpha_0N\le K_N\le U .
 \tag{28}
\]
The exact forward source functional is
\[
 \mathfrak D_{0,K_N,N}(\tau,Z)
   =\ell_\rho((e^{\lambda k}d_{k,N})_{0\le k\le K_N})
   =\sum_{k=0}^{K_N}\mathfrak h_k(\sigma)d_{k,N}.
 \tag{29}
\]
The radial-weight cancellation in the second equality is exact.

**Compatibility asymptotic.** Uniformly in (2), (27)--(28),
at both parities and for all shifts in the first-crossing chamber,
\[
 \boxed{\quad
 \mathfrak D_{0,K_N,N}(\tau,Z)
     =\alpha_{M,N}(Z)\,
       \mathcal B(\tau,Z)\,(1+O(N^{-1})),\qquad
 \mathcal B(\tau,Z)=
       \frac1{d(Z)\prod_{j=1}^{12}(1-\omega(Z)\sigma_j(\tau))}.
 \quad}
 \tag{30}
\]
In particular \(\mathcal B\) is uniformly bounded above and
away from zero. No separation of the twelve roots is required.

To prove (30), multiply the errors in (26) by the exact
root coefficient bound
\[
 |\mathfrak h_k(\sigma)|
       \le {k+11\choose11}e^{h_1(\tau)k}.
 \tag{31}
\]
Since \(h-h_1(\tau)>1/16\), their full sum is \(O(N^{-1})\),
uniformly even as roots coalesce at the limiting frequency.
For the limiting coefficients, (24),(27) imply
\[
 |\omega|\max_j|\sigma_j|<\frac{16}{45}<1.
 \tag{32}
\]
Here \(e^{1/16}<16/15\) follows from
\(\sum_{n\ge0}(1/16)^n/n!\le\sum_{n\ge0}(1/16)^n\),
with strict inequality. The exact generating identity
therefore gives
\[
 \frac1d\sum_{k\ge0}\mathfrak h_k(\sigma)\omega^k
           =\frac1{d\prod_j(1-\omega\sigma_j)}.
 \tag{33}
\]
Its tail beyond \(K_N\) is at most a fixed polynomial in
\(K_N+1\) times \((16/45)^{K_N}\).
Condition (28) makes it exponentially small, uniformly over
all the allowed truncations. This proves (30) with an additive
\(O(N^{-1})\) error after dividing by \(\alpha_{M,N}\).

Finally (24),(32) give explicit nonzero bounds
\[
 \frac23\left(\frac{45}{61}\right)^{12}
       <|\mathcal B(\tau,Z)|
       <2\left(\frac{45}{29}\right)^{12}.
 \tag{34}
\]
The additive error is therefore relative as stated.
Together with (7), this proves the two-sided rate
\[
 cN^{-1/2}e^{NE_0(Z)}
       \le|\mathfrak D_{0,K_N,N}(\tau,Z)|
       \le CN^{-1/2}e^{NE_0(Z)}
 \tag{35}
\]
for all sufficiently large \(N\). Thus this frozen
compatibility is nonzero on the entire stated actual output
family and is not exponentially smaller than its original
outgoing half-input row.

## 5. What the asymptotic does not remove

The functional in (29) is the specified frozen forward
half-line range condition. At the actual positive Fourier
hard endpoint, inward reindexing reverses the symbol and
produces a kernel rather than this cokernel. Equation (35)
does not identify the two boundary problems.

Nor does it estimate the boundary corrections in a factor
construction. The exact relation remains
\[
 T(P_\lambda)=T(A)T(B)+K,\qquad K_{4,4}=1,
 \qquad
 \ell_B(T(A)^{-1}f)
   =\sum_{j=0}^4v_j\,\ell_B(T(A)^{-1}Ke_j),
 \tag{36}
\]
with the notation and finite support of the adopted range
theorem. These correlated responses may have the same
action scale. They have not been discarded or bounded by
(35). All original Hermite forcing, opposite-grid data when
a half-step is used, and the finite output modes remain
separate obligations.

The conclusion rules out the shortcut that this exact
complete outgoing family has an exponentially small full
forward bad component merely because its high coefficients
decay. It does not lower-bound the signed inner observation,
disprove a bilinear cancellation estimate, or establish a
finite-exception theorem.

## Frozen source versions

- Complete finite ratio and metric contraction:
  2bf8a2f401b3472da0d250c97403fa776396e3dd524bd149a9209b6f8eacdeaf.
- Absolute normalization from the literal terminal row:
  51c9e5f1a47be3d9f3e1fa756e390a98c07f84c33f1aa0ad5ee5b948771229ab.
- Complete attached source, Newton bounds and ellipse continuation:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.
- Original uniform action loss \(205/1134\):
  fab5571d039f9fa4e36c0b6ca981f4ebbd2e7384923249882cf22e58eccc8ba3.
- Exact forward functional, weight cancellation and original
  Fourier normalization:
  cf48af3535fc99a4ffb1df782e3cc42e8d0445a2fe7fb16d87a81474cd62512d.
- Exact frozen factor boundary terms and reflection scope:
  6f6a411d7788f2727e3261195bb2a8e46871c631d6f86fab5b2cbb26ed2507a5.
