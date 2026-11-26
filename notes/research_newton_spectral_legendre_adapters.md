# Local spectral adapters for the original Newton gates

Private written proof, 15 November 2026.

The exact Newton multiplication and signed crossing gates admit explicit
one-variable spectral generating families. Their critical values,
nonzero fiber Hessians and Gaussian densities agree with the original
factorial formulas. The multiplication statement includes the high
indices of the actual source. The crossing statement records the
integer Fourier character needed to compare the two analytic lifts.

These identities give a local comparison of the complete Newton and
angular phases when a specified factorization has regular intermediate
labels. They do not prove that an arbitrary positive angular point has
such labels, or that the original integration cycle contains its local
Gaussian class. In particular, they do not transport the entire
inverse-period descent contour through a stationary elimination.

## 1. The exact coefficient dual and the value phase

For \(N\ge3\), put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad
 S_j=\prod_{h=1}^j2\sin(\pi h/N),\quad
 c_j=2\cos((2j+1)\pi/N),
\]
\[
 e_j(c)=S_j^{-2}\prod_{h<j}(c_h-c),\qquad
 \mathcal A_N=\mathbb C[c]/(2T_N(c/2)+2).
 \tag{1}
\]
All quotient statements include the first normals at double nodes.
The original pairing is \(\phi_N(e_i e_j)=\delta_{i+j,D}\),
and the actual turn sends \(e_i\) to \(e_{D-i}\).

If \(f\) is holomorphic around all nodes and represents its full
Hermite data, its canonical Newton coefficient has the exact formula
\[
 \begin{aligned}
 \alpha_r(f)
 &=\frac{(-1)^rS_r^2}{2\pi i}
       \oint\frac{f(c)}{\prod_{j=0}^r(c-c_j)}\,dc\\
 &=-\frac1{2\pi i\,[2\sin(\pi(r+1)/N)]^2}
       \oint\frac{f(c)}{e_{r+1}(c)}\,dc\qquad(r<D).
 \end{aligned}
 \tag{2}
\]
The contour surrounds the prefix nodes, with their repeated-node
multiplicities; it need not surround any other node. This is the
Cauchy divided difference: expanding in the monic Newton basis proves
the first equality, and the definition of \(e_{r+1}\) proves the
second. Consequently it applies to the original quotient coefficients,
not merely to values at distinct roots.

For the crossing, the exact analytic representative is
\[
 R^n(c)=q^{nD^2/4}\exp\{nK(c)/(2\hbar)\},\qquad
 K(c)=\operatorname{arccosh}(-c/2)^2,\quad
 \hbar=2\pi i/N,
 \tag{3}
\]
on \(\mathbb C\setminus[2,\infty)\). Here and below the fractional
power of \(q\) uses \(\log q=\pi i/N\). Formula (3) is the
actual full-Hermite crossing for every signed integer \(n\), by
the pinned direct-power source. It is not an assertion about a
generic-\(q\) continuation or an arbitrary free-boundary power.

Write
\[
 C(s)=2\cos(2\pi s),\qquad
 J(x)=\int_0^x\log(2\sin\pi s)\,ds,
\]
\[
 B(x,c)=\int_0^x\Log(C(s)-c)\,ds-2J(x).
 \tag{4}
\]
The real branch of \(J\) is used on \((0,1)\). Every continuation
of (4) below specifies its logarithms. On a compact regular product
chart, midpoint summation and the original sine-factorial asymptotic
give, at integer \(Nx\),
\[
 e_{Nx}(c)=\frac{e^{NB(x,c)}}{2N\sin\pi x}
                         (1+O(N^{-1})).
 \tag{5}
\]
The expansion holds with fixed derivatives in regular parameters.
For a ratio of Newton products, cancel common factors before applying
it; no separate estimate across a common node cut is needed.

Let \(c=-2\cos t\), \(\Im t<0\), \(|\Re t|<\pi\).
Fix the value logarithm by
\[
 C(s)-c=e^{it}(1+e^{-it+2\pi is})(1+e^{-it-2\pi is}),
 \tag{6}
\]
using the power-series logarithms of the last two factors. Since
\(|e^{-it}|<1\), integration over a period and reflection give
\[
 B(1,c)=it,\qquad B(1-x,c)=B(1,c)-B(x,c).
 \tag{7}
\]
The second identity also uses \(J(1-x)=-J(x)\). In particular the
complementary Newton dual supplies the original trace charge itself;
one must not insert a second charge by hand.

The local derivatives used below are
\[
 B_x=\Log\frac{C(x)-c}{4\sin^2\pi x},\qquad
 B_{xc}=-\frac1{C(x)-c},
 \tag{8}
\]
\[
 B_t=-\frac1{2\pi}
 \left\{\Log\cos(t/2-\pi x)-\Log\cos(t/2+\pi x)\right\}
 =-\frac1\pi\operatorname{artanh}
                     \bigl(\tan(t/2)\tan\pi x\bigr).
 \tag{9}
\]
The logs in (9) are continued in \(x\) from zero. The last notation
includes that continued logarithmic lift, particularly across
\(x=1/2\); it is not an instruction to reset a principal artanh.

## 2. Multiplication: primitive, Hessian and density

Use the entire strict multiplication domain
\[
 0<x,\quad0<y,\qquad\max(x,y)<z<x+y<1.
 \tag{10}
\]
Set
\[
 X=\pi x,\quad Y=\pi y,\quad Z=\pi z,\quad A=X+Y-Z,
 \qquad
 \lambda=\frac{\sin X\sin Y\sin Z}{\sin A},\quad
 c_*=2-4\lambda.
 \tag{11}
\]
The original factorial multiplication coefficient is
\[
 \mu_{ijr}=\frac{S_{i+j}S_r}
 {S_iS_jS_{r-i}S_{r-j}S_{i+j-r}},
 \qquad i=Nx,\ j=Ny,\ r=Nz,
 \tag{12}
\]
and its phase is
\[
 m=J(x+y)+J(z)-J(x)-J(y)
                   -J(z-x)-J(z-y)-J(x+y-z).
 \tag{13}
\]
Its spectral generating family is
\[
 L(c)=B(x,c)+B(y,c)-B(z,c).
 \tag{14}
\]
For example, if \(x\le y\), the definition at the selected saddle
is the canceled expression
\[
 L(c)=\int_0^x\log(C(s)-c)\,ds
        -\int_y^z\log(C(s)-c)\,ds
        -2J(x)-2J(y)+2J(z).
 \tag{15}
\]
All retained factors in (15) are positive at \(c=c_*\).

**Proposition 1.** On all of (10), with these real logarithms,
\[
 L_c(c_*)=0,\qquad L(c_*)=m,
 \tag{16}
\]
\[
 \boxed{\quad
 L_{cc}(c_*)=
 \frac{\sin^2 A}
 {16\pi\lambda\sin(X+Y)\sin(Z-X)\sin(Z-Y)}>0.
 \quad}
 \tag{17}
\]
In particular there is no singularity at a high index or at
\(\lambda=1\).

**Proof.** The three elementary identities
\[
 \begin{aligned}
 \lambda-\sin^2X
 &=\frac{\sin X\sin(X+Y)\sin(Z-X)}{\sin A},\\
 \lambda-\sin^2Y
 &=\frac{\sin Y\sin(X+Y)\sin(Z-Y)}{\sin A},\\
 \lambda-\sin^2Z
 &=\frac{\sin Z\sin(Z-X)\sin(Z-Y)}{\sin A}
 \end{aligned}
 \tag{18}
\]
are strictly positive. Since \(\min(x,y)<1/2\), the first retained
interval in (15) has \(C(s)>c_*\). On the second interval the same
follows from its endpoints unless it crosses \(1/2\). In that case
\(X,Y<\pi/2<Z\), and
\[
 \lambda-1=
 \frac{\cos X\cos Y\sin Z-\sin(X+Y)\cos Z}{\sin A}>0.
 \tag{19}
\]
Thus \(c_*<-2\), which handles that case as well. The canceled
integrals are real analytic throughout the connected domain (10).

To check stationarity without losing a logarithmic branch, first take
\(\lambda>1\), put \(k=\sqrt{(\lambda-1)/\lambda}\), and use
the continuous primitive
\[
 \int_0^s\frac{du}{C(u)-c_*}
 =\frac{\arg(\cos\pi s+ik\sin\pi s)}
                   {4\pi\sqrt{\lambda(\lambda-1)}}.
 \tag{20}
\]
The argument lies in \((0,\pi)\) for \(0<s<1\).
Substitution of (11) into the tangent addition formula gives
\(F(x)+F(y)=F(z)\), where \(F\) is that argument: equality
of tangents is equality here because \(x+y<1\) implies
\(F(x)+F(y)<\pi\). This proves \(L_c(c_*)=0\) on a nonempty
open subset. Real-analytic continuation using (18)--(19) proves it
on all of (10), including \(\lambda=1\).

By (8) and (18), the three derivatives of \(L(c_*)\) in
\(x,y,z\) agree with those of (13). The difference is constant.
Let \(z\uparrow x+y\), with \(x+y<1/2\) fixed. Then
\(c_*\to-\infty\),
\((x+y-z)\log(-c_*)\to0\), and both expressions tend to
\(2[J(x+y)-J(x)-J(y)]\). The constant is zero.

Finally
\[
 \lambda_z=\frac{\pi\lambda\sin(X+Y)}{\sin Z\sin A}.
\]
Differentiate \(L_c(c_*)=0\) in \(z\), using
\(L_{cz}=1/(C(z)-c_*)\) and \((c_*)_z=-4\lambda_z\).
This gives \(L_{cc}=1/[4\lambda_z(C(z)-c_*)]\), which is
(17). \(\square\)

The angular coordinate can have a removable caustic:
\(\lambda=\cos^2(t/2)=1\) gives \(t=0\) and
\(L_{tt}=0\), while the spectral Hessian (17) remains nonzero.
The old edge square root is absent from these formulas.
This statement concerns the multiplication gate. The global trace
term \(-it\) has a spectral square-root coordinate at \(c=-2\);
no removal of that global angular degeneration is asserted.

There is also a normalization identity. After exact cancellation in
(2), the spectral integrand of \(\mu\), apart from \(dc/(2\pi i)\),
has the expansion
\[
 N^{-1}d(c)e^{NL(c)}(1+O(N^{-1})),\qquad
 d(c)=-\frac{\sin Z}
               {2\sin X\sin Y(C(z)-c)}.
 \tag{21}
\]
This follows from (5), or directly by midpoint summation over the two
retained intervals in (15); the latter proof includes the high-index
cases with common canceled cuts. In contrast, (12) gives
\[
 \mu_{Nx,Ny,Nz}=N^{-3/2}\rho_m e^{Nm}(1+O(N^{-1})),
\]
\[
 \rho_m^2=
 \frac{\sin(X+Y)\sin Z}
 {8\sin X\sin Y\sin(Z-X)\sin(Z-Y)\sin A}.
 \tag{22}
\]
Equations (17)--(18) imply the exact positive identity
\[
             \frac{-d(c_*)}{\sqrt{2\pi L_{cc}(c_*)}}=\rho_m.
 \tag{23}
\]
Indeed \(d(c_*)<0\), and a downward vertical Gaussian through
\(c_*\) has the additional minus sign from \(dc/(2\pi i)\).
This is also the orientation of the left side of a positively
enclosing Cauchy contour. Equation (23) identifies its local oriented
Gaussian with the actual factorial density. It does not assert that
a global contour deformation retains only this local segment.

## 3. Both signed crossings, including the Fourier lift

Use the multiplication matrix \(M_\sigma\) of \(R^\sigma\),
with output \(i=Nx\), input \(j=Ny\), and
\[
                         0<y<x<1.
 \tag{24}
\]
The boundary operator denoted \(C_\sigma\) in the corner source
is its transpose. The actual entries and their strict factorial phase
are
\[
 (M_\sigma)_{ij}=\kappa^\sigma(-1)^i q^{\sigma i(j+1)}
                  \frac{S_i}{S_jS_{i-j}},\qquad
 \kappa=q^{D^2/2},\quad\sigma=\pm1,
 \tag{25}
\]
\[
 h=J(x)-J(y)-J(x-y),\qquad
 F_\sigma=h+\sigma i\pi(1/2+x+xy),
 \tag{26}
\]
\[
 (M_\sigma)_{Nx,Ny}
 =N^{-1/2}a_\sigma e^{NF_\sigma}(1+O(N^{-1})),\qquad
 a_\sigma=-e^{\sigma i\pi x}
       \sqrt{\frac{\sin\pi x}{2\sin\pi y\sin\pi(x-y)}}.
 \tag{27}
\]
The square root is positive on (24). These are precisely the original
entries, with \(\sigma\)-dependent interpolation of \((-1)^i\).

Set
\[
 X=\pi x,\quad Y=\pi y,\quad\Delta=X-Y,\qquad
 \lambda_\sigma=\sin X\sin Y\,e^{i\sigma\Delta},\qquad
 c_\sigma=2-4\lambda_\sigma.
 \tag{28}
\]
The imaginary part of \(c_\sigma\) has sign \(-\sigma\).
Choose \(c=-2\cos t\) with
\(t=\sigma\theta-iH\), \(0<\theta<\pi\), \(H>0\).
Use the principal logarithm of \(C(s)-c\), whose imaginary part
has sign \(\sigma\). It agrees with (6) by continuation from
\(s=0\). Define
\[
 Q_\sigma(c)=B(y,c)-B(x,c)
                +\sigma i\left(\frac\pi4+\frac{t(c)^2}{4\pi}\right).
 \tag{29}
\]

**Proposition 2.** On the whole strict triangle (24),
\[
 (Q_\sigma)_c(c_\sigma)=0,\qquad
 Q_\sigma(c_\sigma)=F_\sigma-2\pi i\sigma x,
 \tag{30}
\]
\[
 \boxed{\quad
 (Q_\sigma)_{cc}(c_\sigma)=
 -\frac{e^{-2i\sigma\Delta}}
       {16\pi\sin X\sin Y\sin\Delta}\ne0.
 \quad}
 \tag{31}
\]

**Proof.** Put
\(\ell_x=\Log\cos(t/2-X)-\Log\cos(t/2+X)\), continued
as in (9). Then
\(2\pi(Q_\sigma)_t=\ell_x-\ell_y+\sigma it\).
Substituting (28), and applying the tangent addition formula, gives
\(\exp(\ell_x-\ell_y+\sigma it)=1\).
Its logarithm is a locally constant multiple of \(2\pi i\) on
the connected strict triangle. As \(y\downarrow0\),
\(t\to\sigma\pi\) from the lower half-plane,
\(B_t(y,c_\sigma)\to0\), and
\(B_t(x,c_\sigma)\to i/2\). Hence that multiple is zero.
Since \(dc/dt\ne0\) here, spectral stationarity follows.

For the critical value use
\[
 \begin{aligned}
 C(x)-c_\sigma&=-4\sin X\,e^{-i\sigma Y}\sin\Delta,\\
 C(y)-c_\sigma&= 4\sin Y\,e^{ i\sigma X}\sin\Delta.
 \end{aligned}
 \tag{32}
\]
The specified principal logarithms give
\[
 (Q_\sigma(c_\sigma))_x=h_x+\sigma i\pi(y-1),\qquad
 (Q_\sigma(c_\sigma))_y=h_y+\sigma i\pi x.
 \tag{33}
\]
They are the derivatives of \(F_\sigma-2\pi i\sigma x\).
In the same limit \(y\downarrow0\),
\(B(y,c_\sigma)\to0\),
\(B(x,c_\sigma)\to\sigma i\pi x\), and the Gaussian term
in (29) tends to \(\sigma i\pi/2\). The additive constant
therefore vanishes.

Finally
\((Q_\sigma)_{cx}=1/(C(x)-c)\) and
\((c_\sigma)_x=-4\pi\sin Y\,e^{i\sigma(2X-Y)}\).
Differentiate the first equation of (30) in \(x\), and use (32).
This gives (31). \(\square\)

The density retains the subleading carrier:
\[
 q^{\sigma D^2/4}
  =e^{\sigma i\pi N/4}e^{-\sigma i\pi/2}
                      e^{\sigma i\pi/(4N)}.
 \tag{34}
\]
Using (2) with \(f=R^\sigma e_j\), the leading spectral density
is
\[
 d_\sigma(c)=\frac{\sigma i\sin X}
                         {\sin Y(C(x)-c)},\qquad
 d_\sigma(c_\sigma)=
             -\frac{\sigma i e^{i\sigma Y}}
                         {4\sin Y\sin\Delta}.
 \tag{35}
\]
The factor \(-\sigma i\) in (34) is essential. Direct substitution
gives the exact density identity
\[
 \boxed{\qquad
 \frac{d_\sigma(c_\sigma)^2}
      {2\pi(Q_\sigma)_{cc}(c_\sigma)}=a_\sigma^2.
 \qquad}
 \tag{36}
\]
Thus one may choose the oriented local Gaussian branch to have the
original density (27), continuously on the strict triangle. The
square identity does not determine the intersection number of the
original Cauchy cycle with that branch. Choosing this local orientation
is not a proof of its contribution to a global period.

The linear difference in (30) has a precise lattice meaning:
\(e^{-2\pi i\sigma i}=1\) for the actual output integer \(i\).
If \(i=Nx+\delta_i\), \(j=Ny+\delta_j\) are reconstructed
labels with fixed integer offsets, the density gains the factors
\(e^{\delta_i(F_\sigma)_x+\delta_j(F_\sigma)_y}\).
Using the spectral lift instead changes this by
\(e^{-2\pi i\sigma\delta_i}=1\). This includes the literal
offset \(-1\) in \(D-r\). Multiplication offsets are handled
by the identical differentiation of (16). These facts reconcile the
integer-grid weights at both level parities.

Off the grid, \(-2\pi i\sigma x\) is not zero. It must be
kept as a change of the Fourier character of the lattice sum. Dropping
it from a fixed complex integrand would change its stationary equation.

## 4. What can be sewn locally in the whole original source

Here is an explicit scope in which the adapters compare complete
phases. Use the actual same-index circle-tree kernels, fixed outside
angles, and signed integer powers \(n_v\). At every selected vertex
of degree \(d_v\), multiply its first \(d_v-1\) incident Newton
factors by a binary tree, apply a chain of \(|n_v|\) crossings to
that product, and pair its output with the last incident factor using
the original \(\phi_N\). Assume
\[
 d_v\ge2,\qquad G_v=d_v-2+|n_v|\ge1.
 \tag{37}
\]
Thus each vertex has at least one gate. Degree-one traces and the
degree-two zero-power delta constraint are not silently put into a
strict saddle chart. They require a separate resolution.

There is one spectral variable \(c_g\) for each gate and one
index variable for each internal gate seam. Replace a multiplication
gate by (14), and a crossing by (29), keeping the Fourier lift (30).
Use the original leaf value phases (4). The last output label is
\(D-j\), where \(j\) is the remaining leaf label; at leading
order it is \(1-j/N\), with the exact offset retained in the
density. This constructs a single holomorphic hybrid phase \(\mathcal H\).

The complementary density can also be checked before any asymptotic.
Node reversal and \(S_rS_{D-r}=N\) give
\[
 e_r(c)e_{D-r}(c)
      =\frac{(-1)^NP_N(c)}{N^2(c_r-c)},\qquad
 P_N(c)=2T_N(c/2)+2.
 \tag{37a}
\]
Indeed the two unnormalized products contain every factor of
\(\prod_{j=0}^{N-1}(c_j-c)\) except its \(r\)-th factor,
with multiplicities. Thus on a compact lower angular chart the
complementary value product has phase \(it\) and density
\(1/[N^2(C(r/N)-c)]\). The exact \(-1\) reversal offset is
responsible for this density. Moreover the original trace itself is
\[
 \phi_N(f)=\frac{(-1)^D N^2}{2\pi i}
                      \oint\frac{f(c)}{P_N(c)}\,dc.
 \tag{37b}
\]
Since
\(P_N(-2\cos t)=(-1)^N(e^{iNt}+e^{-iNt})+2\), its local
lower-half-plane integrand in the \(t\) coordinate has the exact
leading trace factor
\[
                  -\frac{N^2\sin t}{\pi i}\,e^{-iNt}
                             (1+O(e^{-N\epsilon})),
 \tag{37c}
\]
on every compact set with \(\Im t\le-\epsilon<0\).
This checks both the primitive charge and the finite normalization.
It does not delete the other parts of the actual residue contour.

Suppose a full critical point of this hybrid phase satisfies all the
following regularity conditions:

* Every gate lies in a specified analytic continuation of the strict
  chart (10) or (24), on which the identities (16), (30), the nonzero
  Hessians (17), (31), and the stated factorial asymptotics continue.
  In particular, remaining in a nonsingular algebraic locus alone is
  not being substituted for a valid factorial interpolation chart.
* Every seam has \(C(r)-c_g\ne0\), and its logarithmic lifts agree
  with the original primitive and Fourier characters.
* The equal vertex spectral variables have regular angular coordinates
  on the branch (6), and their stationary edge indices lie on the
  original regular wire branches. A claimed positive geometric point
  means the canonical positive branches of the pinned angular source.

**Proposition 3.** At such a point the lifted Newton phase and the
original unsummed angular phase are stably equivalent holomorphic
critical germs. Their critical values agree, including the known
crossing scalar phase. Nondegeneracy of one reduced germ is equivalent
to nondegeneracy of the other. In particular, at a regular positive
primitive angular critical point admitting this specified lift, the
full lifted Newton Hessian is nondegenerate and has a local descent
contour. The local gate Gaussian factors are (23) and (36).

**Proof.** First eliminate all \(c_g\), keeping the Newton labels
fixed. Their Hessian block is diagonal, with entries (17) or (31).
The resulting critical action is exactly the factorial Newton phase
with the linear characters \(-2\pi i\sigma x_g\) retained.
The holomorphic Morse lemma with parameters therefore writes
\(\mathcal H\) as that Newton phase plus nondegenerate quadratic
fiber terms, locally.

For the other reduction, a seam from a child to its parent contributes
\[
                         -B(r,c_{\rm child})+B(r,c_{\rm parent}).
 \tag{38}
\]
By (8), its stationary equation forces the two spectral variables
to agree on the stated lift. The gate graph at one vertex is a tree.
Use one common \(c_v\) and one spectral difference for each
internal seam. The mixed Hessian between seam labels and these
differences is an invertible diagonal matrix, up to the invertible
tree incidence change of coordinates: its entries are
\(-1/(C(r)-c_v)\). The seam-by-seam block has the form
\[
                  \begin{pmatrix}0&A\\A^{\mathsf T}&E\end{pmatrix},
                    \qquad \det A\ne0.
 \tag{39}
\]
It is nondegenerate, regardless of \(E\). Its stationary reduction
sets the spectral differences to zero and solves for the seam labels.

At the final pairing, (7) gives
\(-B(1-x,c_v)=B(x,c_v)-it_v\). All other internal value phases
cancel in (38). The remaining phase is therefore exactly
\[
 \sum_{(e,v)}B(x_e,-2\cos t_v)
 +\sum_{v\in S}\left(\frac{i n_vt_v^2}{4\pi}-it_v\right)
 +\frac{i\pi}{4}\sum_{v\in S}n_v.
 \tag{40}
\]
The last constant is the leading phase of the literal scalar
\(q^{n_vD^2/4}\); its finite subscalars remain in (34).
The first two terms are the pinned original unsummed phase, with
outside value factors retained. Thus this second elimination gives
the angular phase plus nondegenerate quadratic blocks.

The determinant/Schur-complement identity for either elimination
shows that its reduced Hessian is nonsingular exactly when the
hybrid Hessian is. This proves stable equivalence and nondegeneracy.
At a regular positive point the original wire Hessians and reduced
angular Hessian are nondegenerate by the pinned unsummed-phase proof.
Its local adapted contour, or directly the holomorphic Morse lemma,
therefore supplies a local descent contour for the Newton germ too.
The density comparisons are the local one-variable Gaussian
identities already proved. No statement about global cycles is used.
\(\square\)

The proof applies equally to a different specified binary resolution
whose seam incidence matrix has the same tree rank. It does not replace
an original reversed-index edge by a same-index edge. Any such change
would require its own exact turn and boundary correspondence.

## 5. Prefix tests and the remaining contour issue

There is a concrete test for the regularity hypothesis in Proposition 3.
For \(a_v=\tan(t_v/2)\ne0\), attach to a partial product its
continued return
\[
 R_A=\sum_{e\in A}r_{v,e}-\frac{i n_A t_v}{2},
 \tag{41}
\]
where \(n_A\) is the signed number of crossing layers already
applied to that partial product. Equation (9) and gate stationarity
give addition of the returns at a multiplication gate, and subtraction
of \(i\sigma t_v/2\) at a crossing. Hence the intermediate output
label must satisfy
\[
 \tan(\pi r_A)=\frac{\tanh R_A}{a_v},\qquad
 e^{2\pi i r_A}=
 \frac{a_v\cosh R_A+i\sinh R_A}
      {a_v\cosh R_A-i\sinh R_A}.
 \tag{42}
\]
The logarithmic label and the return retain the previously chosen
lifts. Equation (42) is a reconstruction test, not a license to reset
every label to a principal strip. At the final trace, the total return
is \(-\pi i\); the complementary last leaf and output labels in
(7) implement that charge without treating the top coefficient as a
strict free variable.

One apparent divisor is excluded for a finite regular prefix.
If \(a_v\ne0\), \(1+a_v^2\ne0\), \(R_A\) is finite, and
both numerator and denominator in (42) are nonzero, direct substitution
gives
\[
 C(r_A)-c_v=
 \frac{4a_v^2}
 {(1+a_v^2)(a_v^2\cosh^2 R_A+\sinh^2 R_A)}\ne0.
 \tag{42a}
\]
Thus a node collision cannot occur at such a prefix. Zeros of the
numerator or denominator in (42), vanishing factorial sines, and exit
from the specified factorial chart remain possible failures; the
collision can occur only after a regularity assumption has failed.
Positive angular geometry alone has not here been proved to exclude
these remaining failures for arbitrary fixed signed words. A failure
of one factorization is not an intrinsic failure of the finite source:
adjacent crossing powers can be fused exactly by (3), and a different
binary product resolution can change the proper prefixes.

There is also a distinction between a critical germ and a finite
descent collar. The inverse-period contour in the pinned source has
\(P(t)=\xi-\pi i\mathbf1\), with real \(\xi\) near zero.
Except at \(\xi=0\), it need not lie in the stationary graph that
eliminates the gate spectral variables. Already at a trivalent
zero-power vertex,
\[
 B(x,c)+B(y,c)-B(1-z,c)
       =B(x,c)+B(y,c)+B(z,c)-it,
 \tag{43}
\]
and spectral stationarity is precisely that vertex's primitive
equation. Thus Proposition 3 gives local stable equivalence at the
critical point; it does not give a pointwise pullback of the entire
inverse-period collar or its prescribed boundary gap.

Finally, (2) and the original integer-residue formulation supply
actual finite starting cycles, with all confluent poles, support
endpoints and modes retained. Neither the gate calculation nor stable
Morse equivalence computes their coefficient on the selected local
Gaussian class. Proving that coefficient is nonzero, controlling the
other pieces of the full contraction, and treating short fillings
outside these regular charts remain separate tasks.

## Pinned direct sources

* `notes/research_corner_newton_source_transport.md`, SHA256
  `24a7f6f721d0a925405424d9a8aba1ac9db8ce7e90ddb937b2a317e10f98b345`:
  the actual transpose convention, both signed entries and factorial
  densities, literal offsets, exact original residue cycle, and the
  distinction between coefficient transport and boundary evaluation.
* `notes/actual_direct_long_power_source.md`, SHA256
  `7c69dbee41401b1d46fa1db1e6046eca0dbde73429eecbead01e6a3bc6067df0`:
  exact Gaussian representative (3), including every full-Hermite
  normal and the original fractional carrier lift for signed powers.
* `notes/actual_positive_newton_multiplication.md`, SHA256
  `543b5be6035ecec349ce8e78ee47085345ceefe4fc51e5f2005b802d999805bb`:
  exact all-index multiplication (12), full Newton pairing and actual
  turn. No positivity for a signed crossing is inferred from it.
* `notes/research_unsummed_network_phase_coercivity.md`, SHA256
  `b5441bb508d3ffad3274e38dda2d6aeb099d08ae2ab043a0d12c25234e4a1e1e`:
  the original same-index angular phase, continued edge stationary
  value, nonzero wire Hessian and adapted local positive contour.
* `notes/research_positive_period_inverse_descent.md`, SHA256
  `b9b5c3d61c704700e9431315cf50591c921ebeb95becdf6a52877606bdbc4565`:
  the separate inverse-period collar and its action normalization,
  used here to state exactly why local stationary equivalence does
  not by itself transport that collar or the original finite cycle.

All derivations and checks are written mathematics and source-text
reads. No mathematical code, numerical computation, test or compilation
was run. No frozen manuscript or other note was edited.
