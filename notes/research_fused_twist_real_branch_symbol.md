# Uniform bulk coefficient noncancellation for the fused full-Hermite twist

Private written proof, 14 November 2026. This gives a quantitative
two-term expansion for the actual finite Fresnel branches, including
their normal weight. For every fixed signed power, the original
Chebyshev coefficients have a uniform inverse-polynomial lower bound
throughout any fixed interior physical-color interval. Their explicit
normal endpoint term survives even when the leading finite Gaussian
sum cancels. No numerical evaluation, test, or frozen-manuscript
change is used.

Use the exact finite-branch identity in
[the full-Hermite reciprocity note](research_full_hermite_gauss_reciprocity.md).
Put \(p\in\mathbb Z\setminus\{0\}\), \(h=|p|\),
\(N\ge2\), \(a=n/N\), and
\[
 G_{p,N}=\frac{e^{i\operatorname{sgn}(p)\pi/4}}{\sqrt{2hN}},
 \qquad s(u)=\frac12-\{u\}\quad(u\notin\mathbb Z).
 \tag{1}
\]
Values at jumps do not affect the integrals. For
\(0\le r<2h\), retain the original branch data
\[
 B_r=\frac12-\frac{a+r}{2p},\qquad
 C_r=(-1)^r\exp\left[-\pi i(n+Nr)
                   -\frac{\pi i(n+Nr)^2}{2pN}\right].
 \tag{2}
\]
Specifically, in the original full algebra
\(\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)\), write the
unique degree-less-than-\(N\) representative as
\(\operatorname{rem}(r_N^{2p})(z)=a_0+
\sum_{n=1}^{N-1}a_n\,2T_n(z/2)\).
The exact canonical coefficients are
\[
 a_n=\kappa^{-p}\sum_{r=0}^{2h-1}C_r
  \operatorname{PV}\int_{\mathbb R}
   [1-a+2p\,s(B_r-v)]e^{2\pi ipNv^2}\,dv,
 \quad 0\le n<N.
 \tag{3}
\]
Here \(\kappa=q^{(N-1)^2/2}\), \(q=e^{\pi i/N}\), with
this fixed logarithm. The actual physical power is \(R^{2p}\),
whose coefficient is \(\kappa^{2p}a_n\); that scalar is retained
and has modulus one.

## 1. A paired integration-by-parts lemma

**Lemma 1.** Suppose \(B\in\mathbb R\setminus\mathbb Z\),
\(2pNB\in\mathbb Z\), and
\(\delta=\operatorname{dist}(B,\mathbb Z)>0\). Then
\[
 \operatorname{PV}\int_{\mathbb R}s(B-v)e^{2\pi ipNv^2}\,dv
       =s(B)G_{p,N}
        +\frac{e^{2\pi ipNB^2}\cot(\pi B)}{4ipN}
        +O\left(\frac1{h^2N^2\delta^3}\right).
 \tag{4}
\]
The implicit constant is absolute. In particular the difference
from \(s(B)G_{p,N}\) is \(O((hN\delta)^{-1})\).

*Proof.* Set \(b=\{B\}\in(0,1)\), and pair positive and
negative integration variables. Subtracting \(s(B)G_{p,N}\)
from the integral in (4) gives
\[
 \int_0^\infty f_b(v)e^{2\pi ipNv^2}\,dv,
 \quad
 f_b(v)=s(b-v)+s(b+v)-2s(b).
 \tag{5}
\]
The function \(f_b\) is piecewise constant, has absolute value
at most two, and vanishes for \(0<v<\delta\). Its jumps are
\(+1\) at \(m+1-b\) and \(-1\) at \(m+b\),
\(m=0,1,\ldots\). Coincident opposite jumps cancel.

Since \(2pNb\) is an integer, every jump has the same Gaussian
phase:
\[
 e^{2\pi ipN(m+b)^2}
 =e^{2\pi ipN(m+1-b)^2}=e^{2\pi ipNb^2}.
 \tag{6}
\]
Integrate (5) by parts on each constant interval using
\((e^{2\pi ipNv^2})'=4\pi ipNv e^{2\pi ipNv^2}\).
The endpoint at zero vanishes because \(f_b=0\) nearby, and
the endpoint at a large cutoff tends to zero. The resulting
distributional derivative of \(f_b(v)/v\) has its jump sum and
an ordinary integral involving \(-f_b(v)/v^2\). The latter has
absolute value at most \(2/\delta\). The jump sum converges in
the order of increasing positive positions, because
\[
 \begin{split}
 \sum_{m\ge0}\left\{\frac1{m+1-b}-\frac1{m+b}\right\}
   &=-\pi\cot(\pi b),\\
 |\pi\cot(\pi b)|&\le\frac{\pi}{2\delta}.
 \end{split}
 \tag{7}
\]
The first identity is the paired partial-fraction expansion of
cotangent; it also follows by subtracting the logarithmic
derivatives of the sine product. The omitted unpaired last term
at a cutoff tends to zero. Keeping the signs in this integration
by parts gives
\[
 \int_0^\infty f_b(v)e^{2\pi ipNv^2}\,dv
 =\frac{e^{2\pi ipNb^2}\cot(\pi b)}{4ipN}
   +\frac1{4\pi ipN}\int_0^\infty
                       \frac{f_b(v)}{v^2}e^{2\pi ipNv^2}\,dv.
 \tag{7a}
\]
The last integral is absolutely convergent. Integrating it once
more by parts produces jump weights \(1/v^3\), whose absolute
sum is \(O(\delta^{-3})\), and an ordinary integral with
amplitude \(3f_b(v)/v^4\), also of absolute size
\(O(\delta^{-3})\). It is therefore
\(O((hN\delta^3)^{-1})\). This proves (4), including its
second-order remainder. The phases with \(B\) and \(b\) agree,
again by the integer hypotheses. The first integration also proves
existence of the paired limit in (5). \(\square\)

The integer condition in the lemma is satisfied by each actual
branch: \(2pNB_r=pN-n-Nr\). The proof does not replace its
discontinuous normal amplitude by a holomorphic continuation.

## 2. The actual branch has an integer leading coefficient

Fix \(0<\epsilon<1/2\) and restrict to the physical integers
\(n\) with \(\epsilon\le n/N\le1-\epsilon\).
For every branch,
\[
 \operatorname{dist}(B_r,\mathbb Z)\ge\frac{\epsilon}{2h}.
 \tag{8}
\]
Indeed \(2pB_r=p-r-a\) is an integer minus \(a\).
Lemma 1 and (3) therefore give a uniform branch estimate
\[
 \operatorname{PV}\int_{\mathbb R}
 [1-a+2p\,s(B_r-v)]e^{2\pi ipNv^2}\,dv
       =c_rG_{p,N}
        +\frac{e^{2\pi ipNB_r^2}\cot(\pi B_r)}{2iN}
        +O_{p,\epsilon}(N^{-2}),
 \tag{9}
\]
where its leading coefficient is the literal integer
\[
 c_r=1-a+2p\,s(B_r)=1+r+2p\lfloor B_r\rfloor
 =\begin{cases}
      r+1,&0\le r<h,\\
      r+1-2h,&h\le r<2h.
   \end{cases}
 \tag{10}
\]
The last expression holds for either sign of \(p\) throughout
\(0<a<1\). Thus exactly one of the \(2h\) branches has zero
Gaussian leading coefficient, and the others have coefficients
\(1-h,\ldots,-1,1,\ldots,h\).

The endpoint terms can be summed exactly. Since \(n+Nr\) is
an integer, direct completion of the same square gives
\[
 C_r e^{2\pi ipNB_r^2}=(-1)^r e^{\pi ipN/2}.
 \tag{10a}
\]
The elementary alternating cotangent identity gives
\[
 \sum_{r=0}^{2h-1}(-1)^r\cot(\pi B_r)
       =2p(-1)^{p+1}\csc(\pi a).
 \tag{10b}
\]
To verify its phase, for any even integer \(M\) subtract the
odd-indexed part of the usual multiplication identity
\(\sum_{r=0}^{M-1}\cot(x+r\pi/M)=M\cot(Mx)\)
from its even-indexed part. The result is
\(\sum_r(-1)^r\cot(x+r\pi/M)=M\csc(Mx)\).
Apply it with \(M=2h\) and \(x=\pi/2-\pi a/(2p)\),
reversing the cyclic residue order when \(p>0\).

Consequently the entire canonical coefficient has the uniform
two-term expansion
\[
 \boxed{a_n=\kappa^{-p}G_{p,N}
       \sum_{r=0}^{2h-1}c_rC_r
       +\frac{ip\,q^{-p/2}}{N\sin(\pi n/N)}
       +O_{p,\epsilon}(N^{-2}).}
 \tag{11}
\]
In the unsimplified original phases the middle term is
\(i(-1)^p p\kappa^{-p}e^{\pi ipN/2}/(N\sin(\pi a))\).
The equality with the displayed phase uses
\((N-1)^2/(2N)=N/2-1+1/(2N)\) and the fixed logarithm of
\(q\). Thus no phase is absorbed into a normalization.

This estimate uses the actual normal data through (3), not the
value-only quadratic Gauss sum. All phases in \(C_r\) remain.

## 3. All original bulk coefficients have a lower bound

**Theorem 2.** For every fixed \(p\ne0\) and
\(0<\epsilon<1/2\), there are \(c_{p,\epsilon}>0\) and
\(N_{p,\epsilon}\) such that
\[
 \boxed{|a_n|\ge\frac{c_{p,\epsilon}}N}
 \tag{12}
\]
for all \(N\ge N_{p,\epsilon}\) and all integers
\(\epsilon N\le n\le(1-\epsilon)N\).
The same bound holds for the actual coefficient
\(\kappa^{2p}a_n\) of \(R^{2p}\).

*Proof.* Factor \(C_0\), which has modulus one, out of the
leading sum. Its remaining factor is
\[
 F_p(N,n)=\sum_{r=0}^{2h-1}c_r(-1)^{(N+1)r}
       \exp\left[-\frac{\pi inr}{p}
                 -\frac{\pi iNr^2}{2p}\right].
 \tag{12a}
\]
It depends only on \(n\) modulo \(2h\) and \(N\) modulo
\(4h\). Hence its nonzero values form a finite set bounded
away from zero. If \(F_p(N,n)\ne0\), the first term in (11)
has size at least a fixed positive multiple of \(N^{-1/2}\),
while the remaining terms are \(O_{p,\epsilon}(N^{-1})\).
For all sufficiently large levels this gives a uniform lower bound
of order \(N^{-1/2}\).

If \(F_p(N,n)=0\), the exact endpoint term in (11) has modulus
\(h/(N\sin(\pi n/N))\ge h/N\), and its error is
\(O_{p,\epsilon}(N^{-2})\). Thus it has modulus at least
\(h/(2N)\) for all sufficiently large levels. Both cases give
(12), uniformly over the prescribed range. The physical scalar
has modulus one. \(\square\)

For \(p=1\) or \(p=-1\), equation (10) gives \(c_0=1\)
and \(c_1=0\). Therefore the sharper bound is
\[
 \boxed{a_n=\kappa^{-p}C_0G_{p,N}+O_\epsilon(N^{-1}),
 \qquad |a_n|=(2N)^{-1/2}+O_\epsilon(N^{-1}).}
 \tag{13}
\]
The original coefficient is nonzero for every sufficiently large
level and every physical color in the indicated interval, with
no parity or coprimality exception. This is a statement about the
specified canonical Chebyshev coefficient of the original power,
not an arbitrary exterior observation.

The coherent finite sum in (11) can vanish at larger powers.
For example take \(p=2\), \(N\equiv6\pmod8\), and
\(n\equiv1\pmod4\) in the same interior range. Directly from
(2),
\[
 C_1/C_0=-1,\qquad C_2/C_0=-1,
 \qquad (c_0,c_1,c_2,c_3)=(1,2,-1,0).
\]
Hence \(\sum_rc_rC_r=0\), but (11) now gives the actual
nonzero endpoint asymptotic
\[
 a_n=\frac{2i q^{-1}}{N\sin(\pi n/N)}+O_\epsilon(N^{-2}).
 \tag{14}
\]
The retained normal term is what proves noncancellation in this
residue class. Separate nonzero Gaussian symbols would miss it.

## 4. Scope for the geometric problem

Equations (9)--(14) provide actual coefficient noncancellation and
a controlled normal remainder on real physical colors. They do
not transport this estimate to a fixed complex geometric color.
These are first-kind Chebyshev coefficients. The original ordinary
circle coefficients are \(\beta_j=(-1)^j(a_j-a_{j+2})\), with
the actual zero endpoint convention. Their differences can cancel;
no lower bound for \(\beta_j\) is inferred from (12).
The exact residue-class identity itself uses integer color, and
its sawtooth branch prescription changes away from that grid.
The separately proved
[complex-color endpoint calculation](research_fresnel_circle_endpoint_dominance.md)
shows why a naive replacement by complete Gaussians is not an
exponential approximation after such a displacement.

Thus the constructive advance is a source-specific two-term
symbol and a uniform lower bound for every original bulk coefficient
of each fixed signed full-twist power.
To prove arbitrary fixed short-filling stability one still needs
the actual complex continuation and coherent exterior contraction.
No statement about a knot's geometric coefficient or volume is
inferred from (12).

## Direct source version

The reciprocity note was read in full at SHA-256
`ccd241bfcd15e9855ea9aaa10e65c84697874c36149d894edf3ff8dfa2300ee1`.
Its original full-Hermite source and Gaussian phase conventions
are those of `actual_twist_circle_fourier_kernel.md` and
`actual_coherent_filling_gaussian_chirp.md`, as pinned there.
