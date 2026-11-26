# The selected amplitude of the exact finite clock contraction

Private written proof, 15 November 2026. No mathematical code,
numerical calculation, test, or saved numerical evidence is used.
Frozen notes and public manuscripts are unchanged.

The complete singleton clock contraction has an all-orders relative
asymptotic on a complex domain containing the physical interior
colors. Its leading amplitude is explicit and nonzero. With the
canonical Fourier character retained, that amplitude is precisely
the normalized Gaussian amplitude of the clock critical point,
with coefficient one. This is proved for the actual finite
contraction, including both endpoints, by evaluating its exact
Pochhammer product.

The conclusion concerns the clock contraction conditional on the
physical colors. It does not assert that the remaining physical
color sum of an arbitrary short tangle has a nonzero geometric
contribution.

## 1. Sources and the exact contraction

The direct written sources are:

* [Joint clock phase](research_joint_clock_phase_equations.md),
  SHA-256
  71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867:
  the full original source, exact clock sum (19), canonical
  primitive (27e)--(27g), and clock Hessian (27i).
* [Exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md),
  SHA-256
  1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72:
  its specified nonzero function \(G_N\), lattice values,
  reflection, marked complex expansion, and finite residue cycle.
* [Root-Pochhammer interpolation](research_root_pochhammer_interpolation.md),
  SHA-256
  46c1a27ca67045f6afdd2fd695f74b735ec611eabedb6f07b50b9bfbaccad4e2:
  the existing all-orders product expansion on disk charts.

The last source already establishes the general asymptotic method.
The additional statement here is the selected amplitude and its
Gaussian normalization for this complete original clock contraction,
on the physical strip and its complex neighborhoods.

Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\qquad
 S_a=\prod_{r=1}^a2\sin(\pi r/N),\quad S_0=1.
 \tag{1}
\]
Let \(u,v\) be nonnegative integers with \(u+v\le d\), and set
\(U=u/N,\ V=v/N\). The sign \(\sigma\in\{1,-1\}\) is the
physical sign, as in the joint clock source. Write the lifted
complex undercolor as \(j\), with
\[
                        T=e^{2\pi i j}.
 \]
At an original physical state \(j=J/N\), where \(J\) is the
integer under-input degree. Define
\[
 a_{\sigma,N}(U,j)
       =\exp\{\sigma\pi i(U+2j-1+1/N)\}
       =-q^{\sigma(u+1)}T^\sigma ,
 \]
and keep the entire finite clock sum
\[
 C_{\sigma,N}(u,v;j)=
       \sum_{h=v}^{u+v}
       \frac{a_{\sigma,N}(U,j)^h}
            {S_{h-v}S_{u-h+v}} .                         \tag{2}
\]
This is the exact clock sum from the original source. For the
positive sign its chosen exponential lift differs from the
source's initial lift by \(-2\pi i h\); for the negative sign
it is the initial lift. Since \(h\) is integral, (2) is
unchanged. This is the canonical Fourier character already
fixed by the joint action calculation.

The finite binomial identity proves, for every nonzero complex
\(T\), not just for its physical samples,
\[
 \begin{split}
 C_{\sigma,N}
   &=\frac{a_{\sigma,N}^{\,v}}{S_u}\,P_{\sigma,N}(u,j),\\
 P_{\sigma,N}(u,j)
   &=\prod_{r=1}^u(1-e^{2\pi i\sigma(j+r/N)}).
 \end{split}                                             \tag{3}
\]
For \(\sigma=1\) the product is \((TQ;Q)_u\). For
\(\sigma=-1\) it is
\((T^{-1}Q^{-u};Q)_u\), with its factors reversed.
Thus (3) is exactly the two products of the prior clock
theorem, including their first shifts and both endpoints.

## 2. Complex domain and all-orders product estimate

Use the open parameter domain
\[
 \mathfrak D=\{(U,j):U\in(0,1),\
                         0<\operatorname{Re}j<
                                \operatorname{Re}(j+U)<1\}.
 \tag{4}
\]
Here \(U\) is real and is evaluated on \(u/N\); \(j\) is
complex. Uniformity means compact subsets of (4), with
the original allowed \(v\)'s, \(0\le v\le d-u\).
For example one can impose
\[
 U\ge\epsilon,\quad \operatorname{Re}j\ge\epsilon,\quad
 \operatorname{Re}(j+U)\le1-\epsilon,\quad
 |\operatorname{Im}j|\le M .
 \tag{5}
\]
In terms of \(T\), this is a specified nonzero domain with
argument lift \(2\pi\operatorname{Re}j\), bounded modulus,
and no zero of any product arc in (3). It includes every
compact subset of the physical interior
\(0<U,\ 0<j,\ j+U<1\). No uniformity through its integer
divisors is claimed.

On \(0<\operatorname{Re}z<1\), set
\[
 s(z)=2\sin\pi z,\qquad
 \ell(z)=\Log s(z),\qquad
 \mathcal J(z)=\int_0^z\ell(t)\,dt,
 \tag{6}
\]
with the principal analytic logarithm and the primitive
real on \((0,1)\), \(\mathcal J(0)=0\). The sine has
positive real part in this strip, so these marks are
unambiguous. Define
\[
 f_\sigma(z)=\ell(z)+\sigma\pi i(z-1/2).
 \tag{7}
\]
Then \(e^{f_\sigma(z)}=1-e^{2\pi i\sigma z}\). These
are the logarithms used for every factor of (3).

Let \(B_{2r}\) be the Bernoulli numbers, \(B_2=1/6\).
For every fixed \(p\ge0\), Euler summation gives
\[
 \begin{split}
 \log P_{\sigma,N}
 ={}&N\int_0^U f_\sigma(j+t)\,dt
           +\frac{f_\sigma(j+U)-f_\sigma(j)}2\\
 &+\sum_{r=1}^p
   \frac{B_{2r}}{(2r)!\,N^{2r-1}}
     \{\ell^{(2r-1)}(j+U)-\ell^{(2r-1)}(j)\}\\
 &+O(N^{-2p-1}).
 \end{split}                                             \tag{8}
\]
The logarithm on the left is the actual sum of the
marked factor logarithms, not an independent logarithm
of the final product. The estimate is uniform on the
compacts specified above. Every fixed \(j\)-derivative
of the normalized remainder obeys the same bound on a
smaller compact neighborhood.

For a direct remainder proof, apply the finite
Euler--Maclaurin identity through its \(p+1\) term.
The derivatives of \(f_\sigma\) through order \(2p+2\)
are uniformly bounded on the compact union of arcs
\(j+[0,U]\). Its integral remainder and last term are
\(O(N^{-2p-1})\); absorb that last term. This proves
(8). The linear term of \(f_\sigma\) contributes no
derivative difference in (8), including when \(r=1\).
Holomorphy and Cauchy's formula prove the derivative
assertion. In particular this proof applies on both
sides of the unit circle in \(T\), rather than only
on the disk chart of the earlier interpolation note.

The corresponding all-orders real factorial formula is
\[
 \log S_u=N\mathcal J(U)+\frac12\log(Ns(U))
  +\sum_{r=1}^p
       \frac{B_{2r}\ell^{(2r-1)}(U)}
            {(2r)!\,N^{2r-1}}
       +O(N^{-2p-1}).                                   \tag{9}
\]
Here \(U\) lies in a compact subset of \((0,1)\).
One proof, including the normalization, is to write
\(\ell(t)=\log(2\pi t)+g(t)\), where \(g\) is smooth at
zero and every odd derivative of \(g\) vanishes there.
Apply Stirling's expansion with remainder to
\((2\pi/N)^u u!\), and Euler--Maclaurin to
\(\sum_{r=1}^u g(r/N)\). The endpoint terms combine to
\(\frac12\log(Ns(U))\); the odd derivatives of
\(\log(2\pi U)\) in Stirling combine with those of
\(g(U)\) to give exactly (9). Taking one further
Bernoulli term bounds the stated remainder. The first
correction is \(\pi\cot(\pi U)/(12N)\), agreeing with
the exact factorial interpolation.

## 3. The selected clock amplitude

Define
\[
 \begin{split}
 W_\sigma(U,V,j)
   ={}&\mathcal J(j+U)-\mathcal J(j)-\mathcal J(U)\\
     &+\sigma\pi i\{V(U+2j-1)+jU+U^2/2-U/2\},\\
 A_\sigma(U,V,j)
   ={}&e^{\sigma\pi i(V+U/2)}
       \exp\left\{\frac{\ell(j+U)-\ell(j)-\ell(U)}2\right\},\\
 D_m(U,j)
   ={}&\ell^{(m)}(j+U)-\ell^{(m)}(j)-\ell^{(m)}(U).
 \end{split}                                             \tag{10}
\]
All powers and square roots mean these displayed logarithms.
In particular \(A_\sigma\) is holomorphic and nonzero
throughout (4).

**Theorem 1.** For every fixed \(p\ge0\), the exact finite
sum (2) satisfies
\[
 \boxed{\displaystyle
 C_{\sigma,N}
  =N^{-1/2}A_\sigma e^{NW_\sigma}
       \exp\left\{
         \sum_{r=1}^p
          \frac{B_{2r}D_{2r-1}(U,j)}
               {(2r)!\,N^{2r-1}}
            +O(N^{-2p-1})\right\}.}                     \tag{11}
\]
The estimates are uniform on every compact in (4),
uniformly in all allowed \(v\), and hold with every
fixed complex-undercolor derivative of the normalized
error. Exponentiating the finite correction series
gives a full relative expansion in integral powers of
\(N^{-1}\).

Indeed
\[
 a_{\sigma,N}^{\,v}
  =e^{N\sigma\pi iV(U+2j-1)}e^{\sigma\pi iV}.
 \]
Insert (7)--(9) into the exact identity (3). The
integral of the linear part of (7) gives
\(\sigma\pi i(jU+U^2/2-U/2)\); its half-endpoint
difference gives \(\sigma\pi iU/2\).
These are exactly (10)--(11). No endpoint summand
has been estimated away.

On a compact parameter set there are constants
\(0<c_K<C_K<\infty\) such that, for all sufficiently
large \(N\),
\[
 c_K N^{-1/2}e^{N\operatorname{Re}W_\sigma}
       \le |C_{\sigma,N}|
       \le C_K N^{-1/2}e^{N\operatorname{Re}W_\sigma}.
 \tag{12}
\]
In fact \(C_{\sigma,N}\ne0\) at every level on (4),
already by (3). The new information in (11)--(12) is
the exact selected rate, power, nonzero amplitude,
and all relative corrections.

The theorem is a statement about the complete original
clock contraction conditional on the undercolor. It
does not replace that undercolor by an optimizer or
alter its subsequent physical sum.

## 4. The actual residue period and its Gaussian normalization

This asymptotic also applies to a specified exact
cycle, without choosing a cycle from a critical point.
Let \(G_N(z)\) be the nonzero sine-factorial
interpolation of the direct source, normalized by
\(G_N(a)=S_a\) for integers \(0\le a<N\). Define
\[
 I_{\sigma,N}(h)=
 \frac{\exp\{\sigma\pi i(U+2j-1+1/N)h\}}
      {G_N(h-v)G_N(u-h+v)} .
 \tag{13}
\]
It agrees with the summand of (2) at every allowed
integer. Choose small positively oriented circles
about \(h=v,\ldots,v+u\), containing no other integer
or interpolation pole, and let \(\Gamma_N\) be their
oriented sum. Then
\[
 C_{\sigma,N}
       =\frac1{2\pi i}\int_{\Gamma_N}
                       I_{\sigma,N}(h)\pi\cot(\pi h)\,dh.
 \tag{14}
\]
This follows directly from the residues, including
the two endpoint residues. The Fourier-character
choice in (13) is specified explicitly; it equals
the literal summand on every residue. It is not
being imposed on an unrelated exterior continuation.

For real physical parameters \(0<U,\ 0<j<j+U<1\),
put
\[
 R_\sigma=\frac U2-\frac{\sigma i}{2\pi}
                  \log\frac{s(j+U)}{s(j)},\qquad
 H_\sigma=V+R_\sigma .
 \tag{15}
\]
This is the canonical clock critical point already
derived from the original source. The corrected
clock action, before evaluating it there, is
\[
 F_\sigma(R)=-\mathcal J(R)-\mathcal J(U-R)
                +\sigma\pi i(V+R)(U+2j-1).
 \tag{16}
\]
The prior primitive calibration, or its elementary
specialization after subtracting the two unchanged
outer factorials, gives
\[
 F_\sigma'(R_\sigma)=0,\quad
 F_\sigma(R_\sigma)=W_\sigma,\quad
 F_\sigma''(R_\sigma)
        =-\frac{2\pi s(U)}
                    {s(R_\sigma)s(U-R_\sigma)} .
 \tag{17}
\]
The Hessian is negative real on this physical domain,
since \(U-R_\sigma=\overline{R_\sigma}\). It has no
zero on the continued regular clock chart.

The exact factorial interpolation, at \(h=N(V+R)\),
has the local summand expansion
\[
 I_{\sigma,N}(N(V+R))
 =\frac1N
     \frac{e^{\sigma\pi i(V+R)}}
          {\sqrt{s(R)s(U-R)}}
        e^{NF_\sigma(R)}\{1+O(N^{-1})\}.                \tag{18}
\]
It is uniform and holomorphic near the critical
point. The square roots use the same factorial
logarithms. The lattice measure is \(N\,dR\).
Consequently its normalized one-dimensional Gaussian
model has leading amplitude
\[
 \begin{split}
 A_{\rm G}
  &=\frac{e^{\sigma\pi iH_\sigma}}
             {\sqrt{s(R_\sigma)s(U-R_\sigma)}}
       \sqrt{\frac{2\pi}{-F_\sigma''(R_\sigma)}}\\
  &=\frac{e^{\sigma\pi iH_\sigma}}{\sqrt{s(U)}}
   =A_\sigma .
 \end{split}                                             \tag{19}
\]
The Gaussian root is positive at physical real
parameters and then continued. The last equality
uses (15): \(e^{\sigma\pi iR_\sigma}
=e^{\sigma\pi iU/2}\sqrt{s(j+U)/s(j)}\).

There is also a direct real-lattice base point fixing this
Gaussian coefficient. Set \(j_0=(1-U)/2\). The exact
normalized Fourier lift in (2), without any further change
of phase, is then \(a_{\sigma,N}=e^{\sigma\pi i/N}\).
Writing \(r=h-v\), the complete sum is
\[
 C_{\sigma,N}(u,v;j_0)
   =\sum_{r=0}^{u}
       \frac{e^{\sigma\pi i(V+r/N)}}{S_rS_{u-r}} .
 \tag{19a}
\]
The support is the real integer interval \(h=v,\ldots,v+u\),
including both endpoints. This slice belongs to the exact
undercolor continuation; it is itself a physical undercolor
when \((N-u)/2\) is integral. Centering the phase in (19a)
puts every summand in the half-plane
\[
 \operatorname{Re}
     e^{-\sigma\pi i(V+U/2)}C_{\sigma,N}(u,v;j_0)
 \ge
 \cos(\pi U/2)\sum_{r=0}^{u}\frac1{S_rS_{u-r}}>0.
 \tag{19b}
\]
No cancellation is possible at this base point.

More precisely, on \(0<R<U\) its real entropy is
\[
 E_U(R)=-\mathcal J(R)-\mathcal J(U-R),\qquad
 E_U''(R)=
   -\frac{\pi\sin(\pi U)}
          {\sin(\pi R)\sin(\pi(U-R))}<0 .
 \tag{19c}
\]
It extends continuously to \([0,U]\), is symmetric about
\(U/2\), and has its unique maximum there. Uniformly for
\(U\) in a compact subset of \((0,1)\), there is a strict
entropy gap outside any fixed sufficiently small
neighborhood of \(U/2\). The same factorial splitting used
for (9), with the crude Stirling remainder and a bounded
sum-to-integral error for \(g\), gives
\[
 \log S_k=N\mathcal J(k/N)+O(\log N),
       \qquad 0\le k\le u\le(1-\epsilon)N .
 \tag{19d}
\]
At \(k=0\) this is immediate; the estimate for \(k\ge1\)
is uniform down to \(k=1\). Thus all summands outside
that neighborhood, including both endpoints, are
exponentially smaller than the central contribution,
up to a fixed polynomial factor.

Inside the neighborhood, (9) gives the density in (18)
with real \(R\). Rescale \(r-u/2\) by \(\sqrt N\).
Strict concavity supplies an integrable Gaussian bound,
and the resulting Gaussian Riemann sums converge with
either parity of \(u\). Consequently the actual lattice
sum, with its positive orientation, satisfies
\[
 C_{\sigma,N}(u,v;j_0)
  =N^{-1/2}e^{NE_U(U/2)}
       \frac{e^{\sigma\pi i(V+U/2)}}{\sqrt{s(U)}}
       \{1+o(1)\}.
 \tag{19e}
\]
The error is uniform on those compact \(U\)-sets and
over all allowed \(v\). The coefficient is one by this
ordinary lattice Laplace argument, not by a freely
chosen square root or cycle orientation. Formula (11)
continues the marked selected expansion from this
base slice throughout (4); its proof by the exact
product provides the uniform complex estimates, without
an assumption about transport of individual thimbles.

Equations (11), (14), and (19) prove that the
**actual finite residue period** has this selected
Gaussian symbol with coefficient one. There is no
unknown local multiplier to be supplied from a
nonvanishing conjecture. This conclusion is stronger
than existence of a stationary point or a nonzero
pointwise density: the exact period itself has the
relative expansion (11).

It does not assert an independently proved
one-thimble homology decomposition of \(\Gamma_N\).
The proof evaluates the whole period algebraically
by (3), so possible endpoint or Fourier-sector
effects have already been included. Equality of
its leading coefficient with (19) must not be
used to discard such sectors in a different
coupled exterior period.

## 5. The full physical row, with its Cartan scalar retained

For the complete row also restrict \(V\) and \(U+V\)
to compact subsets of \((0,1)\). The exact clock
source multiplies (2) by its remaining factors:
\[
 \mathcal R_{\sigma,N}(u,v;j)
   =\kappa^\sigma\frac{S_{u+v}}{S_v}
                      e^{-\sigma\pi i d j}C_{\sigma,N},
 \qquad \kappa=q^{d^2/2}.                              \tag{20}
\]
This follows from its original factor
\(N/(S_{d-u-v}S_v)\) by exact reflection.
At \(j=J/N\), (20) is the literal physical crossing
coefficient, with over-input \(u+v\), over-output \(v\),
under-input \(J\), and transfer \(u\). At complex \(j\)
it is the specified continuation of that same finite
product and Cartan mark.

Let \(G_\sigma(U,V,j)\) be the physical action (27a)
of the joint clock note. Explicitly,
\[
 \begin{split}
 G_\sigma
   ={}&\mathcal J(U+V)+\mathcal J(j+U)
      -\mathcal J(V)-\mathcal J(j)-\mathcal J(U)\\
     &+\sigma\pi i[-j-V+2Vj-U/2+U(j+V)+U^2/2].
 \end{split}                                             \tag{21}
\]
Then
\[
 \mathcal R_{\sigma,N}
 =\kappa^\sigma N^{-1/2}\mathcal A_\sigma e^{NG_\sigma}
   \exp\left\{
      \sum_{r=1}^p
        \frac{B_{2r}\mathcal D_{2r-1}}
                   {(2r)!\,N^{2r-1}}
           +O(N^{-2p-1})\right\},                       \tag{22}
\]
where
\[
 \begin{split}
 \mathcal A_\sigma
   &=e^{\sigma\pi i(j+V+U/2)}
       \exp\left\{\frac{
          \ell(U+V)+\ell(j+U)-\ell(V)-\ell(j)-\ell(U)}2\right\},\\
 \mathcal D_m
   &=\ell^{(m)}(U+V)+\ell^{(m)}(j+U)
           -\ell^{(m)}(V)-\ell^{(m)}(j)-\ell^{(m)}(U).
 \end{split}                                             \tag{23}
\]
The proof is multiplication of (11) by the exact
factors (20), using (9). In particular
\(e^{-\sigma\pi i d j}=e^{-N\sigma\pi i j}
e^{\sigma\pi i j}\); its finite shift accounts for
the \(j\) in the amplitude. All logarithmic
correction coefficients in (22) are independent
of the crossing sign, while the full phases and
Cartan scalar retain that sign.

The amplitude in (23) is nonzero. Thus the entire
original local row has a uniform relative symbol,
not merely a one-sided modulus estimate. Its
fixed undercolor derivatives are controlled on
smaller complex compacts. This derivative control
does not assert that each derivative value is
nonzero.

## 6. Composition and the remaining short-component problem

For any fixed braid, the exact joint clock theorem
first fixes a conserved physical flow and then
gives independent clock intervals (2) at all its
crossings. The products (3) may therefore be
performed simultaneously, with the original cut,
pivots, and exterior scalar unchanged.

If those conditional physical colors range in a
compact set satisfying the local hypotheses at
every crossing, multiplication of (22) gives a
uniform all-orders expansion for the product of
the complete rows. The leading amplitudes multiply
and are nonzero. This holds for any fixed number
of signed crossings, including any fixed short
signed component; the constants may depend on
that component and on the chosen compact set.

The remaining operation is the coherent sum or
integral over physical flows with the prescribed
boundary observation. Its neighboring factors
share those variables. The theorem supplies no
lower bound for that exterior pairing, no
automatic localization to the compact set, and
no estimate for physical endpoint strata.
In particular termwise relative errors cannot be
summed as relative errors of a potentially
cancelling whole period.

What has now been established unconditionally is
the actual local clock contraction's selected
nonzero amplitude, full relative expansion,
specified residue-period normalization, and
Gaussian coefficient one. The general partial
filling theorem still requires the geometric
source pairing and complementary estimates for
the remaining original physical-flow period.
