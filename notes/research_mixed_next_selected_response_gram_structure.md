# The complete selected response as a Gram insertion

Research deduction, 7 November 2026. The selected first-cardinal
response is the original positive conditional Gram operator applied
to an exact divided difference of \(d_N\). Its Hermitian part,
finite half-grid Cauchy formula, and rank-one displacement can all
be written without discarding a row or a boundary term.

These identities retain the distinct adjoint observation. They do
not turn a positive operator into a pointwise positive response, or
bound the actual outgoing arc by the seam value. No numerical
evaluation is used.

## 1. Coefficient-space conventions and the exact response

Put
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad
 P_j=(r;r)_j,\quad p_j(Y)=(rY;r)_j,\quad
 f_j(Y)=p_j(Y)/P_j,\qquad N\ge2.
 \tag{1}
\]
The coefficient space of polynomials of degree at most \(D\) has its
ordinary monomial inner product \(\langle u,v\rangle=u^*v\).
Let \(\mathsf F\) be the matrix whose \(j\)-th column consists of
the monomial coefficients of \(f_j\), and set
\[
 \mathsf A=\mathsf F\mathsf F^*>0,\qquad
 e=(1,\ldots,1)^T,\qquad
 \epsilon(Z)=(1,Z,\ldots,Z^D)^T .
 \tag{2}
\]
Every diagonal coefficient of \(\mathsf F\) is nonzero, so it is
invertible. The original type-three kernel on the unit circle is
\[
 C_0(Y,Z)=\sum_{j=0}^D\overline{f_j(Y)}f_j(Z).
 \tag{3}
\]
Thus its complete constant-term operator is precisely \(\mathsf A\):
if \(p\) is any degree-\(D\) polynomial with coefficient column
\(\mathbf p\), then
\[
 \operatorname{CT}_Y[p(Y)C_0(Y,Z)]
                         =\epsilon(Z)^T\mathsf A\mathbf p .
 \tag{4}
\]
The expression inside the constant term uses the original Laurent
form \(C_0(Y,Z)=\sum Y^{-j}p_j(Y)p_j(Z)/P_j^2\); (3)
is its exact unit-circle identity.

Let \(\mathbf d\) be the coefficient column of the original polynomial
\(d_N\), with \(d_N(r^b)=P_b^{-1}\). The exact cap identity
\(C_0(1,Z)=Nd_N(Z)\), proved in
[the outgoing equation](research_mixed_next_low_cardinal_outgoing_equation.md),
gives
\[
                         \mathbf d=\mathsf A e/N.
 \tag{5}
\]
Here \(f_j(1)=1\), so also \(\mathsf F^*e=e\) and
\(\mathbf d=\mathsf F e/N\).

Let \(\mathsf R\) be the backward monomial shift,
\(\mathsf RY^k=Y^{k-1}\) for \(k\ge1\), and
\(\mathsf R1=0\). For \(|B|=1\), define
\[
 \mathsf T_B=\sum_{h=1}^D B^h\mathsf R^h,\qquad
 (\mathsf T_Bp)(Y)=\frac{B\{p(Y)-p(B)\}}{Y-B}.
 \tag{6}
\]
The quotient is a polynomial with its removable diagonal value.
The original selected response at a physical node \(B=r^b\) is
\[
 \begin{split}
 S_B(Z)&=\mathcal S_{1,0}[\mathfrak l_b](Z)\\
       &=\operatorname{CT}_Y[(\mathsf T_Bd_N)(Y)C_0(Y,Z)]
         =\epsilon(Z)^T\mathsf A\mathsf T_B\mathbf d .
 \end{split}
 \tag{7}
\]
This is the full coefficient, including the outside \(N\) in the
definition of \(\mathcal S_{1,0}\). Indeed \(NQ_b(Y)\) in the
[cardinal-sector identity](research_mixed_next_cardinal_sector_separation.md)
is exactly \(\mathsf T_Bd_N\). There is no additional level scalar
in (7).

## 2. Hermitian part and the distinct adjoint response

Write \(v_B=(1,B^{-1},\ldots,B^{-D})^T\). Direct comparison of
the upper, lower and diagonal entries gives
\[
                 \mathsf T_B+\mathsf T_B^*=v_Bv_B^*-I .
 \tag{8}
\]
Set
\[
 \mathsf Q_B=\mathsf A\mathsf T_B\mathsf A/N,\qquad
 k_B=\mathsf A v_B .
 \tag{9}
\]
The polynomial with coefficient column \(k_B\) is \(C_0(B,Z)\).
Consequently
\[
 \boxed{\quad
 \mathsf Q_B+\mathsf Q_B^*
                  =\frac{k_Bk_B^*-\mathsf A^2}{N}.
 \quad}
 \tag{10}
\]
Define the separate polynomial
\[
                 \widetilde S_B(Z)
                         =\epsilon(Z)^T\mathsf Q_B^*e .
 \tag{11}
\]
Since \(v_B^*\mathsf A e=Nd_N(B)\), equations (5), (7)
and (10) prove
\[
 \boxed{\quad
 S_B(Z)+\widetilde S_B(Z)
        =d_N(B)C_0(B,Z)-\frac{V_{0,N}(Z)}{\kappa^2N^2}.
 \quad}
 \tag{12}
\]
Here \(V_{0,N}=\kappa^2N^2\mathsf A d_N\) is the actual forcing
polynomial of the outgoing equation. In particular, for a physical
\(B\), the complete unselected response is
\[
 \mathcal S_{0,0}[\mathfrak l_b](Z)
      =\widetilde S_B(Z)+\frac{V_{0,N}(Z)}{\kappa^2N^2}.
 \tag{13}
\]
The two terms in (13) cannot be dropped separately.
For general \(Z\), (11) is not the complex conjugate of
\(S_B(Z)\). Equations (10)--(13) are therefore an exact
two-observation identity, not a pointwise real-part inequality.

At the outgoing seam \(Z=1\) those observations do pair:
\[
 S_B(1)=N\mathbf d^*\mathsf T_B\mathbf d,\qquad
 \boxed{\quad
 2\Re S_B(1)
     =N|d_N(B)|^2-\sum_{a=0}^D S_a^{-2},
 \quad S_a=|P_a|.}
 \tag{14}
\]
Indeed
\(\|\mathbf d\|^2=N^{-1}\sum_aS_a^{-2}\), by exact root
averaging. Formula (14) also follows by applying (8).
The powers of \(N\) in (14) reflect the normalization of the
selected response in (7).

Since \(\|\mathsf T_B\|\le D\) for \(|B|=1\),
\[
 |S_B(1)|\le ND\|\mathbf d\|^2
                    =D\sum_{a=0}^D S_a^{-2}.
 \tag{15}
\]
Thus the complete outgoing seam has an upper rate \(c_{\rm b}\),
uniformly for the entire incoming unit circle, where
\(c_{\rm b}=-2J(1/6)\). For the physical low-node interval
\(0\le b\le\delta N\), choose a sufficiently small fixed
\(\delta<1/6\) such that
\(\sup_{\theta\le\delta}[-2J(\theta)]<c_{\rm b}\).
The uniform factorial bound and the proved positive sum
asymptotic then show that the second term of (14) dominates
the first exponentially. Hence \(S_B(1)\) has rate exactly
\(c_{\rm b}\), uniformly on that physical interval.
This controls the full outgoing sum at the seam; it does not
transport it to an independent complex output.

## 3. Exact half-grid Plemelj formula

For a physical \(B\), let
\[
                  \mathcal Y_N=\{Y:Y^N=-1\}.
 \tag{16}
\]
The vectors \(v_Y=(Y^{-j})_{j=0}^D\), \(Y\in\mathcal Y_N\),
are mutually orthogonal and have squared norm \(N\).
Because \((B/Y)^N=-1\), summing two finite geometric progressions
gives
\[
 (\mathsf T_B-\mathsf T_B^*)v_Y
                     =\frac{Y+B}{Y-B}v_Y .
 \tag{17}
\]
For example, after writing \(z=B/Y\), the \(j\)-th row of the
unconjugated sign matrix sums to
\(z^j(1+z)/(1-z)\); the endpoint term vanishes because
\(z^N=-1\). Thus (17) includes both true index endpoints.
Combining (8) and (17) gives the exact spectral decomposition
\[
 \mathsf T_B
   =\frac12(v_Bv_B^*-I)
       +\frac1{2N}\sum_{Y\in\mathcal Y_N}
                          \frac{Y+B}{Y-B}v_Yv_Y^* .
 \tag{18}
\]
All denominators are nonzero. Applying \(\mathsf A\) to
(18) and then to \(\mathbf d\) proves
\[
 \boxed{\quad
 S_B(Z)=\frac12d_N(B)C_0(B,Z)
       +\frac1N\sum_{Y^N=-1}
                    \frac{B}{Y-B}d_N(Y)C_0(Y,Z).
 \quad}
 \tag{19}
\]
To obtain the displayed form, use exact half-grid averaging of
the band \([-D,D]\):
\[
 \frac1N\sum_{Y^N=-1}d_N(Y)C_0(Y,Z)
                 =\operatorname{CT}_Y[d_N(Y)C_0(Y,Z)].
 \tag{20}
\]
There are no nonzero multiples of \(N\) in this band.
The half-grid samples in (19) are values of the original finite
polynomials, not a continuation of their sampled asymptotic.
Their Cauchy weights have size at most \(CN\), since the two
root grids are separated by \(2\sin(\pi/(2N))\).
This polynomial weight bound does not compare the signed sum
in (19) with its unweighted constant term.

The same formula is also an exact contour identity:
\[
 S_B(Z)=\frac1{2\pi i}\oint_{|Y|=R>1}
             \frac{B\,d_N(Y)C_0(Y,Z)}{Y(Y-B)}\,dY .
 \tag{21}
\]
The omitted constant \(d_N(B)\) has zero integral on this
complete exterior circle, since \(C_0\) has only nonpositive
incoming powers and that omitted integrand decays as \(Y^{-2}\)
at infinity. In the rewritten integrand the pole at \(Y=B\)
has residue \(d_N(B)C_0(B,Z)\). Moving (21) across that pole
therefore retains precisely the combined selected and unselected
response. The half contribution in (19) is its finite Plemelj
counterpart.

Formula (19), with \(C_0\) replaced by \(C_\beta\), is valid for
both next flags \(\beta=0,1\). This last assertion follows
directly by checking (21) and (19) on every Laurent monomial
of \(d_NC_\beta\), whose band is still \([-D,D]\).
The positive Gram representation and (10) are asserted only
for \(\beta=0\).

## 4. Rank-one displacement and the actual input

Retain the original outgoing lowering operator
\[
 (\mathcal Lp)(Z)=\frac{p(Z)-p(r^{-1}Z)}Z .
 \tag{22}
\]
It satisfies \(\mathcal L f_j=f_{j-1}\) for \(j\ge1\) and
\(\mathcal L f_0=0\). Hence, as coefficient matrices,
\[
                 \mathcal L\mathsf F=\mathsf F\mathsf R.
 \tag{23}
\]
Since \(\mathsf R\mathsf R^*=I-e_De_D^*\), and
\(f_D(Z)=N^{-1}\sum_{k=0}^D Z^k\), this proves the
rank-one Lyapunov displacement
\[
 \boxed{\qquad
 \mathcal L\mathsf A\mathcal L^*
                  =\mathsf A-\frac{ee^*}{N^2}.
 \qquad}
 \tag{24}
\]
The actual input obeys its corresponding forced equation:
\[
 \boxed{\qquad
                 (I-\mathcal L)\mathbf d=\frac{e}{N^2}.
 \qquad}
 \tag{25}
\]
For one proof, use \(\mathbf d=\mathsf F e/N\) in (23).
Alternatively, the original recurrence for the coefficients
\(d_k=[Z^k]d_N\) is
\[
 d_{k-1}=(1-r^{-k})d_k+N^{-2},\qquad d_D=N^{-2},
 \tag{26}
\]
which gives every row of (25), including the last one.
Thus the rank-one term in (24) and the forcing in (25)
are fixed by the original source.

These identities explain an exact weighted almost-invariance,
with its observation cost explicit. In the positive metric
\[
                \|p\|_{\mathsf A^{-1}}=\|\mathsf F^{-1}p\|_2,
 \tag{27}
\]
\(\mathcal L\) is the ordinary backward shift, and
\[
 \|\mathbf d\|_{\mathsf A^{-1}}=N^{-1/2},\qquad
 \|(I-\mathcal L)\mathbf d\|_{\mathsf A^{-1}}=N^{-1}.
 \tag{28}
\]
In particular \(\zeta=\sqrt N\,\mathbf d\) has norm one and
\(\|(I-\mathcal L)\zeta\|_{\mathsf A^{-1}}=N^{-1/2}\)
exactly. This is almost invariance of the actual reciprocal-factorial
input, without any phase correction, for this specified lowering
operator.
The dual norm of the prescribed point evaluation at \(Z\) is,
however,
\[
        \left(\sum_{j=0}^D|f_j(Z)|^2\right)^{1/2}.
 \tag{29}
\]
It is not polynomially bounded throughout the actual output
regions: the original row \(j=\lfloor N/6\rfloor\) already gives
an exponential rate greater than \(4/25\) on the matched containing
box, as proved in
[the weighted coefficient bound, Section 4](research_mixed_next_low_weighted_coefficient_bound.md).
At \(Z=1\), by contrast, the bound is attained:
\(|d_N(1)|=\sqrt{\sum_j|f_j(1)|^2}/\sqrt N=1\).
Moreover the complete response is \(\mathsf A\mathsf T_B\mathbf d\),
not a power of \(\mathcal L\) applied to \(\mathbf d\).
Consequently (28) alone gives neither the desired output bound
nor a nonzero prescribed observation.

There is also an exact qualification concerning the operator.
\(\mathcal L\) is nilpotent; it is not a knot-group generator.
The original diagonal operator \(\mathcal D f_j=r^j f_j\) is
unitary in the same \(\mathsf A^{-1}\) metric, but
\[
 \langle\zeta,\mathcal D\zeta\rangle_{\mathsf A^{-1}}
       =\frac1N\sum_{j=0}^D r^j=0,\qquad
 \|\mathcal D\zeta-\zeta\|_{\mathsf A^{-1}}=\sqrt2 .
 \tag{30}
\]
Indeed \(\mathsf F^{-1}\zeta=e/\sqrt N\), and
\(\mathsf F^{-1}\mathcal D\mathsf F=\operatorname{diag}(r^j)\).
Thus the lowering-operator estimate does not establish almost
invariance under the actual transfer representation.

All the identities above are finite identities at both parities.
They retain the original full matrices and their normal directions.
Fixed outgoing derivatives can be taken in their polynomial forms.
No incoming ordinary color has been freed from the physical input
used to define the forcing. The remaining task is a source-dependent
bound for the coupled output in (19) or (21), with its complete
pole and complementary cycle retained.
