# A finite mixed kernel through the reduced Euler vacuum

Private written proof, 18 November 2026.

The actual two-head reduced Euler factor admits an exact product
kernel after factorial normalization and a specified diagonal
change of polarization. Its inverse has a product kernel in a
different specified polarization. At the original physical
parameter \(x=-M/q\), both products are midpoint products. On
a compact nonzero-factor chart they have a uniform leading
amplitude equal to one, including the lower donor vacuum.

This is an asymptotic of the literal finite kernel at integer
input indices, with holomorphic coherent variables. It does not
construct an analytic interpolation in the donor index, remove
the recipient upper projector, or estimate a closed source.
The sole complete proof direct is G, which supplies the actual
finite \(S\) factors and their principal correspondence.

## 1. The actual finite factors and the two polarizations

Put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 h=2\pi i/N,\quad x=-M/q,\quad
 f_a=\prod_{\ell=1}^a(1-Q^\ell),\quad f_0=1.
 \tag{1}
\]
Here \(N\ge2\) and \(M\ne0\). All \(f_a\), \(0\le a\le d\),
are nonzero. G's actual \(S=S_2\) has coefficient
\[
 S_{a-n,b+n;\,a,b}
       =x^{-n}\frac{f_{b+n}}{f_bf_n},
 \qquad
 0\le n\le\min(a,d-b).
 \tag{2}
\]
The inverse coefficient is (2) multiplied by
\((-1)^nQ^{n(n-1)/2}\). These statements retain the finite
donor and recipient masks.

Let \(G_Fw_a=f_aw_a\), \(\mathcal G=G_F\otimes G_F\), and
let \(J\) act on the recipient by
\[
                    Jw_b=Q^{b(b-1)/2}w_b.
 \tag{3}
\]
Define the two actual finite matrices
\[
 \mathscr S_+=J\mathcal G^{-1}S\mathcal GJ^{-1},
 \qquad
 \mathscr S_-=\mathcal G^{-1}S^{-1}\mathcal G.
 \tag{4}
\]
At the root \(J\) is unitary in the occupation basis.
No bounded conditioning assertion is made for \(\mathcal G\).

Identify that basis with the polynomials
\(z_{\rm d}^az_{\rm r}^b\), \(0\le a,b\le d\).
Let \(\Pi_d^{\rm r}\) delete every monomial whose recipient
degree exceeds \(d\). Then the exact kernels are
\[
 \boxed{\quad
 \mathscr S_+(z_{\rm d}^az_{\rm r}^b)
 =\Pi_d^{\rm r}\left[
 z_{\rm r}^b\prod_{j=0}^{a-1}
       (z_{\rm d}+x^{-1}Q^{b+j}z_{\rm r})\right],
 \quad}
 \tag{5}
\]
\[
 \boxed{\quad
 \mathscr S_-(z_{\rm d}^az_{\rm r}^b)
 =\Pi_d^{\rm r}\left[
 z_{\rm r}^b\prod_{j=0}^{a-1}
       (z_{\rm d}-x^{-1}Q^jz_{\rm r})\right].
 \quad}
 \tag{6}
\]
Empty products are one. If \(a+b\le d\), the projector in
each formula acts as the identity. Otherwise it stays in
the kernel; an estimate for the unprojected product is not
an estimate for that projected polynomial.

For completeness, conjugating (2) by \(\mathcal G\) gives
\[
 x^{-n}{a\brack n}_Q,\qquad
 {a\brack n}_Q=\frac{f_a}{f_nf_{a-n}}.
 \tag{7}
\]
The additional \(J\) ratio is
\(Q^{bn+n(n-1)/2}\). The elementary polynomial identity
\[
 \prod_{j=0}^{a-1}(u+Q^jv)
  =\sum_{n=0}^a Q^{n(n-1)/2}{a\brack n}_Q u^{a-n}v^n
 \tag{8}
\]
therefore proves (5), and its substitution \(v=-x^{-1}z_{\rm r}\)
proves (6). To prove (8), multiply the degree-\(a\) product
by \(u+Q^av\) and use
\[
 {a+1\brack n}_Q
 ={a\brack n}_Q+Q^{a+1-n}{a\brack n-1}_Q.
\]
This last equality follows directly from the ratios of
the finite \(f\)'s. It proves (8) by induction from \(a=0\).

The polarizations in (4) are different. In the common
factorial basis the positive factor is
\(J^{-1}\mathscr S_+J\), while the negative factor is
\(\mathscr S_-\). In particular the exact inverse relation is
\[
             \mathscr S_-J^{-1}\mathscr S_+J=I,
 \tag{9}
\]
and its reversed product is also the identity.
Every such \(J\), every \(\mathcal G\), and every transformed
neighboring coupon or closing row must remain in a source
calculation. Equations (5)--(6) do not reset a cut or pivot.
The separate \(\kappa,D\) factors of G's reduced braid
generator are unchanged by this statement.

## 2. A uniform nonzero amplitude on the integer family

Write \(B=e^{hb}\), \(t=ha\), and define
\[
 L_+(s)=z_{\rm d}-M^{-1}B e^sz_{\rm r},
 \qquad
 L_-(s)=z_{\rm d}+M^{-1}e^sz_{\rm r}.
 \tag{10}
\]
The respective unprojected products in (5)--(6), with
\(z_{\rm r}^b\) omitted, are exactly
\[
            P_{\pm,N}=\prod_{j=0}^{a-1}
                         L_\pm((j+\tfrac12)h).
 \tag{11}
\]
The half-step is forced by \(x^{-1}=-M^{-1}e^{h/2}\).

Fix a compact parameter set in a slightly larger complex
neighborhood of \((M,B,z_{\rm d},z_{\rm r})\), with \(M\ne0\).
For one of the signs assume there is a disk \(|s|<\tau\)
on which \(L_\pm(s)\) is bounded away from zero and has
a chosen holomorphic logarithm. These are local assumptions
on the explicit linear factors. Each sign may use its own
neighborhood. Define
\[
          \mathcal A_\pm(t)=\int_0^t\log L_\pm(s)\,ds.
 \tag{12}
\]
The path is the straight segment, with the chosen logarithm.
For every integer \(0\le a\le d\) with \(a|h|\le\tau/2\),
and every \(0\le b\le d\) whose \(B=e^{hb}\) belongs to
the stated parameter set, one has
\[
 P_{\pm,N}
   =\exp\!\left(\frac{\mathcal A_\pm(ha)}h\right)
                       \mathcal U_{\pm,N},\qquad
 \mathcal U_{\pm,N}
   =1+O(a|h|^2)=1+O(N^{-1}).
 \tag{13}
\]
The factor \(\mathcal U_{\pm,N}\) is holomorphic and
nonzero in the coherent variables and \(M\). It and its
inverse are uniformly bounded. Every fixed derivative in
these parameters satisfies the same \(O(a|h|^2)\) remainder
estimate on the smaller compact set. At \(a=0\),
\(\mathcal A_\pm=\log\mathcal U_{\pm,N}=0\) exactly.
The full kernel also contains the exact factor \(z_{\rm r}^b\).

Here is a direct remainder proof. Put \(F(s)=\log L_\pm(s)\).
On each interval of complex length \(h\), centered at
\(s_j=(j+\tfrac12)h\), Taylor's formula and cancellation
of the odd term give
\[
 \left|F(s_j)-\frac1h\int_{jh}^{(j+1)h}F(s)\,ds\right|
       \le \frac{|h|^2}{24}\sup|F''|.
 \tag{14}
\]
Parametrizing the segment by \(s=s_j+hu\),
\(-1/2\le u\le1/2\), proves the same bound for complex \(h\).
Summing proves
\[
 \log\mathcal U_{\pm,N}
     =\sum_{j<a}F(s_j)-\mathcal A_\pm(ha)/h
                         =O(a|h|^2).
 \tag{15}
\]
Exponentiation proves (13); Cauchy estimates on the
larger parameter neighborhood prove all the stated
fixed coherent-variable and meridian derivatives.
This proof uses no asymptotic summation of an oscillatory
transfer series: that series was summed exactly in (5)--(6).

If instead the phase is written using the exact
\(N\)-dependent coefficient \(x^{-1}\), the left-endpoint
rule produces a square-root endpoint factor. Expanding
its retained half-step gives exactly (13). Dropping the
half-step while keeping that square root would change
the literal leading amplitude.

The estimate applies to the actual kernel without further
projection precisely in the capacity region \(a+b\le d\).
Outside it, equations (5)--(6) still give the exact kernel,
but (13) applies only before \(\Pi_d^{\rm r}\). No relative
estimate for the projected polynomial is asserted.

## 3. The regular resolved canonical map

We check the relation to G's actual correspondence at
completeness, rather than inferring it from the product's
nonvanishing. Put \(x_0=-1\), \(A=e^t\), and regard \(B\)
as the input recipient clock. For the positive product
the principal mixed phase, including its recipient monomial,
is
\[
 \mathcal F_+
  =(\log B)\log z_{\rm r}
       +\int_0^{\log A}
             \log(z_{\rm d}+x_0^{-1}B e^sz_{\rm r})\,ds.
 \tag{16}
\]
All logarithms here are local. Assume initially the displayed
variables and factors are nonzero. Set
\[
 w=x_0^{-1}Bz_{\rm r}/z_{\rm d},\qquad
                 C=\frac{1+Aw}{1+w}.
 \tag{17}
\]
Differentiation in the output evaluation variables gives
the output clocks
\[
                         A'=A/C,\qquad B'=BC.
 \tag{18}
\]
In the factorial polynomial model the physical lowering
operator is multiplication by its evaluation variable,
followed by the retained upper projection. On the recipient
after \(J\) it is the ordered operator
\(\Pi_d^{\rm r}M_{z_{\rm r}}Q^{J_{\rm occ}}\):
\(z_{\rm r}^b\) is sent to \(Q^bz_{\rm r}^{b+1}\)
before projection. On the regular unprojected correspondence
its principal symbol is the clock times the evaluation
variable. Thus
\[
 f'_{\rm d}=z_{\rm d},\qquad f'_{\rm r}=B'z_{\rm r}.
 \tag{19}
\]
Differentiating (16) in the input positions gives
\[
 f_{\rm d}=z_{\rm d}(1+Aw),\qquad
 f_{\rm r}=BCz_{\rm r}=f'_{\rm r}.
 \tag{20}
\]
Consequently, with \(v=f_{\rm r}/(x_0 f_{\rm d})\),
\[
 v=\frac{w}{1+w},\qquad
 C=1+(A-1)v,\qquad
 \frac{1-A'}{f'_{\rm d}}=\frac{1-A}{f_{\rm d}}.
 \tag{21}
\]
These are exactly G's \(S_2\) map, including preservation
of the physical donor flag \(p_{\rm d}=(1-A)/f_{\rm d}\).
The recipient flag follows from the same formula
\(p_{\rm r}=(1-B)/f_{\rm r}\).

At a lower row endpoint \(A=1,p_{\rm d}=0\), assume the
physical donor and recipient \(f\)'s before and after
the factor are units. Equations (19)--(21) then give
\[
 C=1,\quad
 f'_{\rm d}=f_{\rm d}-f_{\rm r}/x_0,\quad
 w=\frac v{1-v},\quad 1+w\ne0.
 \tag{22}
\]
Hence the factor in (16) is nonzero at \(s=0\).
It remains nonzero on a sufficiently small common
neighborhood and a small disk of normalized donor length.
This supplies exactly the local hypotheses of Section 2.
The mixed phase is regular there and its actual midpoint
amplitude is one at the endpoint.

For the inverse use no \(J\). Its mixed phase is (16)
with \(x_0^{-1}Bz_{\rm r}\) replaced by \(-x_0^{-1}z_{\rm r}\).
Both output physical \(f\)'s are now the evaluation variables.
Writing
\[
 C=\frac{z_{\rm d}-x_0^{-1}Az_{\rm r}}
          {z_{\rm d}-x_0^{-1}z_{\rm r}},
\]
differentiation gives \(A'=A/C,B'=BC\),
\(f_{\rm r}=f'_{\rm r}=z_{\rm r}\), and
\(f_{\rm d}=z_{\rm d}-x_0^{-1}Az_{\rm r}\).
The donor flag is again preserved. This is the inverse
of (21). At \(A=1\), it reads
\(f'_{\rm d}=f_{\rm d}+f_{\rm r}/x_0\); the same unit
hypotheses give the nonzero-factor chart for (6).

## 4. What has not been transported

The finite formulas are rational identities in \(q,M\)
where the finitely many \(f_a\)'s are nonzero, and so
retain the finite block's meridian and quantum germs.
They do not turn G's root-level reduced-word identity
into an off-root identity for a closed ordinary-color
invariant. Its additional source and pivot adapters remain.
The uniform derivative claim in (13) concerns fixed integer
indices and the specified coherent variables and \(M\).

Although (12) is a holomorphic function of a continuous
normalized length \(t\), (13) was proved for \(t=ha\) with
integer \(a\). It supplies no exact interpolation of the
finite matrix at complex \(a\), no uniqueness modulo
functions periodic in \(a\), and no replacement for its
root carries or upper endpoint currents on a complex contour.
The same distinction applies to the recipient occupation:
the actual samples have \(B=e^{hb}\). Treating \(B\) as an
independent holomorphic parameter in the product supplies
the stated uniform estimates, not a proof of a source
interpolation in complex \(b\) or of a physical lattice
sequence approaching an arbitrary complex geometric clock.

A full \(S_r\) after factorial normalization has the
donor multinomial factor
\[
 \frac{f_a}{f_{a-\sum n_j}\prod_jf_{n_j}}
\]
with G's ordered \(K\)-monomials. This is not the scalar
two-variable product (5). Nor do the hypotheses above
automatically hold at every intermediate factor of that
star. No uniform whole-star amplitude is inferred.

Finally a local unit amplitude is not a contribution of
the original source. The exact capacity masks, the interface
chirps, the original diagonal and scalar lines, and the
closing functional must all still be paired. No geometric
cycle, noncancellation, or scalar lower bound is proved here.

## Complete proof-source pin

* G: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.

The complete source was freshly read nontruncated in this
active sequence and retained unchanged. Every used implication
was checked. Only written mathematics and text/hash operations
were used; frozen and public files were not edited.
