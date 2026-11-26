# Fourier interpolation selects the canonical crossing normalization

22 November 2026. Written research proof.
Earlier final notes and frozen manuscripts remain unchanged.

The crossing source has an exact polynomial bandwidth. Its values on
the corresponding complete Fourier grid are known factorial products.
We prove that this grid selects the canonical Gamma asymptotic on a
fixed complex neighborhood of the maximum of its magnitude profile.
An exact three-coordinate transport equation then extends the estimate
throughout the positive pair-angle domain.

The normalization proof uses a local Cauchy interpolation remainder
and a global bound on the actual grid values. It requires neither the
earlier fractional-source rigidity theorem nor growing-order
asymptotic expansions. The grid alone would not suffice: the essential
additional estimate suppresses the interpolation remainder at both
edges of the allowed Fourier band.

## 1. The original source and its full Fourier grid

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=e^{\pi i d^2/(2N)}.
 \tag{1}
\]
Use the full original algebra and centered basis of [P]. Put
\[
 U_x=\sum_{a=0}^d x^a f_a,\qquad
 \Phi_N(C,H,K)=\phi(f_0U_{-C}U_{-H}U_{-K}).
 \tag{2}
\]
Here \(\phi\) is the original bilinear Frobenius closing,
\(f_0=R^+/\sqrt N\), and every repeated-root derivative coordinate
is retained. The polynomial in (2) is symmetric and separately of
degree at most \(d\). Set
\[
 C=e^{-2\pi ic},\quad H=e^{-2\pi ih},\quad K=e^{-2\pi ik},
 \qquad \varphi_N(c,h,k)=\Phi_N(C,H,K).
 \tag{3}
\]

Let \(\mathfrak F_N\) be the canonical factorial explicitly defined
in [E]. It has its specified meromorphic continuation and satisfies
\[
 \mathfrak F_N(r)=(Q;Q)_r\ (0\le r<N),\qquad
 \mathfrak F_N(w+1)=(1-Q^{w+1})\mathfrak F_N(w).
 \tag{4}
\]
Its logarithmic marks are fixed by that definition. Define
\[
 \Gamma_N(c,h,k)=\frac{\kappa^2}{N^2}
 \frac{\prod_{a\in\{c,h,k\}}
             \mathfrak F_N(N(1-a)-1/2)^2}
      {\prod_{\{a,b\}}\mathfrak F_N(N(1-a-b))}.
 \tag{5}
\]
The products count labelled singles and pairs. There is no unspecified
periodic factor in this definition.

The full grid, its cardinal polynomials, and its denominator are
\[
 a_i=(i+1/2)/N,\quad C_i=q^{-1}Q^{-i},\quad
 D_N(z)=1+z^N,\quad
 \ell_i(z)=\frac1N\sum_{r=0}^d(z/C_i)^r
       =\frac{D_N(z)}{D_N'(C_i)(z-C_i)}.
 \tag{6}
\]
The quotient is the displayed polynomial, including at its removable
point. In particular \(C_i^N=-1\) and
\(\ell_i(C_j)=\delta_{ij}\).

The exact full-basis identity in [P, Section 4] states
\[
 G_{ijk}:=\Phi_N(C_i,C_j,C_k)=\Gamma_N(a_i,a_j,a_k).
 \tag{7}
\]
This is zero unless \(i+j,i+k,j+k\le d\). On that support,
\[
 G_{ijk}=\frac{\kappa^2}{N^2}
 \frac{F_{d-i}^2F_{d-j}^2F_{d-k}^2}
      {F_{d-i-j}F_{d-i-k}F_{d-j-k}},\qquad
 F_r=(Q;Q)_r.
 \tag{8}
\]
Thus the original source, not an auxiliary norm, is exactly
\[
 \Phi_N(C,H,K)=
       \sum_{i,j,k=0}^d G_{ijk}\ell_i(C)\ell_j(H)\ell_k(K).
 \tag{9}
\]
The grid is a basis of the full Newton space. It is not evaluation
only at distinct Casimir roots.

## 2. A global bound on the actual grid

Write
\[
 L(x)=\int_0^x\log|2\sin\pi t|\,dt,\qquad
 T(a,b)=L(a+b)-L(a)-L(b),
\]
\[
 \mathcal D=\{c,h,k>0:\ c+h,c+k,h+k<1\},\qquad
 A_0(c,h,k)=T(c,h)+T(c,k)+T(h,k).
 \tag{10}
\]
The function \(A_0\) is continuous on the compact closure
\(\overline{\mathcal D}\).

**Lemma 1.** It is strictly concave on \(\mathcal D\), positive
there, and has the unique global maximum on
\(\overline{\mathcal D}\) at
\[
 p=(1/3,1/3,1/3),\qquad M=A_0(p)=-9L(1/3)>0.
 \tag{11}
\]

**Proof.** For \(a,b>0\), \(s=a+b<1\), the Hessian of \(T\) is
\[
 \pi\begin{pmatrix}
 \cot\pi s-\cot\pi a&\cot\pi s\\
 \cot\pi s&\cot\pi s-\cot\pi b
 \end{pmatrix}.
 \tag{12}
\]
Its diagonal entries are negative and its determinant is \(\pi^2\),
by the cotangent addition formula. It is negative definite. Summing
the three such forms on the coordinate pairs gives a negative-definite
Hessian for \(A_0\). At equal coordinates \(a\),
\(\partial_c A_0=2\log(2\cos\pi a)\), which vanishes at \(a=1/3\).
Strict concavity gives the unique interior maximum. Along the segment
from \(p\) to a boundary point the second derivative is strictly
negative before the endpoint. Continuity therefore excludes a
second maximum on the boundary.

For positivity, at fixed \(s\in(0,1)\) the function
\(L(s)-L(t)-L(s-t)\) vanishes at both endpoints and has second
derivative
\[
             -\frac{\pi\sin\pi s}
                    {\sin\pi t\sin\pi(s-t)}<0.
\]
Thus each \(T(a,b)>0\) on its domain. Finally
\(L(1-x)=-L(x)\), since the log-sine integral over \([0,1]\)
is zero, which gives the value of \(M\). \(\square\)

**Lemma 2.** There is a constant \(B\) independent of \(N,i,j,k\)
such that on the entire supported grid,
\[
       \log|G_{ijk}|=N A_0(a_i,a_j,a_k)+O(\log N).
 \tag{13}
\]
Consequently every closed subset of
\(\overline{\mathcal D}\) not containing \(p\) has a strict
exponential gap below \(e^{NM}\), uniformly in its grid samples.

**Proof.** Put \(S_r=\prod_{a=1}^r2\sin(\pi a/N)\), \(S_0=1\).
The elementary uniform estimate is
\[
       \log S_r=N L(r/N)+O(\log N),\qquad 0\le r<N.
 \tag{14}
\]
For \(r\le N/2\), monotonicity of
\(\log(2\sin\pi x)\) bounds the difference between its sum and
integral by the telescoping difference of its first and last
sample, plus the first-cell error. The telescoping difference
is \(O(\log N)\). The first-cell error is \(O(1)\), by comparison
with \(\log(2\pi x)\). For larger \(r\), use the exact identity
\(S_rS_{d-r}=N\) and \(L(1-x)=-L(x)\).
The change of one cell costs \(O(\log N)\).

The same endpoint comparison proves uniformly that
\[
 |L(x+t)-L(x)|\le C|t|\log(e/|t|)
 \tag{15}
\]
when both arguments lie in \([0,1]\). The modulus follows by
integrating a bound by a constant plus
\(|\log x|+|\log(1-x)|\).
The magnitude formula for the weighted tensor in [P, (9)],
together with its exact grid conversion, gives
\[
       |G_{ijk}|=
       N\,\frac{S_{i+j}S_{i+k}S_{j+k}}{S_i^2S_j^2S_k^2}.
 \tag{16}
\]
Apply (14), then (15) to move the indices to the angles \(a_i\).
All supported pair angles are at most one; hence (15) also covers
the support faces. This proves (13). The final assertion follows
from Lemma 1 and compactness. Unsupported grid values are exactly
zero and require no estimate. \(\square\)

## 3. The analytic Gamma profile and its Fourier band

The strip expansion in [E, Section 4] is uniform on complex compact
sets with \(0<\Re w<1\). In the notation
\[
 f(w)=\frac{\operatorname{Li}_2(1)-
                  \operatorname{Li}_2(e^{2\pi iw})}{2\pi i},
 \qquad \mathfrak h(w)^2=i(1-e^{2\pi iw}),
\]
its shifted leading form is
\[
 \mathfrak F_N(Nw+\tau)
    =\sqrt N\,\mathfrak h(w)(1-e^{2\pi iw})^\tau
            e^{Nf(w)}(1+O(N^{-1}))
 \tag{17}
\]
for bounded fixed \(\tau\). This follows by Taylor expansion of
the uniform formula in [E]; \(f'(w)=\log(1-e^{2\pi iw})\).
All marks are inherited from that formula.

It follows directly from (5) that on complex compact sets where
the real parts of all singles and pairs are in \((0,1)\),
\[
 \Gamma_N=\kappa^2N^{-1/2}\mathcal B e^{N\mathcal S}
                                      (1+O(N^{-1})),
 \tag{18}
\]
\[
 \mathcal S=
 \frac{\sum_{\{a,b\}}\operatorname{Li}_2(e^{-2\pi i(a+b)})
       -2\sum_a\operatorname{Li}_2(e^{-2\pi ia})
       +3\operatorname{Li}_2(1)}{2\pi i},\qquad
 \mathcal B=\frac{-i}{\prod_{\{a,b\}}\mathfrak h(1-a-b)}.
 \tag{19}
\]
Each squared single factorial, including its shift \(-1/2\),
has leading amplitude \(iN\); the three pair factors supply the
denominator in (19). This fixes both the phase and the power of \(N\).
The section is holomorphic and nonzero on these compact sets
for large \(N\), by the nonzero strips in [E].

On real \(\mathcal D\), the literal branches give
\[
 \mathcal S=A_0-\pi i(ch+ck+hk),\qquad
 \mathcal B=\frac{e^{\pi i(c+h+k)}}
 {2\sqrt{2\sin\pi(c+h)\sin\pi(c+k)\sin\pi(h+k)}}.
 \tag{20}
\]
For example the real and imaginary parts of
\(\operatorname{Li}_2(e^{-2\pi ix})\), \(0<x<1\), are
\(\pi^2(x^2-x+1/6)\) and \(2\pi L(x)\); substitution gives
(20). The amplitude uses
\(\mathfrak h(1-x)=i e^{-\pi ix/2}\sqrt{2\sin\pi x}\).
These are the canonical marks, not a fresh choice of square root.

For \(a=c+iy\) with other coordinates real,
\[
       \left.\partial_y\Re\mathcal S\right|_{y=0}
                                      =\pi(h+k).
 \tag{21}
\]
At \(p\) this is \(2\pi/3\) in each coordinate. Choose a small
fixed complex product box about \(p\) and an \(\alpha>0\) such
that throughout that box
\[
       \alpha\le\partial_{\Im a_j}\Re\mathcal S
                              \le2\pi-\alpha
                        \qquad(j=1,2,3).
 \tag{22}
\]
Continuity of the analytic function \(\mathcal S\) proves this
simultaneously for complex values of the other coordinates.
This strict band condition, rather than the grid values alone,
will control the interpolation error.

## 4. The exact interpolation remainder selects the normalization

Choose a small real radius \(r>0\). For each \(N\), take endpoints
\[
 u_N=n_-/N=p_1-r+O(N^{-1}),\qquad
 v_N=n_+/N=p_1+r+O(N^{-1}),
 \tag{23}
\]
where \(n_\pm\) are integers. Choose a small fixed height \(\tau>0\)
so that all products of the angular rectangles
\[
          u_N<\Re a<v_N,\qquad |\Im a|<\tau
 \tag{24}
\]
remain in the fixed analytic box of (22). Their activity images
are annular sectors. Use their positively oriented boundaries
\(\mathcal C_N\); the exponential map is one-to-one on each
rectangle when \(r\) is chosen small.

Let \(I_N=\{i:u_N<a_i<v_N\}\) and define the local interpolation
operator in one coordinate by
\[
        (P_j f)(t)=\sum_{i\in I_N} f(C_i)\ell_i(t),
                  \qquad R_j=I-P_j.
 \tag{25}
\]
Other coordinates are parameters. For a function holomorphic on
the sector and its boundary, Cauchy's residue theorem gives
\[
 (R_jf)(t)=\frac{D_N(t)}{2\pi i}
       \int_{\mathcal C_N}
               \frac{f(z)}{(z-t)D_N(z)}\,dz .
 \tag{26}
\]
Indeed the residue at \(z=t\) is \(f(t)\) and the residue at
\(z=C_i\) is \(-f(C_i)\ell_i(t)\). At a grid target the formula
follows by continuity. No division by \(D_N(t)\) is made.
In applying (26) to \(\Gamma_N\), use the local angular logarithm
in its indicated sector; no global periodicity is presumed.

There is a fixed gap \(\gamma>0\) such that every real face of
the box in (23), and every supported grid point outside its
three-dimensional interior, has
\[
                         A_0\le M-\gamma .
 \tag{27}
\]
This is Lemma 1: for large \(N\) such points stay at least
\(r/2\) from \(p\). The face estimate is uniform in the other
two real coordinates of the box.

For a contour angle \(a=x+iy\), its activity satisfies
\(|z|=e^{2\pi y}\). On a vertical side in (24),
\[
                  |D_N(z)|=1+e^{2\pi Ny},
 \tag{28}
\]
because \(Nx=n_\pm\). On the two horizontal sides, for large \(N\),
\[
             |D_N(z)|\ge\tfrac12 e^{2\pi N\max(y,0)}.
 \tag{29}
\]
The same lower bound, without the factor \(1/2\), holds on the
vertical sides. From (18) and (22), with the other two angles
real in the box, we therefore obtain
\[
 \frac{|\Gamma_N(x+iy,\cdot,\cdot)|}{|D_N(z)|}
   \le N^B
       \exp\{N[A_0(x,\cdot,\cdot)-\alpha|y|]\}.
 \tag{30}
\]
For \(y>0\), subtract the \(2\pi Ny\) from the denominator and
integrate the upper bound in (22); for \(y<0\), integrate its
lower bound. This proves (30) in both directions.

Let real targets lie in a fixed smaller box about \(p\).
Their activities are a fixed distance from \(\mathcal C_N\),
and \(|D_N(t)|\le2\). On vertical contour sides (27) applies;
on horizontal sides (30) supplies the loss \(\alpha\tau\).
Thus, with
\(\delta_0=\min(\gamma,\alpha\tau)>0\), (26) implies
\[
          |R_j\Gamma_N|\le N^B e^{N(M-\delta_0)}.
 \tag{31}
\]
This holds uniformly with the other two real coordinates anywhere
in the larger box, not merely at the target.

For real target activities, \(|\ell_i(t)|\le1\), directly from
the finite geometric average in (6). Hence \(\|P_j\|_\infty\le N\).
The exact telescoping identity
\[
 I-P_1P_2P_3=R_1+P_1R_2+P_1P_2R_3
 \tag{32}
\]
and (31) bound the local interpolation remainder by
\(N^B e^{N(M-\delta_0)}\), after changing \(B\). Only one
variable is complex at a time in this argument.

The original full interpolant (9) differs from
\(P_1P_2P_3\Gamma_N\) only in its grid terms outside \(I_N^3\).
By Lemma 2 and (27), their total absolute value is at most
\[
                         N^B e^{N(M-\gamma)}.
 \tag{33}
\]
This bounds the discarded terms of the actual source. It is not
an assumed bound on an unknown boundary packet.

Combining (31)--(33), then shrinking the real target box so that
\(A_0>M-\delta_0/4\), gives
\[
                \varphi_N/\Gamma_N
                       =1+O(N^B e^{-\delta_0 N/2})
 \tag{34}
\]
there, with room to decrease the exponent. Every fractional class
is included.

### A complex seed follows from the same contours

We record the details needed to propagate on complex tubes directly.
Allow target angles to have \(|\Im a_j|\le t_0\), for a small
fixed \(t_0>0\), while remaining separated from the contour boundaries.
The geometric polynomial and its numerator obey
\[
 |\ell_i(e^{-2\pi ia_j})|\le e^{2\pi N(\Im a_j)_+},\qquad
 |D_N(e^{-2\pi ia_j})|\le2e^{2\pi N(\Im a_j)_+}.
 \tag{35}
\]
Consequently the omitted grid sum in (33) costs at most an extra
\(e^{6\pi Nt_0}\).

For the local remainder use
\(P_1P_2P_3=(I-R_1)(I-R_2)(I-R_3)\).
Every nonidentity term is an iterated contour integral (26).
Its Cauchy denominators remain uniformly separated from zero.
First replace each unintegrated target imaginary part by zero.
By (22) this changes \(\Re\mathcal S\) by at most \(6\pi t_0\).
Next move the integrated imaginary parts from zero to their contour
values, one coordinate at a time. Estimate (22), valid jointly
on the complex box, gives (30) in each of these coordinates.
Every nonempty contour term therefore retains either the
real-face gap \(\gamma\) or a horizontal loss \(\alpha\tau\).
Its numerator factors in (35) cost at most another
\(e^{6\pi Nt_0}\). All contour lengths and remaining kernel
factors have fixed bounds. Thus the entire error is bounded by
\[
                N^B e^{N(M-\delta_0+12\pi t_0)}.
 \tag{36}
\]
Choose \(12\pi t_0<\delta_0/4\). Shrink the target real box and,
if necessary, \(t_0\), so that
\(\Re\mathcal S>M-\delta_0/4\) throughout its complex closure.
The lower bound from (18) now turns (36) into an exponentially
small relative error on a fixed complex neighborhood of \(p\).
This proves a complex seed with no maximum-principle continuation
and no fractional-source initializer as input.

## 5. Three-coordinate transport gives the whole pair domain

For completeness we give the exact source identity used for propagation.
It follows from the same full grid, independently of any asymptotic.
Put
\[
 J_N=\frac{\eta}{N}
          [2+C^N+H^N+K^N-(CHK)^N].
\]
Then
\[
 (1-C/q)^2\Phi_N(C/Q,H,K)
       -(1-CH)(1-CK)\Phi_N(C,H,K)=CJ_N,
 \tag{37}
\]
and the other two equations are its permutations.

Here is a short polynomial proof. Let \(W\) be the left side.
On the full grid it is zero: for \(i<d\) supported neighboring
values in (8) have the displayed homogeneous ratio. A transfer
leaving support has \(i+j=d\) or \(i+k=d\), which makes its
corresponding factor \(1-C_iC_j\) or \(1-C_iC_k\) zero.
An inadmissible value cannot become admissible when \(i\)
increases. At \(i=d\), \(C_d=q\) kills the shifted term;
the only supported current value has \(j=k=0\), and then
\(C_dC_0=1\). Thus the cyclic wrap is also included.

The centered duality and \(f_0f_d=1/N\) in [P] give
\[
 [H^d]\Phi_N=\frac{\eta}{N}\sum_{a=0}^d(CK)^a
 \tag{38}
\]
and its permutations. They imply that the coefficients of
\(H^N,K^N,C^{N+1}\) in \(W\) are respectively
\[
 \frac{\eta C}{N}[1-(CK)^N],\quad
 \frac{\eta C}{N}[1-(CH)^N],\quad
 \frac{\eta}{N}[1-(HK)^N].
 \tag{39}
\]
In the last calculation \(q^{-2}Q^{-d}=1\).
They agree with the corresponding coefficients of \(CJ_N\).
The remainder has degrees at most \((N,N-1,N-1)\), vanishes
on the full grid, and hence equals \((C^N+1)R_0(H,K)\).
At \(C=0\) it vanishes identically, so \(R_0=0\). This proves
(37) without division on support walls or at the cyclic wrap.

The factorial shift in (4) gives exactly
\[
 \Gamma_N(c+1/N,h,k)
       =\frac{(1-CH)(1-CK)}{(1-C/q)^2}\Gamma_N(c,h,k).
 \tag{40}
\]
The full multiplier around the \(N\)-step \(C\) cycle remains
\[
 \mathcal M_C=
       \frac{[1-(CH)^N][1-(CK)^N]}{(1+C^N)^2}.
\]
This follows by taking the finite product of (40); it is not
reset to one. Zeros and poles are retained as meromorphic
factors, with the canonical angle marks.
Thus for \(E_N=\varphi_N/\Gamma_N-1\),
\[
 E_N(c+1/N,h,k)-E_N(c,h,k)
  =\frac{CJ_N}
       {(1-C/q)^2\Gamma_N(c+1/N,h,k)}.
 \tag{41}
\]

**Theorem 3.** For every compact
\(\mathcal K\subset\mathcal D\), there is a fixed open complex
neighborhood \(V\) of \(\mathcal K\) and a \(\delta>0\) with
\[
                   \sup_V|E_N|=O(e^{-\delta N}).
 \tag{42}
\]
On a smaller neighborhood the same bound holds for every fixed-order
derivative. It holds for the full sequence of large integer levels.

**Proof.** Enlarge \(\mathcal K\) slightly within the real domain,
retaining compact closure. For a real target \(a\) there, choose
\[
           b_j=1/3+\{N(a_j-1/3)\}/N.
 \tag{43}
\]
These seeds lie in the normalization neighborhood of Section 4
for large \(N\), and \(a_j-b_j\in N^{-1}\mathbb Z\).
Starting at the target, lower coordinates above their seed
values, then raise the others. During the first stage pair sums
decrease; during the second every coordinate is at most its
seed value. Thus the path lies in a fixed compact
\(\mathcal L\subset\mathcal D\), with fewer than \(3N\) steps.
For instance its singles are bounded below by the smaller of
the target lower bound and \(1/3\); for \(N\ge12\), its pair
sums are at most the larger of the target upper bound and \(5/6\).

Let \(m_0=\min_{\mathcal L} A_0>0\).
For a complex target \(a+iy\) use the same real path with the
same imaginary vector \(y\) at every point, including its seed.
Choose a fixed height \(t>0\) so small that the seed belongs to
the complex neighborhood already proved, all factorial strips
keep positive margins, and throughout the complex path box
\[
       \Re\mathcal S\ge m_0/2,\qquad
                         6\pi t<m_0/4 .
 \tag{44}
\]
The first inequality follows from continuity and compactness.
Equation (18) bounds the shifted Gamma denominator below by
\(N^{-B}e^{Nm_0/2}\). The single-angle margins keep
\(|1-C/q|\), and its permutations, uniformly away from zero.
At \(|y_j|\le t\) the literal forcing obeys
\[
                       |J_N|\le(6/N)e^{6\pi Nt}.
 \tag{45}
\]
Each increment in (41) is therefore at most
\(N^B e^{-Nm_0/4}\), after changing constants. Reverse steps
use the forward identity at the lower endpoint, with the
opposite sign. Both endpoints lie in the same compact path box.

The complex seed error is exponentially small by Section 4.
Summing fewer than \(3N\) increments proves (42), absorbing
polynomial factors by decreasing \(\delta\). Open real buffers
and a smaller fixed height give an open complex neighborhood.
Cauchy's formula on a smaller neighborhood proves the
fixed-order derivative assertion. \(\square\)

This proof does not divide by \(J_N\), a cyclic-norm numerator,
or \(1+C^N\). Resonant fractional classes, both parities and
composite levels remain included. No fixed neighborhood at a
boundary of \(\mathcal D\), or estimate of derivative orders
growing with \(N\), is asserted.

## 6. Consequence and scope

Equations (18)--(20) now give a nonzero leading asymptotic for
the original crossing source on every real compact subset of
\(\mathcal D\), and on an appropriate fixed complex neighborhood
with the canonical branches retained. The error relative to the
exact Gamma section is exponentially small. The leading
Stirling approximation itself still has its stated \(O(N^{-1})\)
error.

The normalization is a consequence of the original Fourier
bandwidth, its exact grid, the strict concavity of its actual
magnitude profile, and the Cauchy remainder estimate. Orthogonality
is used in the full-grid reconstruction; interpolation error is
estimated before drawing a conclusion about a nonzero scalar.
No independent summand magnitudes are substituted for the
original source.

This is a simpler proof of the local result, not a global
Conway-gluing theorem. It does not replace physical boundary
spaces by a bounded-dimensional affine solution space. The
inverse pairings, support projections, ordered crossings and
turns, larger complex continuations, and original closing
functional still require control in a general short component.
The nonzero geometric contribution needed for finitely many
exceptional filling assignments remains unproved.

Only two complete direct proof texts are used:

| Label | Complete source | SHA-256 |
|---|---|---|
| P | [Exact pairwise source, 668 lines](research_exact_pairwise_conway_source.md) | 470c9df0384274623a1aa0b6939067021894f2fea41595dfa7440081ca77f1d1 |
| E | [Canonical factorial and complex strips, 226 lines](exact_factorial_interpolation_and_complex_contours.md) | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |

Both entire matching sources were read. The finite grid, original
algebra and exact tensor magnitudes are imported from [P].
The literal canonical factorial and its uniform complex expansion
are imported from [E]. All selection and transport estimates are
proved above. The earlier fractional-source theorem is not a
proof input. No novelty is claimed for Cauchy's interpolation
formula or finite Fourier reconstruction as general methods.
Only written mathematics and text operations were used.
