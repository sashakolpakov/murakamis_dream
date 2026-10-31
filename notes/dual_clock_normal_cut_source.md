# An exact dual clock lift to the centralizer normal co-source

Research theorem, 27 October 2026. Every actual finite cut clock has
an explicit polynomial centralizer-normal co-source, valid on ALL
matrices. On the physical scaled clock this polynomial converges
locally uniformly to a whole exponential, with uniform factorial
coefficient bounds. Its derivatives transport every bounded normalized
cut-position moment exactly.

The lift is contravariant: it represents a trace FUNCTIONAL.
It is not a multiplicative symbol map, a crossing intertwiner, or an
internal Gaussian source comparison.

## 1. The dual Toeplitz map of the actual compact source

Put \(n=N-1\). In the source coordinates \(T=va\), the actual
coherent matrix symbol is
\[
 f_C(v,T)=\sum_{i,j=0}^n C_{ij}\binom nj
                      v^{i-j}T^j(1-T)^{n-j}.
\]
Let \(\omega_I=-\Omega_0/(2\pi i)\), whose marked compact period
is one. Angular integration and the beta integral give, for every
polynomial \(P\),
\[
 \int_\Gamma P(-T)f_C\,\omega_I
           =\frac1N\operatorname{Tr}(\mathcal T_N(P)C), \tag{1}
\]
where the diagonal Toeplitz row is
\[
 [\mathcal T_N(b^h)]_j
       =(-1)^h\frac{(j+1)^{\overline h}}
                         {(N+1)^{\overline h}},
 \qquad h\ge0,\quad 0\le j<N.                          \tag{2}
\]
A bar denotes the rising factorial. Formula (2) holds at ALL
polynomial degrees, not only below \(N\).

On polynomials of degree at most \(n\), \(\mathcal T_N\) is an
isomorphism onto the diagonal matrices: its h-th basis column is
a polynomial in j of degree h with nonzero leading coefficient,
evaluated at the N distinct integer points. This is different from
the covariant symbol quantization
\(b^h\mapsto(-1)^h(J)_h/(n)_h\).

The all-matrix pairing here is the normalized ORDINARY TRACE.
On the actual position-conserving weighted-word and Green cut
arrays it agrees with the original average cut because those
arrays are diagonal. It is not the original average functional
\(\Phi(C)=N^{-1}\sum_{i,j}C_{ij}\) on arbitrary off-diagonal
Ward matrices. Any such Hopf-current comparison must retain
and transport that original coupon separately. The trace
extension is stated explicitly rather than identified with
all possible actual co-sources.

## 2. Exact inversion for the WHOLE clock

For any complex \(w\), define the polynomial of degree at most n
\[
 P_{N,w}^{\vee}(b)=\sum_{h=0}^n a_{N,h}(w)b^h,
\]
\[
 a_{N,h}(w)=
 \frac{(N+1)^{\overline h}}{h!}
     \sum_{r=h}^n(-1)^r\binom rh(w-1)^r .               \tag{3}
\]
Then exactly
\[
              \mathcal T_N(P_{N,w}^{\vee})=w^J ,
              \qquad Je_j=je_j.                       \tag{4}
\]
Thus for EVERY matrix C,
\[
 \frac1N\operatorname{Tr}(w^JC)
                 =\int_\Gamma P_{N,w}^{\vee}(-T)f_C\,\omega_I .
                                                               \tag{5}
\]

Here is a direct proof. The polynomial identity
\[
 (j)_r=\sum_{h=0}^r(-1)^{r-h}\binom rh
                     \frac{r!}{h!}(j+1)^{\overline h} \tag{6}
\]
follows, for example, by comparing coefficients in
\((1+\delta)^j\): sum the right side over r with weight
\(\delta^r/r!\), use
\(\sum_{r\ge h}(-1)^{r-h}\binom rh\delta^r
=\delta^h/(1+\delta)^{h+1}\), and then the rising-binomial
series. Now expand \(w^j\) in the Newton basis
\[
 w^j=\sum_{r=0}^n\frac{(j)_r}{r!}(w-1)^r
                       \quad(0\le j\le n).
\]
Insert (6), collect h, and apply (2). This is precisely (3)--(4).

Useful exact endpoint formulas are
\[
 P_{N,w}^{\vee}(0)=\sum_{r=0}^{N-1}(1-w)^r,\qquad
 P_{N,w}^{\vee}(-1)=w^N-(w-1)^N.                        \tag{7}
\]
These are not the actual clock eigenvalues at j=0,n.
Confusing dual polynomial evaluation with a matrix endpoint
would lose finite endpoint corrections.

## 3. Scaled clocks, moments, and uniform whole limits

Put \(w=e^{z/N}\). On every compact complex z-set,
\(|w-1|\le C/N\). For all sufficiently large N,
\[
 |a_{N,h}(e^{z/N})|
 \le \frac{(N+1)^{\overline h}}{h!}
          \frac{|w-1|^h}{(1-|w-1|)^{h+1}}
 \le C_1\,\frac{C_2^h}{h!},
 \qquad 0\le h<N.                                    \tag{8}
\]
Indeed \((N+1)^{\overline h}\le(2N)^h\) for h<N, while
\((1-C/N)^{-h-1}\) is bounded uniformly in that range.
For each fixed h, the leading r=h term in (3) gives
\[
 a_{N,h}(e^{z/N})\longrightarrow(-z)^h/h!.
\]
The factorial majorant proves the WHOLE locally uniform limit
\[
              P_{N,e^{z/N}}^{\vee}(b)\longrightarrow e^{-zb}
                     \quad\text{on }\mathbb C_z\times\mathbb C_b.
                                                               \tag{9}
\]
This also proves convergence of every fixed derivative by Cauchy's
formula. No WKB asymptotic interpretation of these derivatives is used.

Differentiation of (4) gives the exact normalized moment identities
\[
 \mathcal T_N\!\left(\partial_z^r
           P_{N,e^{z/N}}^\vee\right)
       =(J/N)^r e^{zJ/N}.                              \tag{10}
\]
At z=0 these give every fixed normalized polynomial cut-position
moment. Unnormalized moments \(J^r\) retain the explicit factor
\(N^r\). Formula (10) is a whole clock-coupling identity, valid before
any internal flow sum.

The bounded moment has a stronger finite normal-order statement.
Put
\[
 G_{N,r}(b)=\left.\partial_z^r
                   P_{N,e^{z/N}}^\vee(b)\right|_{z=0}.
\]
It has degree at most \(\min(r,n)\). In particular for every fixed
r and all \(N>r\), its normal pole in (13) has order at most
r+1, INDEPENDENT of N. An exact closed formula is
\[
 [b^h]G_{N,r}=
 \frac{(N+1)^{\overline h}}{N^r h!}
       \sum_{s=h}^{\min(r,n)}
            S(r,s)(-1)^s\binom sh s!,
 \qquad 0\le h\le\min(r,n),                            \tag{10a}
\]
where \(S(r,s)\) are Stirling numbers of the second kind.
This follows by differentiating
\((e^{z/N}-1)^s\) at zero, whose r-th derivative is
\(s!S(r,s)/N^r\). For r at most n the leading coefficient is
\((-1)^r(N+1)^{\overline r}/N^r\), while each lower coefficient
is \(O_r(N^{h-r})\). Hence
\[
 G_{N,r}(b)=(-b)^r+O_r(1/N)
\]
on every fixed compact b-set. Arbitrary bounded-degree normalized
Green cut-position polynomials follow by linearity. Their actual
source-normal pole depth is therefore bounded even though the
WHOLE clock uses degree \(N-1\).

Beta reflection gives
\[
 \mathcal T_N(P(-1-b))_j=\mathcal T_N(P)_{n-j}.
\]
Injectivity on degree at most n therefore proves
\[
 P_{N,w}^\vee(-1-b)=w^nP_{N,w^{-1}}^\vee(b).             \tag{11}
\]
The centered polynomial
\[
 \widehat P_N(z,b)=e^{-nz/(2N)}P_{N,e^{z/N}}^\vee(b)
\]
reflects z to -z and tends to \(e^{-z(b+1/2)}\).
For the identity matrix, (5) is EXACTLY the retained source character
\[
 \int_\Gamma\widehat P_N(z,-T)\omega_I
    =\frac1N\operatorname{Tr}e^{z(J-n/2)/N}
    =\frac{\sinh(z/2)}{N\sinh(z/(2N))}.                 \tag{12}
\]
Thus this lift reproduces the same whole source norm/peripheral
factor as the scaled-meridian and Gamma-source calculations.

## 4. Normal residue and global affine clutch

Use the normal centralizer coordinate \(b=-a/\eta\) and
\[
 \nu_{\mathrm{cut}}=-\frac{d\eta}{\eta}\wedge
                         \frac{\Omega_0}{1-\eta v}.
\]
For every h, expansion of the geometric denominator gives
\[
 \operatorname{Res}_{E}(b^h\nu_{\mathrm{cut}})
                           =-(-T)^h\Omega_0 .
\]
Linearity, (3), and (5) yield the exact source pairing
\[
 \frac1N\operatorname{Tr}(w^JC)
   =\frac1{2\pi i}\int_\Gamma
      \operatorname{Res}_{E}
           \left(P_{N,w}^\vee(b)f_C\nu_{\mathrm{cut}}\right). \tag{13}
\]
This is a SOURCE-KERNEL lift; it is not asserted to be the internal
Gaussian image of that kernel.

The north and south torsor coordinates obey
\[
 b_S=b_N+\frac1{v\eta},\qquad
 b_S-1-b_N=\frac{1-\eta v}{v\eta}.
\]
Use \(P(b_N)\) north and \(P(b_S-1)\) south. Their difference is
divisible by the Gauss-wall factor. After multiplication by
\(\nu_{\mathrm{cut}}\) the Gauss-wall pole cancels, leaving only
\(\eta^{-r}d\eta\wedge\Omega_0\) with \(r\ge2\).
Each has an explicit normal primitive and zero E-residue.
Thus (13) retains a compatible affine Cech moment marking.
Bare \(P(b_S)\) would have the wrong residue polynomial.

At finite N the normal pole degree can reach N, since
\(\deg P^\vee=N-1\) and \(\nu_{\mathrm{cut}}\) already has a simple
normal pole. It must not be replaced by a bounded normal jet.
After taking the explicit residue formula, (8)--(9) do allow
locally uniform convergence of the whole residue to its exponential
source form. No algebraicity of that limiting horizontal exponential
is claimed.

## 5. Exact finite cut-current endpoints

For an arbitrary zero-extended finite current \(J_j\), set
\(\lambda_{N,w}^{\mathrm{head}}(J)=N^{-1}\sum_{j=0}^{N-1}w^jJ_j\).
For \(w\ne0\), direct summation by parts gives
\[
 \lambda_{N,w}^{\mathrm{head}}((S-1)J)
   =(w^{-1}-1)\lambda_{N,w}^{\mathrm{head}}(J)
               +\frac{w^{N-1}J_N-w^{-1}J_0}{N}.        \tag{14}
\]
Including both actual tails gives the full finite row
\(N^{-1}\sum_{j\in\mathbb Z}w^jJ_j\), for which the endpoint
terms telescope and the factor is exactly \(w^{-1}-1\).
Its z-derivatives retain every normalized position-moment endpoint.

The original raw Green arrays already contain \(1/N\).
Equations (5), (13), and (14) use matrix-normalized arrays;
\(I_{\mathrm{mat}}=NI_{\mathrm{raw}}\), \(J_{\mathrm{mat}}=NJ_{\mathrm{raw}}\).
Equivalently use N times these rows on raw arrays.
No factor N is absorbed into an endpoint.

## 6. Whole word composition is exact; Gaussian naturality is additional

An actual transfer clock can be split into literal input/output
position clocks. For the recorded checked R conventions,
\[
 R_+:(i,j)\mapsto(j+k,i-k),\qquad
 R_-:(i,j)\mapsto(j-k,i+k),
\]
so
\[
 w^kR_+=(I\otimes w^{-J})R_+(w^J\otimes I),\qquad
 w^kR_-=(I\otimes w^J)R_-(w^{-J}\otimes I).              \tag{15}
\]
These are exact coefficient identities with the same Cartan and
pivot lines. Products and tensor products use the actual operator
composition, or equivalently the exact finite coherent STAR product.
Thus all weighted words and their coupling derivatives retain their
source meaning.

Pointwise multiplication is not that star product. Already at N=2
the actual inverse clocks obey
\(\operatorname{Tr}(w^Jw^{-J})/2=1\), whereas
\[
 \int_0^1[1+(w-1)T][1+(w^{-1}-1)T]\,dT
          =1+\frac{w+w^{-1}-2}{6}.
\]
At the actual root clock w=-1 this is 1/3, not one.
The DUAL pairing (5) gives one exactly.

Moving a dual clock through an actual crossing therefore requires
the transpose of its finite star action. A scalar polynomial in b
represents diagonal co-sources only; after an off-diagonal crossing
one generally needs the full angular/coherent dual source as well.
The normal residue is not a multiplicative operator-algebra map.

Consequently this theorem supplies the actual whole CUT clock and
all its normalized moments, including tails and affine clutch.
The independent second framing coordinate still needs its network
map. Nor is the source-dependent transverse Gaussian pushforward
proved natural for this contravariant star action. These are the
specific remaining couplings, rather than a defect in the finite
clock formula.

## 7. Why the raw framing moments are not the finite critical field

For the actual scalar closed cut \(C=F_NI\), the polynomial
normal-centralizer moments from (1) normalize to
\[
 \mu(b^h)=(-1)^h/(h+1).
\]
Their Hankel matrices are signed Hilbert matrices, positive definite
at EVERY size: \(\mu(p\overline p)=\int_0^1|p(-T)|^2dT>0\)
for nonzero p. Hence no nonzero polynomial ideal is annihilated.
This raw framing co-source cannot factor through a fixed finite
algebra in b, even for the actual figure-eight.

This does not contradict a finite algebra of ISOLATED TRANSVERSE
geometric critical points. The framing variable is meant to be
integrated first, or retained in a relative/twisted complex.
It does rule out defining that critical observable as the raw
Toeplitz image of b: \(\mathcal T_N\) is not multiplicative.
A finite list of moments reconstructs a density only AFTER its
critical polynomial relation has actually been supplied.

[Exact audit](../experiments/audit_dual_clock_normal_cut_source.py)
and [results](../experiments/dual_clock_normal_cut_source_results.json):
337 symbolic clock, normalized-moment, reflection, endpoint and
finite-current identities pass at N=2 through 11.

