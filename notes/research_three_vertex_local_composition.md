# Local composition of the retained three-crossing vertex

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The corner-deleted original vertex has an accretive wire Hessian at
the homogeneous point. Consequently its local packets compose for
every fixed number of vertices. The cyclic local coefficient agrees
exactly with the independently proved full cyclic spectral coefficient.
This gives a bound on the **signed total** complementary cyclic
integral, not on its absolute value. No full open-chain asymptotic or
identification of a cyclic network with a knot is asserted here.

The subsequent [global retained-wire bound](research_three_vertex_global_wire_bound.md)
upgrades this complement to an absolute exponential bound and proves
the full-period retained kernel for fixed homogeneous Fourier endpoints.
It still leaves the actual ordinary-color cap contours separate.

## 1. The exact source and the eliminated Hessian

Use the original matrices and corner deletion from
[the traced-vertex proof](research_traced_three_vertex_endpoint.md),
Sections 7--9:
\[
 A=JM^3,\qquad \widetilde A=A-M^TP_LJM P_LM,
 \quad L=\lfloor N/50\rfloor,\qquad
 \widetilde V_N(x,y)=h(x)^T\widetilde A h(y).
 \tag{1}
\]
All physical values and first normals are already included in this
finite source. Put
\[
 x_*={1\over6}+{i\log2\over2\pi},\quad
 X_*={1+i\sqrt3\over4},\quad
 a_0={2\over3^{1/4}\sqrt{2+i\sqrt3}},\quad
 k_0={4\pi\over21}(2\sqrt3-3i),\quad
 \rho={5-\sqrt{21}\over2}.
 \tag{2}
\]
The square root defining \(a_0\) has positive real part. The cited
fixed-neighborhood theorem proves, with uniform holomorphic normalized
error and its fixed derivatives,
\[
 \widetilde V_N(x,y)=\kappa N^{-1/2}a(x,y)e^{N\Phi(x,y)}
 (1+O(N^{-1})),\qquad
 \Phi(x_*,x_*)=2c,\quad a(x_*,x_*)=a_0\ne0.
 \tag{3}
\]
Here \(c=2\int_0^{5/6}\log(2\sin\pi u)\,du\), and
\(\kappa\) is the original level-dependent unit phase. In particular
(3) is not an assumed interpolation of rowwise asymptotics.

We compute the wire derivatives before composing (3). Set
\(X=e^{2\pi ix},Y=e^{2\pi iy}\). With the continued logarithms
specified in the traced-vertex proof, the index phase is
\[
 \begin{split}
 F(s,t;x,y)={}&\mathcal J(s+t)
  +{i\pi\over2}\{s+t-(s+t)^2\}
  +s\log X+t\log Y-I_X(s)-I_Y(t),\\
 I_X(s)={}&\int_0^s\log(1-Xe^{-2\pi iu})\,du,\\
 \Phi(x,y)={}&F(s_c,t_c;x,y)-\pi i(x+y).
 \end{split}
 \tag{4}
\]
The stationary index pair is \(s_c=t_c=1/3\) at the center.
Writing \(r=\sqrt3\), its derivative blocks are
\[
 F_{(s,t)(s,t)}=-\pi
 \begin{pmatrix}r+i&r^{-1}+i\\r^{-1}+i&r+i\end{pmatrix},
 \quad F_{(s,t)(x,y)}=2\pi(r^{-1}+i)I_2,
 \quad F_{(x,y)(x,y)}=-{4\pi\over r}I_2.
 \tag{5}
\]
For example,
\(F_{sx}=2\pi i/(1-Xe^{-2\pi is})\) and
\(F_{xx}=2\pi i\{X/(1-X)-Xe^{-2\pi is}/(1-Xe^{-2\pi is})\}\).
Also
\[
 \Phi_x=2\pi i s_c+\log(1-Xe^{-2\pi is_c})
                -\log(1-X)-\pi i,
 \qquad \nabla\Phi(x_*,x_*)=0.
 \tag{6}
\]
The last zero is an equality of the chosen logarithms: the two
denominator arguments at the center are \(\pi/6,-\pi/6\),
so the imaginary part is \(2\pi/3+\pi/3-\pi=0\); their
moduli agree. It is not inferred from an exponentiated equation.

Differentiating \(F_s=F_t=0\) gives the Schur complement
\[
 \boxed{\quad
 -\Phi''(x_*,x_*)=k_0
            \begin{pmatrix}5&-2\\-2&5\end{pmatrix},
 \qquad \Re k_0={8\pi\sqrt3\over21}>0,
 \qquad \pi a_0^2=k_0.
 \quad}
 \tag{7}
\]
The real matrix in (7) has eigenvalues 3 and 7. Shrinking a fixed
wire neighborhood therefore makes the real part of the negative
Hessian uniformly positive there. This is a local statement about
the retained vertex; it makes no assertion about the omitted wire
periods.

## 2. Local cyclic composition, including one and two vertices

Choose a sufficiently small fixed \(d>0\), and let
\(I_d=x_*+[-d,d]\), oriented in the increasing real direction.
For fixed \(m\ge1\), define the actual restricted integral
\[
 C^{\rm loc}_{m,N}=N^m\int_{I_d^m}
          \prod_{j=1}^m\widetilde V_N(x_j,x_{j+1})
                   \,dx_1\cdots dx_m,\qquad x_{m+1}=x_1.
 \tag{8}
\]
**Theorem 1.** At both parities, along all sufficiently large levels,
\[
 C^{\rm loc}_{m,N}
 =\kappa^m e^{2mcN}
       {\rho^{m/2}\over1-\rho^m}\{1+O_m(N^{-1})\}.
 \tag{9}
\]

*Proof.* Every wire is stationary at \(x_*\) by (6). Let \(P_m\)
be the cyclic permutation matrix, including \(P_1=(1)\). The
negative Hessian of the sum of phases is
\[
 k_0 C_m,\qquad C_m=10I_m-2(P_m+P_m^T).
 \tag{10}
\]
This convention retains both incidences of a loop when \(m=1\),
giving \(C_1=(6)\). For \(m=2\), the two edges are parallel:
\(C_2=\left(\begin{smallmatrix}10&-4\\-4&10\end{smallmatrix}\right)\).
Thus its eigenvalues are always
\(10-4\cos(2\pi j/m)\), in particular at least 6.
The negative real Hessian is bounded below by \(6\Re k_0\)
at the center. The edgewise neighborhood in (7) gives strict real
concavity throughout a smaller cube, and a strict gap on its boundary.

Insert the uniform exact-source packet (3) in (8). Its Gaussian
coefficient is
\[
 {a_0^m(2\pi)^{m/2}\over k_0^{m/2}\sqrt{\det C_m}}
   ={1\over\sqrt{\det(5I_m-P_m-P_m^T)}}.
 \tag{11}
\]
The Gaussian square root is continued from positive real quadratic
forms. In particular \(\sqrt{k_0}=\sqrt\pi\,a_0\); the
factor \(k_0^{m/2}\) is formed using this one fixed square root,
not a separately chosen principal square root of a large determinant.
The original factors of \(N\) are
\(N^mN^{-m/2}N^{-m/2}=1\).

Since \(\rho+\rho^{-1}=5\), the product over roots of unity gives
\[
 \prod_{j=0}^{m-1}\{5-2\cos(2\pi j/m)\}
       =\rho^{-m}(1-\rho^m)^2.
 \tag{12}
\]
This proves the coefficient in (9). The analytic amplitude and phase
have the usual local Taylor expansion with Gaussian domination.
The term of order \(N^{-1/2}\) is odd, and integration over the
centered cube differs from integration over all real directions by
an exponentially small error. The error is therefore relative
\(O_m(N^{-1})\). This proof uses only the restricted exact integral
(8). \(\square\)

The local coefficient is \(1/\sqrt3\) for \(m=1\) and
\(1/\sqrt{21}\) for \(m=2\), consistent with their special
incidence multiplicities.

## 3. An open chain with fixed Fourier endpoints

Fix \(x_0=x_m=x_*\). The corresponding local open integral is
\[
 O^{\rm loc}_{m,N}=N^{m-1}\int_{I_d^{m-1}}
             \prod_{j=1}^m\widetilde V_N(x_{j-1},x_j)
                          \,dx_1\cdots dx_{m-1}.
 \tag{13}
\]
For \(m=1\) there is no integral. These endpoints are fixed
**Fourier variables**; they are not complete ordinary-color caps.

Let \(B_r\) be the real tridiagonal matrix with diagonal 5 and
adjacent entries \(-1\), and put \(D_r=\det B_r\),
\(D_0=1,D_{-1}=0\). Then
\[
 D_1=5,\qquad D_r=5D_{r-1}-D_{r-2},\qquad
 D_{m-1}={\rho^{-m}-\rho^m\over\sqrt{21}}>0.
 \tag{14}
\]
The internal negative Hessian is \(2k_0B_{m-1}\), whose real
part is positive. The same Gaussian calculation gives
\[
 \boxed{\quad
 O^{\rm loc}_{m,N}
   =\kappa^m N^{-1/2}e^{2mcN}
          {a_0\over\sqrt{D_{m-1}}}\{1+O_m(N^{-1})\}.
 \quad}
 \tag{15}
\]
Indeed the powers are
\(N^{m-1}N^{-m/2}N^{-(m-1)/2}=N^{-1/2}\).

There is also a local holomorphic version for the two Fourier
endpoints near \(x_*\). The internal critical point continues by
the implicit-function theorem. The original finite integrand is
holomorphic, so the small internal contours may be moved through
that point; their connecting boundary pieces keep the local strict
gap. The effective negative endpoint Hessian at the center is
\[
 k_0\begin{pmatrix}
 5-2D_{m-2}/D_{m-1}&-2/D_{m-1}\\
 -2/D_{m-1}&5-2D_{m-2}/D_{m-1}
 \end{pmatrix}.
 \tag{16}
\]
For \(m=1\) the convention \(D_{-1}=0\) gives (7).
For \(m\ge2\), (16) follows by eliminating \(2B_{m-1}\)
from the real path matrix with endpoint diagonal 5, internal diagonal
10, and adjacent entries \(-2\). That matrix is positive definite,
so its Schur complement is positive definite too. The local amplitude
thus remains holomorphic and nonzero. None of these local statements
estimates the full open source outside the indicated wire neighborhood.

## 4. What the independently known full cyclic answer adds

Let \(C^{\rm full}_{m,N}\) and
\(\widetilde C^{\rm full}_{m,N}\) denote the full-period cyclic
integrals of the original and retained vertices, respectively, at
the common height \(\Im x_*\). Exact cardinal averaging gives
\[
 C^{\rm full}_{m,N}=\operatorname{Tr}(A^m),\qquad
 \widetilde C^{\rm full}_{m,N}=\operatorname{Tr}(\widetilde A^m).
 \tag{17}
\]
The original positive similarity and the corner estimate in Section 7
of the traced-vertex note imply
\[
 |\operatorname{Tr}(A^m)-\operatorname{Tr}(\widetilde A^m)|
 \le C_mN^{a_m}e^{N\{2(m-1)c+\sigma\}},
 \qquad \sigma={\log(100e)\over50}<3/25<2c.
 \tag{18}
\]
To see this directly, telescope the difference of powers in the
\(M\)-similarity gauge, use the original bounds
\(\|MAM^{-1}\|\le C e^{2Nc}\) and
\(\|M(A-\widetilde A)M^{-1}\|\le CN^a e^{N\sigma}\),
and then \(|\operatorname{Tr} T|\le N\|T\|\).

The independent
[cyclic spectral theorem](research_positive_three_crossing_cycle.md),
Theorem 2, proves
\[
 C^{\rm full}_{m,N}
 =\kappa^m e^{2mcN}
       \left\{{\rho^{m/2}\over1-\rho^m}+O_m(N^{-1/2})\right\}.
 \tag{19}
\]
Comparing (9), (18), and (19) now yields the exact-source consequence
\[
 \widetilde C^{\rm full}_{m,N}-C^{\rm loc}_{m,N}
           =O_m(N^{-1/2}e^{2mcN}).
 \tag{20}
\]
The left side is the signed total integral over the complement of
the local cube in the full cyclic wire period. This is a polynomial
relative error, not an exponential bound or an estimate of the
integral of the absolute value. Its proof uses the separately proved
positive spectral theorem; it is not a proof that local coercivity
alone controls a global cycle. There is no corresponding open-chain
conclusion here.

## 5. Exact algebra reproduction

Run `python3 experiments/check_three_vertex_local_composition.py`.
The [saved record](../repro/results/research-three-vertex-local-composition.json)
checks the exact derivative blocks, Schur complement, scalar
normalization, cyclic multiplicities, and determinant recurrence. It
records the proof and dependency hashes. It does not computationally
certify the analytic contour estimates or infer asymptotics from finite
levels.
