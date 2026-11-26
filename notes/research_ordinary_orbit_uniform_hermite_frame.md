# A uniformly stable ordinary-orbit Hermite frame

Private written proof, 17 November 2026.

The complete root can be omitted from a uniformly stable Hermite
sampling frame for every Laurent polynomial in the actual fixed-source
degree window. Its complete value has an explicit recovery row of
bounded Euclidean norm. For the original knot source, the sampled
normals are fixed finite differences of genuine quantum-normal jets
in ordinary color classes. Their squared norm is a positive energy
uniformly comparable to the full Laurent coefficient norm.

This proves neither exponential growth of that energy nor a lower
bound for its selected complex recovery row.

## 1. The sampling theorem

Fix an integer \(A\ge1\), set \(H=4A+1\), and let \(N\ge2\). Write
\[
 \zeta_l=e^{2\pi i l/N},\qquad
 \mathscr E_N=N^{-1}Y\partial_Y,\qquad
 f(Y)=\sum_{k=-AN}^{AN}a_kY^k .
 \tag{1}
\]
All norms below are the usual Hermitian Euclidean norms. Put
\[
 y_l=\bigl((\mathscr E_N^h f)(\zeta_l)\bigr)_{h=0}^{H-1}
       \in\mathbb C^H,\qquad
 \mathcal E_N(f)=\sum_{l=1}^{N-1}\|y_l\|^2 .
 \tag{2}
\]

**Theorem 1.** There are constants \(c_A,C_A>0\), independent of
\(N\) and \(f\), such that
\[
 c_A N\sum_k|a_k|^2
 \le \mathcal E_N(f)
 \le C_A N\sum_k|a_k|^2 .
 \tag{3}
\]
There is an explicit row, depending only on \(A,N\), that recovers
\(f(1)\) from the vectors \(y_l\), \(l\ne0\), with Euclidean norm
bounded independently of \(N\). The minimum norm of any such recovery
row is bounded above and below by positive constants depending only
on \(A\).

The statement includes the full indicated Laurent space, all its
central aliases, every level parity, and \(N=2\).

### Fourier alias spaces

For \(0\le r<N\) let
\[
 I_r=\{k\in[-AN,AN]\cap\mathbb Z:k\equiv r\pmod N\},\qquad
 v(\lambda)=(1,\lambda,\ldots,\lambda^{H-1})^{\mathsf t},
\]
and let \(V_r\) have columns \(v(k/N)\), \(k\in I_r\).
Write \(a_r=(a_k)_{k\in I_r}\) and \(b_r=V_ra_r\).
Then
\[
 y_l=\sum_{r=0}^{N-1}\zeta_l^r b_r,\qquad
 \sum_{l=0}^{N-1}\|y_l\|^2=N\sum_r\|b_r\|^2 .
 \tag{4}
\]
The second equality follows by summing the finite geometric series
\(\sum_l\zeta_l^{r-s}=N\delta_{rs}\).

The nodes for \(r=0\) are \(-A,\ldots,A\). For \(r>0\), they are
\[
 \theta-A,\ldots,\theta+A-1,\qquad \theta=r/N.
 \tag{5}
\]
There are constants \(\mu_A,\Lambda_A>0\) such that
\[
 \mu_A\|a_r\|^2\le\|V_ra_r\|^2\le\Lambda_A\|a_r\|^2
 \tag{6}
\]
for every \(r,N\). Indeed the matrices with all \(2A+1\) columns
\(v(\theta+j)\), \(-A\le j\le A\), have full column rank for
\(0\le\theta\le1\). Their first \(2A+1\) rows form a Vandermonde
matrix with nonzero determinant
\(\prod_{-A\le i<j\le A}(j-i)\).
Continuity on this compact interval gives a positive minimum
singular value and a finite maximum. The matrices in (5) are
column submatrices, and \(V_0\) is the endpoint matrix.
This proves (6) without a level-dependent interpolation estimate.

Let \(U_r=\operatorname{im}V_r\), and define its orthogonal projector
and their average by
\[
 Q_r=V_r(V_r^*V_r)^{-1}V_r^*,\qquad
 P_N=\frac1N\sum_{r=0}^{N-1}Q_r .
 \tag{7}
\]

### A uniform gap after deleting one node

We prove that there is \(\gamma_A>0\) such that
\[
                         \|P_N\|\le1-\gamma_A
                         \quad(N\ge2).
 \tag{8}
\]
For \(0\le\theta\le1/2\), \(1/3\le d\le1/2\), consider the two
spaces spanned respectively by
\[
 \{v(\theta+j):-A\le j\le A\},\qquad
 \{v(\theta+d+j):-A\le j\le A-1\}.
 \tag{9}
\]
Together these are \(H\) columns with distinct nodes. Nodes within
one list differ by nonzero integers; nodes in different lists
differ by an integer plus \(d\), so cannot coincide.
The square Vandermonde matrix is invertible throughout the compact
rectangle of \((\theta,d)\). Consequently the two spaces have zero
intersection and a uniformly bounded angle: there is
\(\varepsilon_A>0\) such that
\[
 |\langle u,v\rangle|\le(1-\varepsilon_A)\|u\|\|v\|
 \tag{10}
\]
when \(u,v\) belong to the respective spaces.

Here is an elementary justification of the uniform assertion.
The least singular value of the combined matrix has a positive
compact minimum \(s_A\), and the norms of its two column blocks
have a common finite bound \(L_A\). For unit vectors \(u,v\),
their coefficient vectors have squared norms summing to at least
\(2/L_A^2\). Applying the least singular value bound to
\(u-e^{i\alpha}v\), with its phase chosen to maximize the inner
product, gives (10) with
\(\varepsilon_A=s_A^2/L_A^2>0\).

For the projectors \(Q,Q'\) onto any subspaces of these two spaces,
\[
                         Q+Q'\le(2-\varepsilon_A)I .
 \tag{11}
\]
To check this directly, set \(p=Qz,q=Q'z\) and
\(S=\|p\|^2+\|q\|^2=\langle z,p+q\rangle\). Equation (10) gives
\(\|p+q\|^2\le(2-\varepsilon_A)S\); Cauchy--Schwarz gives
\(S\le(2-\varepsilon_A)\|z\|^2\).

Set \(m=\lfloor N/2\rfloor\). Pair residues \(r\) and \(r+m\)
for \(0\le r<m\). Their separation \(d=m/N\) belongs to
\([1/3,1/2]\) for every \(N\ge2\), including \(N=2\).
Their actual spaces are subspaces of (9) with \(\theta=r/N\).
This includes the extra column of \(U_0\).
For odd \(N\) there is one unpaired residue, whose projector is
bounded by \(I\). Summing (11) gives
\[
 P_N\le\left(1-\frac mN\varepsilon_A\right)I
       \le(1-\varepsilon_A/3)I .
 \tag{12}
\]
This proves (8), with \(\gamma_A=\varepsilon_A/3\).

The sum map \(\mathcal S:\bigoplus_r U_r\to\mathbb C^H\),
\(\mathcal S(b_r)=\sum_rb_r\), satisfies
\(\mathcal S\mathcal S^*=\sum_rQ_r=NP_N\). Hence
\[
 \left\|\sum_rb_r\right\|^2
     \le N(1-\gamma_A)\sum_r\|b_r\|^2 .
 \tag{13}
\]
Subtracting the \(l=0\) term in (4) and using (6) proves (3),
for example with \(c_A=\gamma_A\mu_A\) and
\(C_A=\Lambda_A\). Thus deletion of the complete node has been
paid uniformly, rather than estimated from its unknown value.

## 2. An explicit fixed-size recovery matrix

For \(1\le l<N\) define
\[
 A_{l,N}=\frac1N\sum_{r=0}^{N-1}\zeta_l^{-r}Q_r,\qquad
 L_{l,N}=(I-P_N)^{-1}A_{l,N}.
 \tag{14}
\]
These are \(H\)-by-\(H\) matrices; their definition involves no
source coefficients. Fourier inversion in (4) gives
\[
 b_r=\frac1N y_0+
                \frac1N\sum_{l=1}^{N-1}\zeta_l^{-r}y_l .
 \tag{15}
\]
Applying \(Q_r\), summing in \(r\), and using \(\sum_rb_r=y_0\)
proves the exact missing-jet identity
\[
                    y_0=\sum_{l=1}^{N-1}L_{l,N}y_l .
 \tag{16}
\]
In particular, with \(e_0=(1,0,\ldots,0)^{\mathsf t}\),
\[
                    f(1)=\sum_{l=1}^{N-1}e_0^*L_{l,N}y_l .
 \tag{17}
\]
Every missing normal through order \(H-1\) is also recovered by
(16); no missing-node normal is input.

The row norm has an exact finite formula. Put \(A_{0,N}=P_N\).
Fourier orthogonality and \(Q_r^2=Q_r\) give
\[
 \sum_{l=0}^{N-1}A_{l,N}A_{l,N}^*=P_N,\qquad
 \sum_{l=1}^{N-1}L_{l,N}L_{l,N}^*
                         =P_N(I-P_N)^{-1}.
 \tag{18}
\]
Thus the squared Euclidean norm of the row in (17) is
\[
 e_0^*P_N(I-P_N)^{-1}e_0
                          \le\gamma_A^{-1}-1 .
 \tag{19}
\]
This is a bounded recovery row for the actual complex value;
its coefficients need not be positive.

For completeness, its minimum possible norm has a uniform positive
lower bound too. Test any exact recovery row on
\(S_N(Y)=1+\cdots+Y^{N-1}\), which belongs to (1).
One has \(S_N(1)=N\), \(\sum|[Y^k]S_N|^2=N\), and by (3)
\(\mathcal E_N(S_N)\le C_A N^2\).
Cauchy--Schwarz therefore forces the row norm to be at least
\(C_A^{-1/2}\). This is a norm test on the sampling space, not an
assertion that this test polynomial is a knot invariant.
Together with (19) it proves the last statement of Theorem 1.

## 3. The actual quantum-normal source energy

The sole proof direct [R] fixes the original reduced, zero-framed
knot source. For a fixed braid of length \(\ell\), strand number
\(b\), writhe \(w\), and \(c=b-1-w\), it proves
\[
 F_N(M)=f_N(M^2),\qquad K_N=f_N(1),\qquad
 \operatorname{supp}f_N\subset[-AN,AN],
 \quad
 A=\max\left(1,\left\lceil(3\ell+|c|)/2\right\rceil\right).
 \tag{20}
\]
This is the actual finite-head width, including the retained
\(x^{-(N-1)c}\) pivot/framing adapter. No change of closing or
normalization is made here.

Let \(\Delta\) be the symmetric Alexander polynomial with
\(\Delta(1)=1\), and define the fixed numbers
\[
 \alpha_s=\left.(Z\partial_Z)^s\Delta(Z)\right|_{Z=1}.
 \tag{21}
\]
The root-normal coordinate and genuine finite-color jets are
\[
 q(\delta)=e^{\pi i/N}(1-\delta)^{1/(2N)},\qquad
 J_{h,l,N}(r)=[\delta^h]C_{l+rN}(q(\delta)).
 \tag{22}
\]
Here \(1\le l<N\), \(0\le r\le h<H\), and \(C_j\) is the original
reduced zero-framed color with unknot value one.

Use the following combinations, rather than the vector of all
raw jets in (22):
\[
 B_{h,l,N}
     =N^{-h}\sum_{r=0}^h(-1)^r\binom hr J_{h,l,N}(r).
 \tag{23}
\]
The exact same-source finite-difference adapter of [R, (18)] is
\[
 B_{h,l,N}
  =\left.
       N^{-h}(Y\partial_Y)^h
          \left(\frac{f_N(Y)}{\Delta(Y^N)}\right)
    \right|_{Y=\zeta_l}.
 \tag{24}
\]
In particular, these are ordinary-node meridian derivatives of the
actual source divided by its entire Alexander factor. They are not
obtained by identifying fixed-meridian and integral-color normal
paths. Their equality follows from the genuine shifted integral-color
restriction and its \(h\)-th finite difference, as proved in [R].

Let \(B_{l,N}=(B_{h,l,N})_{h=0}^{H-1}\), and define the fixed
triangular matrix
\[
 (\mathcal D_\Delta)_{ah}
  =\begin{cases}
     \binom ah\alpha_{a-h},&0\le h\le a<H,\\
     0,&h>a.
    \end{cases}
 \tag{25}
\]
It has diagonal entries one and is independent of \(N,l\).
The full Alexander Leibniz identity of [R, (19)] is exactly
\[
                            y_l=\mathcal D_\Delta B_{l,N}.
 \tag{26}
\]
Both \(\mathcal D_\Delta\) and its inverse have fixed finite norms.
Therefore Theorem 1 proves the positive actual-source estimate
\[
 c_{A,\Delta}N\sum_k|[Y^k]f_N|^2
 \le
 \mathcal Q_N:=\sum_{l=1}^{N-1}\sum_{h=0}^{H-1}|B_{h,l,N}|^2
 \le
 C_{A,\Delta}N\sum_k|[Y^k]f_N|^2 .
 \tag{27}
\]
For example, one can take
\(c_{A,\Delta}=c_A/\|\mathcal D_\Delta\|^2\) and
\(C_{A,\Delta}=C_A\|\mathcal D_\Delta^{-1}\|^2\).
This energy uses no color divisible by \(N\): every color in
(23) lies between \(1\) and \(HN-1\) in an ordinary residue class.
It does use genuine high colors when \(r>0\), and quantum normals
when \(h>0\).

The exact complete recovery is now
\[
 K_N=\sum_{l=1}^{N-1}
                  e_0^*L_{l,N}\mathcal D_\Delta B_{l,N}.
 \tag{28}
\]
Its row norm is at most
\(\|\mathcal D_\Delta\|\sqrt{\gamma_A^{-1}-1}\).
On the full Laurent sampling space, the minimum exact row norm is
also bounded below independently of \(N\): apply the same test
\(f=S_N\), now using the upper bound in (27).
Thus the minimum dual norm is \(\Theta_{A,\Delta}(1)\).
The row is known without inserting the unknown scalar \(K_N\).

There is no assertion that \(\mathcal Q_N\) is uniformly equivalent
to the squared norm of all the raw quantities (22).
Those contain additional fixed-order terms of the completed period;
(23) is the exact combination that removes them and selects (24).
The finite differences, their signs, and the powers \(N^{-h}\)
are part of the source observation.

## 4. Scope and coverage

The new estimate deletes the complete node from a stable full
Hermite frame. The alias Vandermonde method itself is already in
[the orbit-jet growth note](research_regularized_orbit_jet_growth.md),
Section 2, for full-circle sampling with the complete node retained.
[Bounded meridian jets](bounded_meridian_jets.md) studies singular
recurrence transfer; it does not prove this deleted-node frame.
[The tame source-channel frame](actual_tame_c0_hermite_source_frame.md)
concerns a two-dimensional Casimir channel, rather than the entire
Laurent meridian polynomial. These three coverage texts were read
in full. Their results are not proof premises here.

[R] already supplies the exact omitted-node residue reconstruction,
actual Laurent width, and genuine high-color quantum-normal adapter.
The improvement here is the uniform frame estimate (3), the explicit
bounded row (17), and the positive normal energy (27). No general
novelty is claimed for Hermite interpolation or Fourier frames.

Equation (27) identifies an actual positive energy for the whole
meridian coefficient vector, not for the selected value alone.
Equation (28) gives an upper bound for that value from the energy.
Neither proves that this energy has the geometric exponential rate,
nor that the original vector has a non-exponentially-small component
along the recovery row. The overlap
\[
 \frac{|K_N|}
 {\|\ell_N\|\,
       \bigl(\sum_{l,h}|B_{h,l,N}|^2\bigr)^{1/2}}
 \tag{29}
\]
for the specified row \(\ell_N\) in (28) remains unestimated.
No scalar lower bound, noncancellation, source-cycle identification,
or finite-exception filling theorem follows from uniform sampling.

The sole complete proof direct is:

| Label | Complete source | SHA256 |
|---|---|---|
| R | notes/research_ordinary_orbit_jet_reconstruction.md | 6c9c3089b93204ae6b7045265ece6deac1552563de806dae3810392c239c028d |

The entire direct was read at this matching pin. It supplies only
the actual-source statements explicitly used in Section 3.
The sampling, transversality, reconstruction matrices, and all
conditioning bounds are proved above by written finite-dimensional
arguments. No mathematical programs, numerical cases, tests, or
builds were used. Frozen notes and manuscripts are unchanged.
