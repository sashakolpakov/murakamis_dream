# An exact pairwise presentation of the original Conway source

22 November 2026. Written research draft.
Earlier author-final notes and public manuscripts remain unchanged.

Every multiplication in the original finite Conway algebra can be
written with one weighted Frobenius tensor. That tensor factors into
three explicit pair weights. Its inverse edge metric has an equally
explicit factorial formula. This gives a finite sum for any literal
Conway tree using pair weights, quadratic phases, the prescribed turns,
and the original boundary vectors.

The same tensor is the exact polynomial interpolant of the canonical
Gamma section on a specified coherent parameter grid. The grid gives
the entire Newton basis, including its Hermite directions. It is not
evaluation only at distinct Casimir roots.

The weights below have positive sine-product magnitudes and retained
complex phases. No positivity of the scalar sum, asymptotic lower
bound, or volume theorem is inferred.

## 1. The full original algebra

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=q^{d^2/2}.
 \tag{1}
\]
Every fractional power of \(q\) means the displayed exponential.
For \(r\ge0\) write
\[
 F_r=(Q;Q)_r=\prod_{a=1}^r(1-Q^a),\qquad
 S_r=\prod_{a=1}^r2\sin(\pi a/N)\quad(0\le r\le d).
 \tag{2}
\]
Empty products are one. The factors \(F_r,S_r\) are nonzero for
\(0\le r\le d\); \(F_N=0\). We allow higher \(F_r\) only as
numerators of finite identities. In particular, no division by
\(F_N\) is made.

The complete source algebra and normalized Newton basis are
\[
 \mathcal H_N=\mathbb C[z]/(2T_N(z/2)+2),\qquad
 e_r=S_r^{-2}\prod_{a=0}^{r-1}(c_a-z),\qquad
 c_a=2\cos((2a+1)\pi/N).
 \tag{3}
\]
The positive coefficient norm makes \(e_0,\ldots,e_d\) Hermitian
orthonormal. This is the specified Newton norm; no comparison to
another physical Hilbert--Schmidt norm is assumed.
The original bilinear pairing, closures, turn, and signed crossings
from the complete compiler [C] are
\[
 \begin{gathered}
 \phi(e_ie_j)=\delta_{i+j,d},\qquad
 \phi\Bigl(\sum_i x_i e_i\Bigr)=x_d,\qquad
 m\Bigl(\sum_i x_i e_i\Bigr)=x_0,\\
 J_e e_i=e_{d-i},\qquad
 R^+=\kappa\sum_i(-q)^i e_i,\qquad
 R^-=\kappa^{-1}\sum_i(-q)^{-i}e_i,\qquad R^+R^-=1.
 \end{gathered}
 \tag{4}
\]
Here \(J_e\) also denotes the reversal matrix on coefficient columns.
The basis vectors are real under coefficient reflection
\(a^\sharp(z)=\overline{a(\bar z)}\).

Put
\[
 u=f_0=R^+/\sqrt N,\qquad v=u^{-1}=Nf_d=\sqrt N R^-,
 \qquad
 g_{ij}=\phi(ue_ie_j),\qquad A_{ijk}=\phi(ue_ie_je_k).
 \tag{5}
\]
These are bilinear tensors, without conjugation of their inputs.
The inverse in (5) exists in the entire nonreduced algebra.
The original Newton product is
\[
 e_ie_j=\sum_{\ell=\max(i,j)}^{i+j}
 \frac{S_{i+j}S_\ell}
 {S_iS_jS_{\ell-i}S_{\ell-j}S_{i+j-\ell}}e_\ell
 \quad(i+j\le d),
 \qquad e_ie_j=0\quad(i+j\ge N).
 \tag{6}
\]
Both assertions in (6) hold in the full quotient, with all repeated-root
normals, by [C].

## 2. The explicit pair weights and vertex

**Theorem 1.** The weighted pair metric is
\[
 \boxed{\quad
 g_{ij}=
 \frac{\kappa^{-1}}{\sqrt N}(-1)^{i+j}q^{-i-j-ij}
                  \frac{S_{i+j}}{S_iS_j}
 \quad(i+j\le d),\qquad g_{ij}=0\quad(i+j\ge N).
 \quad}
 \tag{7}
\]
Its inverse \(h=g^{-1}\) is
\[
 \boxed{\quad
 h_{ij}=
 \frac{\kappa^{-1}}{\sqrt N}q^{ij}
                  \frac{S_iS_j}{S_{i+j-d}}
 \quad(i+j\ge d),\qquad h_{ij}=0\quad(i+j<d).
 \quad}
 \tag{8}
\]
The three-index tensor is zero unless all three pair sums are at
most \(d\). On that support, with \(s=i+j+k\),
\[
 \boxed{\quad
 A_{ijk}=
 \frac{\kappa^{-1}}{\sqrt N}(-1)^s q^{-s-ij-ik-jk}
 \frac{S_{i+j}S_{i+k}S_{j+k}}{S_i^2S_j^2S_k^2}.
 \quad}
 \tag{9}
\]
Equivalently, on the same support,
\[
 A_{ijk}=
 \frac{\kappa^{-1}}{N^{7/2}}(-1)^s q^{-s-ij-ik-jk}
 \frac{S_{d-i}^2S_{d-j}^2S_{d-k}^2}
      {S_{d-i-j}S_{d-i-k}S_{d-j-k}}.
 \tag{10}
\]
The exact factorization, including its zeros, is
\[
 \boxed{\qquad
 A_{ijk}=\kappa^2N(-q)^{i+j+k}g_{ij}g_{ik}g_{jk}.
 \qquad}
 \tag{11}
\]
All sine factors in a nonzero entry are strictly positive. Their
complex carriers in (7)--(11) are part of the source.

We prove these formulas by a finite summation in the original
algebra, rather than by interpolation at Casimir values.

### A cleared finite summation

Temporarily let \(p\) be an indeterminate and write
\((a;p)_r=\prod_{t=0}^{r-1}(1-ap^t)\).
The finite identity needed is
\[
 \sum_{r=0}^n
 \frac{(p^{-n};p)_r(b;p)_r p^r}
      {(p;p)_r(c;p)_r}
       =\frac{\prod_{t=0}^{n-1}(b-cp^t)}{(c;p)_n}.
 \tag{12}
\]
Here is an elementary proof. After multiplication by \((c;p)_n\),
the left side is a monic polynomial of degree \(n\) in \(b\).
Only its \(r=n\) term contributes to the leading coefficient;
\[
 (p^{-n};p)_n=(-1)^np^{-n(n+1)/2}(p;p)_n
\]
makes that coefficient one. At \(b=cp^m\), \(0\le m<n\), the
ratio \((b;p)_r/(c;p)_r=(cp^r;p)_m/(c;p)_m\) is a polynomial
of degree \(m\) in \(p^r\). Each of its monomials has zero sum,
because for \(0\le a\le m<n\),
\[
 \sum_{r=0}^n\frac{(p^{-n};p)_r}{(p;p)_r}p^{(a+1)r}
                    =(p^{a+1-n};p)_n=0.
 \tag{13}
\]
The finite product expansion giving the first equality follows by
induction on \(n\), multiplying by the next factor; its coefficient
recurrence is the finite binomial recurrence. Thus the monic polynomial
has precisely the \(n\) stated roots for generic \(c,p\), proving
(12). Clearing its remaining denominators gives the identity at
all specializations where that cleared identity is evaluated.

Substitute \(n=i\), \(b=p^{-j}\), \(c=p^{-(i+j+k)}\) in (12).
Express every shifted factorial by ordinary finite factorials and
clear denominators before specializing \(p=Q\). The result is
\[
 \sum_{r=0}^{\min(i,j)}
 (-1)^r Q^{r(r+1)/2+rk}
 \frac{F_{i+j+k-r}}{F_{i-r}F_{j-r}F_r}
       =\frac{F_{i+k}F_{j+k}}{F_iF_jF_k}.
 \tag{14}
\]
For example the conversion uses
\[
 (p^{-j};p)_r=(-1)^r p^{-jr+r(r-1)/2}
                    \frac{(p;p)_j}{(p;p)_{j-r}}.
 \]
For \(0\le i,j,k<N\), every denominator in (14) has index below
\(N\). Numerators with index at least \(N\) are zero at the root.
This is why (14) specializes without a hidden \(F_N\) division.

### Applying the summation to the source

The root identities
\[
 F_r=(-i)^rq^{r(r+1)/2}S_r,\qquad
 S_rS_{d-r}=N,\qquad (-q)^d=\kappa^{-2}
 \tag{15}
\]
follow directly from the factors in (2); \(F_d=N\).
Set \(a_N=\kappa^{-1}/\sqrt N\), \(t=(-q)^{-1}\). Equation (4)
and the original bilinear duality give
\[
 \Lambda(e_\ell):=\phi(ue_\ell)
       =\frac{\kappa}{\sqrt N}(-q)^{d-\ell}
       =a_Nt^\ell.
 \tag{16}
\]

For \(i+j\le d\), put \(\ell=i+j-r\) in (6).
Using (15), its coefficient becomes
\[
 [e_\ell](e_ie_j)=
 q^{-2ij+r^2}
 \frac{F_{i+j}F_\ell}
      {F_iF_jF_{i-r}F_{j-r}F_r},
 \qquad 0\le r\le\min(i,j).
 \tag{17}
\]
Apply \(\Lambda\) and then (14) with \(k=0\). This gives
\[
 g_{ij}=a_Nt^{i+j}Q^{-ij}\frac{F_{i+j}}{F_iF_j}
                                      \quad(i+j\le d).
 \tag{18}
\]
For \(i+j\ge N\), (6) already gives zero. Substitution of (15)
in (18) proves (7).

Next pair the expansion (17) with \(e_k\) using (18).
If \(\ell+k\ge N\), that summand is zero by (6), exactly as
its numerator \(F_{\ell+k}\) in (14) is zero. Extracting the
common factor from the other summands leaves the left side of
(14). Consequently
\[
 A_{ijk}=
 a_Nt^{i+j+k}Q^{-(ij+ik+jk)}
 \frac{F_{i+j}F_{i+k}F_{j+k}}{F_i^2F_j^2F_k^2}.
 \tag{19}
\]
When a pair sum is at least \(N\), the original pair product is
zero, and so is the numerator in (19). Otherwise converting (19)
by (15) proves (9). Complementing the sine factorials proves
(10). Multiplying the three instances of (7), with the displayed
carrier in (11), proves the factorization.

Finally \(g=J_eM_u\), where \(M_u\) is multiplication by \(u\).
As \(v=N u^\sharp\) and the Newton basis is real,
\[
 h=M_vJ_e=N J_e\overline gJ_e.
 \tag{20}
\]
This proves invertibility on the full algebra. Substitution of
(7) in (20), using
\(\kappa^2q^{d^2+2d}=1\), gives precisely (8).
It does not use a positive or a diagonal spectral measure.

## 3. Exact turns, boundary vectors, and tree contraction

For coefficient columns \(x,y\), let
\[
 A(x,y)_i=\sum_{a,b}A_{abi}x_ay_b.
 \]
If \(z\) is the original coefficient column of the product \(xy\),
then \(A(x,y)=gz\), by (5). Thus the original multiplication is
\[
                         z=hA(x,y).
 \tag{21}
\]
This determines the edge conventions.

Orient a literal expression tree from its leaves to its output.
Between successive multiplication vertices retain the actual
ordered unary word \(T\). The matrix on that internal edge is
\[
                             K_T=Th,
 \tag{22}
\]
with the parent input index first and child output index second.
For an empty unary word it is \(h\). A genuine turn gives \(J_eh\);
its entries are
\[
 (J_eh)_{ij}=
 \frac{\kappa^{-1}}{\sqrt N}
 (-q)^{-j}q^{-ij}\frac{S_{d-i}S_j}{S_{j-i}}
 \quad(i\le j),
 \qquad (J_eh)_{ij}=0\quad(i>j).
 \tag{23}
\]
The opposite orientation uses its transpose \(hJ_e\), with the
opposite triangular support. In particular \(J_eh\) is not
silently replaced by \(hJ_e\).

All unary words can themselves be compiled using the explicit
pair metrics:
\[
 M_{R^+}=\sqrt N\,J_eg,\qquad
 M_{R^-}=N^{-1/2}hJ_e.
 \tag{24}
\]
For example \(M_{R^+}h=\sqrt N\,J_e\) and
\((J_eM_{R^+})h=\sqrt N\,I\), in these Newton conventions.
These are ordered identities, not permission to move turns
through products.

An original leaf with coefficient column \(b\), followed by a
unary corridor \(T\) before its first multiplication, contributes
the column \(Tb\). The elementary columns are
\[
 1=e_0,\qquad
 (R^+)_i=\kappa(-q)^i,\qquad
 (R^-)_i=\kappa^{-1}(-q)^{-i}.
 \tag{25}
\]
An integer power may be kept as the indicated unary product of
(24), or expanded into its literal signed unit factors. No new
independent filling variable is introduced by such an expansion.

If the original closing row is \(\ell\), and \(T_0\) is the
ordered corridor from the last multiplication to that closing,
the root factor is the row
\[
                              \ell T_0h.
 \tag{26}
\]
Without a root corridor, the two original closings become
\[
 \begin{split}
 (\phi h)_i&=\sqrt N\,\kappa^{-1}(-q)^{-i}=v_i,\\
 (mh)_i&=\sqrt N\,\kappa^{-1}\delta_{i,d}.
 \end{split}
 \tag{27}
\]
Indeed \(\phi\) is the row selecting \(e_d\), \(m\) selects
\(e_0\), and (8) gives (27) directly. Any prescribed exterior
scalar remains as the same exterior scalar.

Use \(A\) at each multiplication, (22) on each internal edge,
and the stated leaf and root factors. Induction using (21)
proves that their finite index contraction is exactly the
original scalar. For an open output, retain \(hA(x,y)\) and its
root corridor as the full output column instead of closing it.
If the expression contains no multiplication at all, its value
is simply \(\ell Tb\); no extra \(h\) is inserted. These
conventions include a unit leaf and arbitrary leaf corridors.

Replacing each \(A\) by (11) now gives a literal pairwise state sum.
Each trivalent vertex supplies its three \(g\) factors and its
known one-body carrier; each internal edge supplies (8), (23),
or the ordered products in (22)--(24), expanded with their actual
intermediate indices. Every such index still ranges over all
\(0,\ldots,d\). Supports and sine magnitudes are explicit, and
all nonconstant phases are quadratic or linear in the labels.
There is no remaining three-index weight to be determined.

## 4. Exact coherent interpolation of the Gamma grid

For completeness, this tensor also identifies the complete
canonical Gamma-grid datum of the crossing kernel. Let
\[
 U_x=\sum_{a=0}^d x^af_a,\qquad
 f_a=N^{-1/2}\sum_{r=0}^d
 e^{2\pi i(a-d/2)(r-d/2)/N}e_r.
 \tag{28}
\]
This is the full centered basis of [C]. Its transformation is
unitary for the positive coefficient norm, and
\(\phi(f_af_b)=\delta_{ab}\).
Define
\[
 x_i=-q^{-1}Q^{-i},\qquad
 w_i=\kappa\sqrt N(-q)^i,\qquad 0\le i\le d.
 \]
The finite geometric sum in (28) proves
\[
                              U_{x_i}=w_i e_i.
 \tag{29}
\]
This is a basis identity in \(\mathcal H_N\), not evaluation of
its elements at the repeated Casimir nodes.

Let \(\mathfrak F_N\) be the canonical factorial of [G]. Its
finite normalization and quasiperiod are
\[
 \mathfrak F_N(r)=F_r\quad(0\le r\le d),\qquad
 \mathfrak F_N(z+N)=(1-e^{2\pi iz})\mathfrak F_N(z).
 \tag{30}
\]
The exact canonical section for angles \(a,b,c\) is
\[
 \Gamma_N(a,b,c)=\frac{\kappa^2}{N^2}
 \frac{\prod_{t\in\{a,b,c\}}
          \mathfrak F_N(N(1-t)-1/2)^2}
      {\prod_{\{t,t'\}}\mathfrak F_N(N(1-t-t'))}.
 \tag{31}
\]
The products count labelled singles and pairs. At
\(a_i=(i+1/2)/N\), its single arguments are \(d-i\) and its
pair arguments are \(d-i-j\). Therefore on pair support
\[
 \Gamma^{\rm grid}_{ijk}:=\Gamma_N(a_i,a_j,a_k)
 =\frac{\kappa^2}{N^2}
 \frac{F_{d-i}^2F_{d-j}^2F_{d-k}^2}
      {F_{d-i-j}F_{d-i-k}F_{d-j-k}}.
 \tag{32}
\]
Outside that support at least one pair argument is \(-m\),
\(1\le m\le d\). By (30), \(\mathfrak F_N\) has a simple
pole there, since \(\mathfrak F_N(N-m)\ne0\). All numerator
arguments are still in \(0,\ldots,d\). Thus the quotient has
value zero, with no zero-over-zero prescription.

Using (15), formula (10) is equivalently
\[
 A_{ijk}=
 \frac{\kappa^{-1}(-q)^{-i-j-k}}{N^{7/2}}
 \frac{F_{d-i}^2F_{d-j}^2F_{d-k}^2}
      {F_{d-i-j}F_{d-i-k}F_{d-j-k}}
 \tag{33}
\]
on support. Equations (29), (32), and (33) prove the exact identity
\[
 \phi(f_0U_{x_i}U_{x_j}U_{x_k})=\Gamma^{\rm grid}_{ijk}
 \tag{34}
\]
for all triples, including the support zeros.

There is an explicit global polynomial reconstruction. Put
\[
 D_N(x)=1-(-1)^dx^N,\qquad
 L_i(x)=\frac1N\sum_{a=0}^d(x/x_i)^a
       =\frac{D_N(x)}{N(1-x/x_i)}.
 \tag{35}
\]
The quotient in (35) is the displayed polynomial, including at
\(x=x_i\); \(x_i^N=(-1)^d\) and \(L_i(x_j)=\delta_{ij}\).
Since the original crossing kernel is separately of degree
at most \(d\), its exact presentation is
\[
 \boxed{\quad
 \phi(f_0U_xU_yU_z)=
 \sum_{i,j,k=0}^d
       \Gamma^{\rm grid}_{ijk}L_i(x)L_j(y)L_k(z).
 \quad}
 \tag{36}
\]
Every datum on the right is the explicit factorial expression
(32), with its specified zero support. No unknown source value
has been fitted.

Equation (36) does not assert equality of the polynomial source
to the meromorphic function (31) away from the grid. The latter
has its own cyclic norm and affine source extension [G].
Interpolation retains precisely the whole polynomial source,
including the information that cannot be discarded by selecting
only a local homogeneous Gamma solution.

## 5. A true Fourier dilation with one-variable weights

The pairwise sum has a further exact form in which every factorial
magnitude belongs to a single variable. The remaining couplings
are affine constraints in a cyclic group, with a unitary Fourier
transform. This is a dilation of the same scalar, rather than a
replacement by the squared norm of its coefficients.

Put \(m=2N\), \(\mathsf G=\mathbb Z/m\mathbb Z\); the existing
\(q\) is a primitive \(m\)-th root. Extend all sequences below by
zero from \(\{0,\ldots,d\}\) to \(\mathsf G\). On that window define
\[
 \begin{split}
 \alpha_i&=(-q)^{-i},&
 X_i&=\alpha_iq^{i^2/2}S_{d-i},&
 Y_a&=q^{-(d-a)^2/2}/S_a,\\
 V_i&=q^{-i^2/2}S_i,&
 W_b&=q^{(d+b)^2/2}/S_b,&
 a_i&=\alpha_iq^{i^2}S_{d-i}^2.
 \end{split}
 \tag{37}
\]
All half-integer powers retain convention (1). Let
\(\delta_{\mathsf G}\) denote the indicator of zero in \(\mathsf G\).
The exact resolutions are
\[
 \begin{split}
 g_{ij}
 &=\kappa^{-1}N^{-3/2}X_iX_j
      \sum_{a\in\mathsf G}Y_a
                \delta_{\mathsf G}(i+j+a-d),\\
 h_{ij}
 &=\kappa^{-1}N^{-1/2}V_iV_j
      \sum_{b\in\mathsf G}W_b
                \delta_{\mathsf G}(i+j-b-d).
 \end{split}
 \tag{38}
\]
There is also a direct resolution of a vertex:
\[
 \begin{split}
 A_{ijk}={}&\kappa^{-1}N^{-7/2}a_i a_j a_k
  \sum_{a,b,c\in\mathsf G}Y_aY_bY_c\\
 &\ \cdot\delta_{\mathsf G}(i+j+a-d)
       \delta_{\mathsf G}(i+k+b-d)
       \delta_{\mathsf G}(j+k+c-d).
 \end{split}
 \tag{39}
\]
Here all physical and added charge variables carry their zero-padded
window factors.

There is no alias in these constraints. In the first line of (38),
\(i+j+a\) lies in \([0,3d]\), which contains only the representative
\(d\) of its congruence class modulo \(2N\). In the second line,
\(i+j-b\in[-d,2d]\) likewise contains only that representative.
Thus the first sum sets \(a=d-i-j\) exactly on the support of \(g\),
and the second sets \(b=i+j-d\) exactly on the support of \(h\).
For these values,
\[
 \frac{i^2+j^2-(d-a)^2}{2}=-ij,\qquad
 \frac{-i^2-j^2+(d+b)^2}{2}=ij.
 \tag{40}
\]
These identities and the complementary form of (7) prove (38).
Applying the three first constraints to (39) gives the phase
\[
 i^2+j^2+k^2
 -\tfrac12\bigl((i+j)^2+(i+k)^2+(j+k)^2\bigr)
                         =-ij-ik-jk,
 \]
which proves (39) by (10). All its one-variable magnitudes are
positive factorial weights on their allowed window.

For clarity, use the Fourier convention
\[
 (\mathcal F_m w)(\xi)
       =m^{-1/2}\sum_{x\in\mathsf G}q^{\xi x}w(x).
 \tag{41}
\]
The finite geometric sum proves that \(\mathcal F_m\) is unitary.
The diagonal chirps in (37) are also unitary before multiplication
by their stated magnitudes. They are \(2N\)-periodic for both
parities: for example
\[
 q^{(x+2N)^2/2}/q^{x^2/2}
                   =e^{2\pi ix+2\pi iN}=1.
 \]
The affine reversal \(J_{\mathsf G}:x\mapsto d-x\) is a unitary
permutation and preserves the physical window. Other affine
permutations used on charge variables keep their translated
window factors.

The normalization of a constraint can be expressed by a fixed
copy map. Let \(\Delta e_\xi=e_\xi\otimes e_\xi\), an isometry.
Then
\[
 \mathcal C_+
    =\mathcal F_m^*\Delta^*(\mathcal F_m\otimes\mathcal F_m),
 \qquad
 (\mathcal C_+)_{z;x,y}
       =m^{-1/2}\delta_{\mathsf G}(x+y-z),\qquad
 \mathcal C_+\mathcal C_+^*=I.
 \tag{42}
\]
Indeed its matrix entry is
\(m^{-3/2}\sum_\xi q^{\xi(x+y-z)}\).
For example the first constraint of (38) equals
\(\sqrt m\,(\mathcal C_+)_{d-a;i,j}\).
Thus the normalized addition and copy operations have no
unrecorded large-level norm factor.

There is a useful global statement of all these constants.
After substituting (38) or (39), expanding the unary words, and
collecting factors at each variable, the original scalar has the form
\[
 Z_N=C_N
  \sum_{x\in\mathsf G^{\,v}}
    \prod_{\ell=1}^v w_\ell(x_\ell)
    \prod_{\nu=1}^f
       \delta_{\mathsf G}((Bx)_\nu-\beta_\nu).
 \tag{43}
\]
Here \(B\) and the affine vector \(\beta\) record the literal
constraints, \(C_N\) retains all displayed powers and original
source scalars, and each \(w_\ell\) is a known one-variable
factorial weight times a diagonal phase, with its window.
Original leaf and closing factors from (25)--(27) are included;
Kronecker boundary conditions can remain among these weights.
The numbers \(v,f\) count the actual expanded variables and
constraints. No independence or rank assumption on \(B\) is needed.

Use
\(\delta_{\mathsf G}(y)=m^{-1}\sum_\xi q^{\xi y}\)
for each constraint in (43) and sum the variables separately.
The exact Fourier presentation is
\[
 \boxed{\quad
 Z_N=C_Nm^{v/2-f}
       \sum_{\xi\in\mathsf G^{\,f}}
          q^{-\langle\beta,\xi\rangle}
          \prod_{\ell=1}^v
             (\mathcal F_m w_\ell)((B^t\xi)_\ell).
 \quad}
 \tag{44}
\]
Each variable sum supplies \(\sqrt m\), and each constraint
supplies \(m^{-1}\); these give the stated power.

Finally let \(E:\mathbb C^N\to\mathbb C^{2N}\) extend a physical
column by zero. Then
\(\mathcal F_mE\) is an isometry and
\(E^*\mathcal F_m^*\mathcal F_mE=I_N\).
The projection \(EE^*\) onto the physical window remains part of
every corresponding reconstruction. Enlarging the space does
not allow its deletion, removal of a boundary condition, or
replacement of the original scalar by a positive norm.
Equations (38)--(44) exhibit an exact unitary Fourier organization
of the source; growth and cancellation in its one-variable
weights and final contraction still require analysis.

## 6. Scope and complete sources

The construction is uniform over the literal tree grammar generated
by the original multiplication, genuine turns, signed crossing
powers, units, and original closing rows. It keeps their prescribed
order and all \(N\) coordinates. Both parities and composite levels
are included because only the primitive root \(Q\) and factorial
indices below \(N\) occur in denominators.

The finite identity (12) is the second terminating
\(q\)-Chu--Vandermonde sum, as named in
[NIST DLMF, equation 17.6.3](https://dlmf.nist.gov/17.6.E3).
That reference is coverage only; its proof and the cleared root
specialization used here were given above.
Exact finite Fourier contraction with sine magnitudes
and quadratic phases already appears for mixed three- and
four-crossing words in the earlier
[mixed-wire calculation](research_mixed_wire_exact_contraction.md).
That complete note was read for coverage at
f3147da81f7abfb60aa0b6e4ae3cfce1868b4772b168b8a73b3fc98f2a71a81b.
No proof from it is imported. The complete centered compiler
already provides arbitrary literal finite source compilation.
Here the additional identification is the factorized weighted
vertex, its explicit inverse and turn edges, and the complete
Gamma-grid interpolation for that same source.

No novelty is claimed for finite summation, changing a Frobenius
functional by a unit, or Fourier dilation as general methods.
The pairwise presentation is not a nonnegative integrand or a
positive replacement invariant. Its oscillation, allowed index
regions, endpoint rows, and possible scalar cancellations remain.
It proves no geometric saddle selection, assembled lower bound,
or finite-exception theorem.

The complete proof sources used are:

| Label | Complete source | SHA-256 |
|---|---|---|
| C | [Full centered Conway compiler, 405 lines](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| G | [Exact canonical Gamma source, 632 lines](research_crossing_exact_gamma_source_extension.md) | f19221b384ae9c2de47beee8460df4eee30f3419df6cf0478c18569b3f464495 |

Both entire matching sources were read. The finite-algebra proof
through (27) uses [C]; [G] supplies the specified canonical
factorial and section in (30)--(31). Only written mathematics
and text operations were used. No mathematical programs,
numerical experiments, tests, builds, git operations, or
earlier-final edits were performed.
