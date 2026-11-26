# Exact channel transport for the first coideal crossing

24 November 2026. Written research proof.

The first crossing in the actual coideal graph has an explicit finite
transform. It decouples the neighboring total coideal into a one-head
operator, with every original phase retained. Its action between two
independently specified joint Haar metrics is diagonal in the channel
labels, with an explicit positive gain. The weight in that gain is
symmetric and has a uniform two-label ideal-octahedron volume profile.

This gives an exact isometry after specified positive reweightings,
and sharp exponential crossing costs before those reweightings.
The two interface metrics differ. The original closing remains a
prescribed complex row; no word-energy or scalar lower bound follows.

## 1. Actual generators and every external coideal channel

Use the complete balanced physical basis of P and K. Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1}=q^d,\quad \kappa=q^{d^2/2},\quad
 c=1+q,\quad F_a=(Q;Q)_a,\quad F_0=1,\quad F_d=N .
 \tag{1}
\]
The basis is physically orthonormal. Its actual generators are
\[
 Ke_a=xQ^{-a}e_a,\qquad Ee_a=(Q^{-a}-1)e_{a-1},\qquad
 Fe_a=(1-Q^{a+1})e_{a+1}.
\]
The missing endpoint arrows are zero. Retain the ordered coproducts
\(E_{12}=E_1K_2+E_2\), \(F_{12}=F_1+K_1^{-1}F_2\).
On \(r\) heads write
\[
 B_c^{(r)}=\mathsf F-(\mathsf E-cI)\mathsf K^{-1},\qquad
 B_c^{(0)}=c.
\]
C and K prove, on the entire tensor space,
\[
 p_N(B_c^{(r)})=0,\quad
 p_N(z)=2q^{N/2}T_N(z/(2\sqrt q)),\quad
 \mu_j=Q^j+qQ^{-j}\quad(0\le j<N),
 \tag{2}
\]
where \(\sqrt q=e^{\pi i/(2N)}\) and \(T_N\) is Chebyshev.
These roots are distinct. Every root occurs if \(r\ge1\).
Also \(\overline{\mu_j}=q^{-1}\mu_j\), and
\[
 p_N'(\mu_j)=\frac{2NQ^j}{Q^{2j}-q},\qquad |p_N'(\mu_j)|\ge N.
 \tag{3}
\]
No simple-node quotient of a pair Casimir is being taken.

Fix a width \(b\ge2\) and set
\[
 U=V_N^{\otimes(b-2)},\quad W=V_N\otimes U,\quad
 S=B_c^{(b-2)},\quad T=B_c^{(b-1)}
       =(F_2-E_2K_2^{-1})+K_2^{-1}S .
 \tag{4}
\]
For \(b=2\), interpret \(U=\mathbb C\) and \(S=c\).
The operators \(T,S\) commute. Choose any external root
\(\nu\in\{\mu_0,\ldots,\mu_d\}\), not necessarily \(c=\mu_0\).
For scalar arguments define the monic continuants
\[
 D_{-1}=0,\quad D_0=1,\qquad
 D_{a+1}(\lambda;\sigma)
  =(\lambda+qQ^a\sigma)D_a(\lambda;\sigma)
               -q(1-Q^a)^2D_{a-1}(\lambda;\sigma).
 \tag{5}
\]
They also have their commuting operator-coefficient meaning.
The first-head tridiagonal determinant is
\(D_N(\lambda;T)=p_N(\lambda)-(-1)^{N+1}p_N(T)\).
Consequently \(D_N(\nu;T)=0\) at every width. The graph
\[
 L_\nu=\sum_{a=0}^d|a\rangle_1\otimes
                    \frac{q^{-a}D_a(\nu;T)}{F_a}
 \tag{6}
\]
therefore parameterizes the whole kernel
\(\ker(B_c^{(b)}-\nu I)\), with inverse first-coordinate
extraction \(\pi_0L_\nu=I\). This follows by the unit upper-arrow
recurrence, just as in K, without requiring \(\nu=c\).

Every original unmarked signed braid commutes with \(B_c^{(b)}\).
Its graph action is thus \(\pi_0RL_\nu\); these actions preserve
products and inverses. For the first positive crossing put
\[
                         C_\nu=\pi_0R_1^+L_\nu .
 \tag{7}
\]
The source-selected case is \(\nu=c\); write \(R_c=\pi_0RL_c\)
for a whole reduced word. At even width \(b=2k\),
K and G give the original cup, graph input, and full marked row:
\[
 u_0=p^{\otimes k}=L_cz_0,\quad
 z_0=Nx^{-d}|d\rangle_2\otimes p^{\otimes(k-1)},\quad
 \mathcal K_N=\chi_N\ell_0L_c\,R_cz_0 .
 \tag{8}
\]
The external factor \(\chi_N\) and the full row \(\ell_0\) remain.
Other external channels do not replace this original source.

## 2. The literal crossing transform and its neighboring coideal

The full positive crossing in P sends \((a,b)\) to
\((b+n,a-n)\). Output first occupation zero forces \(b=n=0\).
Its surviving coefficient is exactly \(\kappa x^{-a}\).
Substitution of (6), using \(x^{-a}q^{-a}=(-1)^a\), proves
\[
 \boxed{\quad C_\nu
  =\kappa\sum_{a=0}^d(-1)^a|a\rangle_2\otimes
       \left[(\langle0|_2\otimes I_U)
                       \frac{D_a(\nu;T)}{F_a}\right].\quad}
 \tag{9}
\]
No physical shuffle or unrecorded phase was used.
Finite propagation makes this lower triangular in the head-2
occupation. The leading \(T\)-coefficient of \(D_a(\nu;T)\)
is \(q^{a^2}\); a strict downward path in \(T\) has product
\(q^aF_a\). Its diagonal is consequently
\[
                     \kappa(-1)^a q^{a(a+1)}I_U .
 \tag{10}
\]
In particular \(C_\nu\) is invertible. This is its triangular
diagonal, not an assertion that the physical matrix is diagonal.

Let \(\mathcal D e_a=q^{-a}e_a\), and let \(B_\nu^{(1)}\)
mean the actual one-head coideal with auxiliary parameter \(\nu\).
Define on head 2, with identity on \(U\),
\[
 J_\nu'=q\mathcal D\,\overline{B_\nu^{(1)}}\,\mathcal D^{-1}.
 \tag{11}
\]
It has the same \(N\) simple roots \(\mu_j\). Direct rearrangement
of (5) in the rows of (9) gives
\[
 \boxed{\quad C_\nu T=J_\nu'C_\nu,\qquad C_\nu S=SC_\nu.\quad}
 \tag{12}
\]
For explicit verification,
\[
 (J_\nu'v)_a=(1-Q^{-a})v_{a-1}
    +q(1-Q^{-a-1})v_{a+1}-q^{-1}Q^{-a}\nu v_a.
 \tag{13}
\]
The recurrence writes \(TD_a\) as its next and previous
continuants. The factors \((-1)^a/F_a\) give (13);
\(D_{-1}=D_N(\nu;T)=0\) gives both endpoints.
Equation (11) follows because \(\bar\nu=q^{-1}\nu\).
Thus the actual first crossing decouples the total tail \(T\)
into this specified one-head coideal; the deeper \(S\) is unchanged.

## 3. Symmetric positive weights and a finite product

For any two roots put
\[
 h_N(\lambda,\sigma)=\sum_{a=0}^d
                    \left|\frac{D_a(\lambda;\sigma)}{F_a}\right|^2.
 \tag{14}
\]
An exact reciprocity will be useful:
\[
 D_a(\lambda;\sigma)
   =q^{a(a+1)}\overline{D_a(\sigma;\lambda)},\qquad
                 h_N(\lambda,\sigma)=h_N(\sigma,\lambda).
 \tag{15}
\]
It holds whenever \(\bar\lambda=q^{-1}\lambda\) and
\(\bar\sigma=q^{-1}\sigma\). For a direct proof set the
right side of the first identity equal to \(R_a\).
Conjugating (5) and changing its normalization to \(R_{a+1}\)
multiplies the linear coefficient by \(q^{2a+2}\):
\[
 q^{2a+2}(q^{-1}\sigma+q^{-2}Q^{-a}\lambda)
                         =\lambda+qQ^a\sigma.
\]
The previous-term coefficient becomes
\(q^{4a+1}(1-Q^{-a})^2=q(1-Q^a)^2\).
The same recurrence and initial values prove (15) for every \(a\).
Also \(D_a(-\lambda;-\sigma)=(-1)^aD_a(\lambda;\sigma)\).

Write \(\lambda=\mu_j\), \(\sigma=\mu_l\), and \(m=\lfloor N/2\rfloor\).
Set
\[
 A=\begin{cases}[m-j-l]_N,&N\text{ even},\\
                 [m+j-l]_N,&N\text{ odd},\end{cases}
 \qquad B=d-A .
\]
Then the complete coefficient vector has the finite product
\[
 \boxed{\quad
 \Phi_{j,l}(z):=\sum_{a=0}^d\frac{D_a(\lambda;\sigma)}{F_a}z^a
       =(-qQ^lz;Q)_A(-q^2Q^{-l}z;Q)_B,\quad
 h_N(\lambda,\sigma)=\frac1{2\pi}\int_0^{2\pi}
                            |\Phi_{j,l}(e^{i\theta})|^2d\theta .
 \quad}
 \tag{16}
\]
Indeed recurrence (5) gives, modulo \(z^N\),
\[
 (1-\lambda z+qz^2)\Phi(z)
                   =(1+q\sigma z+qQz^2)\Phi(Qz).
 \tag{17}
\]
Successive coefficients are determined by \(1-Q^a\ne0\), \(a<N\).
For the proposed product the two endpoint parameters are
\(\{qQ^{-j},Q^j\}\), in that order for even \(N\), and reversed
for odd \(N\). This proves (17) and then (16).
It is a finite identity, not an infinite root-of-unity product.
Every factor parameter has modulus one. In particular
\[
                         1\le h_N(\lambda,\sigma)\le4^d .
 \tag{18}
\]
The upper bound follows by bounding each coefficient by
\(\binom da\) and using \(\sum_a\binom da^2=\binom{2d}d\le4^d\).

## 4. A uniform two-label volume profile

Define folded angles by
\[
 \lambda=2\sqrt q\cos\alpha,\quad
 \sigma=2\sqrt q\cos\beta,\qquad 0\le\alpha,\beta\le\pi .
 \tag{19}
\]
If \(\alpha+\beta>\pi\), replace them by
\((\pi-\alpha,\pi-\beta)\); simultaneous negation leaves \(h_N\)
unchanged. This means replacing \((\lambda,\sigma)\) by
\((-\lambda,-\sigma)\); its generating polynomial is the original
one at \(-z\), so Parseval is unchanged. Relabel the roots accordingly.
Hence assume \(\alpha+\beta\le\pi\), and put
\[
 \psi=(\pi-\alpha-\beta)/2.
\]
For \(\psi>0\) define
\[
 \theta_*=\arccos\frac{\cos\alpha-\cos\beta}{2},\qquad
 u_*=(\theta_*-\alpha)/2\in(0,\psi),
\]
\[
 \mathcal V(\alpha,\beta)=2\{
 \Lambda(u_*)+\Lambda(\alpha+u_*)+
 \Lambda(\psi-u_*)+\Lambda(\psi+\beta-u_*)\},
 \quad \Lambda(v)=-\int_0^v\log|2\sin t|\,dt .
 \tag{20}
\]
Use \(\mathcal V=0\) when \(\psi=0\). Extend \(\Lambda\)
oddly and \(\pi\)-periodically when using it outside \([0,\pi]\).
There is a universal constant \(C\) such that
\[
 \boxed{\quad
 \left|\log h_N(\lambda,\sigma)
                 -\frac N\pi\mathcal V(\alpha,\beta)\right|
      \le C\log N\qquad\text{for every }N,j,l.
 \quad}
 \tag{21}
\]
The assertion includes flat profiles, endpoint labels and both parities.

Here is a uniform proof fixing the action constant. Put
\(f(v)=\log|1-e^{iv}|\), of circle mean zero.
After \(z=q^{-1/2}e^{i\theta}\), the endpoint quadratic in (17)
is \((1-e^{i\alpha}e^{i\theta})(1-e^{-i\alpha}e^{i\theta})\).
The starting quadratic is
\((1+qe^{i\beta}e^{i\theta})(1+qe^{-i\beta}e^{i\theta})\).
Thus the finite arc energy has the following mean-zero primitive,
with \(\delta=\pi/N\):
\[
 E_\delta(\theta)=\frac2\pi\left\{
 -\Lambda\frac{\theta+\alpha}{2}
 -\Lambda\frac{\theta-\alpha}{2}
 +\Lambda\frac{\theta+\delta+\pi-\beta}{2}
 +\Lambda\frac{\theta+\delta-\pi+\beta}{2}\right\}.
 \tag{22}
\]
The arcs can be continued across a full turn: its integral of \(f\)
is zero. This accounts for the different endpoint orders in (16).
For \(E=E_0\), differentiation gives
\[
 E'(\theta)=\frac1\pi
       \log\left|\frac{\cos\theta-\cos\alpha}
                        {\cos\theta+\cos\beta}\right|.
 \tag{23}
\]
For \(\alpha+\beta<\pi\), the sign comparison for the squared ratio
is the sign of
\((\cos\alpha+\cos\beta)(\cos\alpha-\cos\beta-2\cos\theta)\).
The unique maximum is \(-\theta_*\), and the unique minimum is
\(\theta_*\). Logarithmic cusps have the same derivative sign on
their two sides and introduce no other extrema.
Substitution in (22), using \(\Lambda(\pi-v)=-\Lambda(v)\),
proves
\[
                    \max E=E(-\theta_*)=\mathcal V(\alpha,\beta)/\pi.
 \tag{24}
\]
If \(\alpha+\beta=\pi\), (23) and its zero mean give \(E=0\).
Each shifted \(\Lambda\) has zero circle mean, so no additive
boundary action is left undetermined in these statements.

For completeness the grid errors are uniform even at coalescing
endpoints. On any interval \(I\) of length \(\ell\le1\),
\[
 \int_I|f(v)|\,dv\le C\ell\log(e/\ell),\qquad
 |\Lambda(v+\epsilon)-\Lambda(v)|
                         \le C|\epsilon|\log(e/|\epsilon|).
 \tag{25}
\]
The bound follows by separating the logarithmic zero from its
bounded smooth remainder. Thus
\(\|E_\delta-E\|_\infty\le C\log N/N\).
For each finite product arc, compare its log samples with the
integral over their grid cells. Away from the bounded number of
cells nearest a zero, the summed oscillation is
\(\int|f'|=O(\log N)\). Near a zero the cell average is
\(-\log N+O(1)\), and the sample is at most that quantity plus
a constant. This proves the uniform one-sided upper bound
\[
 \log|\Phi_{j,l}(q^{-1/2}e^{i\theta})|^2
                              \le NE(\theta)+C\log N .
 \tag{26}
\]
It includes exact product zeros. Half-grid endpoints and one-cell
length changes contribute only \(O(\log N)\) by (25).

For the lower bound choose a midpoint of the actual \(q\)-grid
nearest a maximizing circle point. All factor zeros of (16) lie
on that grid; in the rotated coordinate it is the same shifted grid.
The chosen point is at distance at least \(\pi/(2N)\) from every
actual zero and within \(O(N^{-1})\) of a maximum of \(E\).
By (25) the action lost is at most \(C\log N/N\).
At these midpoint samples the zero-containing cells have both
sample and average equal to \(-\log N+O(1)\).
The grid comparison is therefore two-sided with error \(C\log N\).
On an interval of width \(\kappa_0N^{-3}\) about this point every
factor remains at distance at least \(\kappa_1/N\) from zero.
Its total logarithmic derivative is at most \(CN^2\); the product
logarithm changes by \(O(1)\). Parseval integration over this interval
loses only \(O(\log N)\). Together with (24)--(26) this proves (21),
including \(\psi=0\), without a channel cutoff.

## 5. The specified ideal octahedron

The volume in (20) has a fixed-boundary angle interpretation.
For \(0<u<\psi\), take two ideal tetrahedra of each type
\[
 (u,\psi-u,\pi-\psi),\qquad
 (\alpha+u,\psi+\beta-u,\psi).
 \tag{27}
\]
All angles are positive and sum to \(\pi\).
The internal edge has alternating angles \(\pi-\psi,\psi\),
of sum \(2\pi\). Boundary angle sums are fixed as \(u\) varies.
Their volume functional and derivatives are
\[
 W(u)=2\{\Lambda u+\Lambda(\alpha+u)
                    +\Lambda(\psi-u)+\Lambda(\psi+\beta-u)\},
\]
\[
 W'(u)=2\log\frac{\sin(\psi-u)\sin(\psi+\beta-u)}
                         {\sin u\sin(\alpha+u)},\qquad
 W''(u)=-2\sin\psi\left\{
 \frac1{\sin u\sin(\psi-u)}
 +\frac1{\sin(\alpha+u)\sin(\psi+\beta-u)}\right\}<0 .
 \tag{28}
\]
The endpoint derivatives are \(+\infty,-\infty\).
The unique maximum is \(u_*\): its equation is precisely
\(\cos(\alpha+2u)=(\cos\alpha-\cos\beta)/2\).
Off-critical assignments need not have consistent tetrahedral moduli.

At this maximum put
\[
 r=\frac{\sin u_*}{\sin(\psi-u_*)},\qquad
 v=r e^{i(\pi-\psi)}.
\]
The stationary equation says
\(r^{-1}=\sin(\alpha+u_*)/\sin(\psi+\beta-u_*)\).
Consequently the alternating shapes \(v,-1/v,v,-1/v\)
develop the four tetrahedra around the edge \(0\infty\).
Their six ideal vertices are
\[
                            0,\ \infty,\ 1,\ v,\ -1,\ -v .
 \tag{29}
\]
They form a convex ideal octahedron. The equator is centrally
symmetric and strictly convex, and its vertical side planes support
the four faces at \(\infty\). For an adjacent equatorial pair \(a,b\),
the other face is the hemisphere through \(0,a,b\), with boundary
circle \(|z|^2-\ell(z)=0\), \(\ell\) real linear.
Its values at \(-a,-b\) are \(2|a|^2,2|b|^2>0\).
Thus these four planes support as well, in the halfspace containing
\(\infty\). All four positive tetrahedra fill the convex hull.
Equatorial boundary angles alternate \(\psi,\pi-\psi\);
pole-to-equator angles alternate \(\psi+\alpha,\psi+\beta\).
They are positive and less than \(\pi\). Its volume is (20).

In particular \(0\le\mathcal V\le4G_{\rm Cat}\).
One direct upper proof writes the four positive arguments of
\(\Lambda\) in \(W/2\) as \(x_1,x_2,x_3,x_4\), of sum \(\pi\).
The functional \(W\) is twice the sum of the two tetrahedron volumes
in (27). Each is strictly concave on its angle simplex:
the negative Hessian in two angle coordinates has positive first
diagonal and determinant
\(\cot p\cot q+\cot q\cot r+\cot r\cot p=1\).
The angle assignment depends injectively and linearly on the \(x_i\),
so their sum is strictly concave on \(x_i>0,\sum x_i=\pi\).
Its differential vanishes at \(x_i=\pi/4\).
This gives the global maximum
\(2\sum_i\Lambda(\pi/4)=4G_{\rm Cat}\), the regular octahedron.
When \(\alpha=0\), (20) reduces to G's one-label family.
When \(\psi=0\), use its flat zero-volume limit.
No cell in a prescribed link complement has been identified here.

## 6. Independent joint Haar frames and exact crossing gains

Let \(P_j(T)\), \(P_l(S)\) denote full spectral idempotents.
For \(b=2\), only \(P_0(S)=I\) is present, since \(S=c=\mu_0\).
For \(b\ge3\), every pair of labels occurs. Define
\[
 P_{j,l}=P_j(T)P_l(S),\qquad
 Q_{j,l}=P_j(J_\nu')P_l(S),\qquad
 H_{\rm in}=\sum_{j,l}P_{j,l}^*P_{j,l},\quad
 H_{\rm out}=\sum_{j,l}Q_{j,l}^*Q_{j,l}.
 \tag{30}
\]
These are independently specified positive metrics in the physical
space \(W\), not definitions using \(C_\nu\).
They orthogonalize the indicated commuting pairs.
They need not equal G's single-tail Haar metric.
The projectors sum to identity, so their lower bound is \(N^{-2}I\).
Their upper bounds are \(e^{C_bN}I\): use the bounded actual generators,
the product formula for spectral projectors, and (3).
Thus both metric logarithms have size \(O_b(N)\).

For \(w\in\ker(S-\sigma)\), the complete joint input channel is
\[
 u_\lambda(\sigma;w)
   =\sum_{a=0}^d|a\rangle_2\otimes
                    \frac{q^{-a}D_a(\lambda;\sigma)}{F_a}\,w .
 \tag{31}
\]
Its first coordinate is \(w\), and unit upper-arrow elimination
shows that these are all joint \((\lambda,\sigma)\) vectors.
Because \(p_N(\lambda)=p_N(\sigma)=0\), its final recurrence closes.
Equation (9) now gives the exact, phase-retaining action
\[
 C_\nu u_\lambda(\sigma;w)
      =\kappa\,r_\lambda(\nu)\otimes w,\qquad
 (r_\lambda(\nu))_a=(-1)^aD_a(\nu;\lambda)/F_a.
 \tag{32}
\]
The output is a joint \((J_\nu',S)\) eigenvector with the same labels.
In (30) the norm of a vector in one joint channel is its original
physical norm. Therefore
\[
 \boxed{\quad
 \frac{\|C_\nu u\|_{H_{\rm out}}^2}{\|u\|_{H_{\rm in}}^2}
      =\frac{h_N(\nu,\lambda)}{h_N(\lambda,\sigma)}
          \quad(0\ne u\text{ in the joint }(\lambda,\sigma)\text{ channel}).
 \quad}
 \tag{33}
\]
Multiplicities in \(w\) are unrestricted. This is an exact all-channel
orthogonality calculation for the actual crossing, not a phase-free model.
Writing \(\alpha_\xi\) for the folded angle of a root \(\xi\),
(21) also computes its local energy increment uniformly:
\[
 \frac1N\log\frac{h_N(\nu,\lambda)}{h_N(\lambda,\sigma)}
 =\frac{\mathcal V(\alpha_\nu,\alpha_\lambda)
             -\mathcal V(\alpha_\lambda,\alpha_\sigma)}{\pi}
                              +O(\log N/N).
 \tag{33a}
\]
The same intermediate label \(\lambda\) occurs in both terms.
This is not a telescoping assertion for neighboring crossings
without matching their different interface frames.

Both signs use the same finite kernel. On a scalar deeper channel
\(S=\sigma\), let \(U_\sigma\) have columns (31), with \(w=1\),
and write \(C_{\nu|\sigma}\) for the resulting \(N\times N\) matrix.
These columns form a complete simple eigenbasis. Reciprocity and
\(\bar F_a=(-1)^aq^{-a(a+1)}F_a\) give
\[
 C_{\nu|\sigma}=\kappa\mathcal D\overline{U_\nu}U_\sigma^{-1},
 \qquad
 C_{\nu|\sigma}^{-1}
       =\mathcal D\,\overline{C_{\sigma|\nu}}\,\mathcal D^{-1}.
 \tag{33b}
\]
The second equality uses \(\mathcal D\overline{\mathcal D}=I\)
and \(\bar\kappa=\kappa^{-1}\). Conjugation here is on the scalar
channel matrix with its two parameters exchanged; it is not a
replacement of an original marked row or a free permutation of heads.

The positive functions in (33) have their joint spectral meaning.
For example \(h_N(T,S)=\sum_{j,l}h_N(\mu_j,\mu_l)P_{j,l}\).
Equation (33) is equivalently
\[
 C_\nu^*H_{\rm out}C_\nu
       =H_{\rm in}\frac{h_N(\nu,T)}{h_N(T,S)} .
 \tag{34}
\]
All products on the right are Hermitian in their prescribed metric.
There is a constant-one propagation law between explicit reweightings:
\[
 \widetilde H_{\rm in}=H_{\rm in}h_N(\nu,T),\qquad
 \widetilde H_{\rm out}=H_{\rm out}h_N(J_\nu',S),\qquad
 C_\nu^*\widetilde H_{\rm out}C_\nu=\widetilde H_{\rm in}.
 \tag{35}
\]
The weights have the actual shared labels in (33); they are not
independently maximized edges. By (18), or (21), their logarithmic
cost is \(O(N)\), so the reweighted metrics also have radius \(O_b(N)\).
They are different interface forms, not a common unitarizing metric.

## 7. Sharp source-channel costs and remaining scope

Specialize \(\nu=c\) and put \(g_N(\lambda)=h_N(c,\lambda)\),
as in G. From (20)--(21),
\[
 1\le h_N(\lambda,\sigma)
       \le\exp\{(4G_{\rm Cat}/\pi)N+O(\log N)\}
 \tag{36}
\]
uniformly over all nodes. G gives the matching maximum for \(g_N\).
The two-label formula also proves this bound directly by (29).
Thus (33) and its inverse give upper exponent \(2G_{\rm Cat}/\pi\)
for both crossing norms. This is sharp when \(b\ge3\):
\[
 \boxed{\quad
 \log\|C_c\|_{H_{\rm in}\to H_{\rm out}}
  =\log\|C_c^{-1}\|_{H_{\rm out}\to H_{\rm in}}
       =\frac{2G_{\rm Cat}}\pi N+O_b(\log N).
 \quad}
 \tag{37}
\]
Indeed every \(\sigma\) occurs. The node \(-c\) is in the spectrum,
\(g_N(-c)=h_N(c,-c)=N\) by the endpoint product in G, and
\(h_N(-c,-c)=g_N(c)\) by simultaneous-negation symmetry.
The channels \((\lambda,\sigma)=(c,-c)\), respectively
\((-c,-c)\), give the lower bounds in (37).
For \(b=2\), \(S=c\) and reciprocity instead gives
\[
                  \|C_cu\|_{H_{\rm out}}=\|u\|_{H_{\rm in}}
                       \quad\text{for every }u .
 \tag{38}
\]
This is still between two forms. It does not make the triangular
matrix (9) physically diagonal or remove its possible Jordan behavior.
For a general external \(\nu\), (36) gives the same universal upper
exponent for \(C_\nu\) and its inverse; sharpness for every \(\nu\)
is not asserted.

For an original paired source the specialization in (8) is retained
through every actual reduced word. G's legal marked row remains a
specified complex row, with its original external line.
Changing to (30) or (35) must transport that row and the input too;
G's boundary cost in a different metric is not silently reused.
The channel norm calculation does not insert separate probabilities
into the original scalar or bound its coherent channel sum below.
All actual pair-Casimir normal directions remain inside the full maps.
No peripheral or moving-\(q\) normal identity is asserted.

R already constructs the exact reduced braid representation through
a different \(F\)-prefix quotient, including a triangular Euler
first generator. C and K already supply conserved channels and graph
reduction, and G supplies the one-label volume slice.
Thus neither triangular reduction nor general orthogonal-polynomial,
Fourier, or Haar methods are claimed new. Twisted Clebsch--Gordan
and \(q\)-orthogonal-polynomial models are established background;
see Granovskii--Zhedanov,
[Twisted Clebsch--Gordan coefficients for SUq(2)](https://doi.org/10.1088/0305-4470/25/17/002).
No formula identification or proof from that paper is used here.
The additional assertions are the actual coideal crossing transform,
its two-label positive weights and volume profile, and the specified
joint-Haar transport laws with their sharp costs.
The sewn metric/phase comparison and the positive geometric scalar
estimate for arbitrary fixed short components remain unproved.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| G | [Coideal graph Gram and volume](research_coideal_graph_gram_and_octahedral_volume.md) | 398 | 35ca803fb3262b1f85a08c3aa9b9112bcc2823ce380ce82362ef18bd382d6766 |
| K | [Continuant source kernel](research_coideal_continuant_source_kernel.md) | 365 | 3ea997e5258c9413fd7c771a6a1475b90b39bf731ac55c0902fd136943b26f44 |
| P | [Full physical crossing](research_full_physical_crossing_gaussian_packet.md) | 306 | 7f1b9932f88aa549bc55088b6f056f5a362548bc51c9fdd7c6b00469e725f531 |
| C | [Conserved coideal channels](research_conserved_coideal_braid_channels.md) | 437 | b2a8c539742b4662ab8acbf4dc11c9bfa6acd27e895653ccfc47848278899fd4 |
| R | [Earlier actual reduced braid source](research_actual_reduced_braid_source.md) | 330 | 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243 |

Only written mathematics, source reads and text/hash operations were used.
Earlier final notes, the ledger, and public manuscripts are unchanged.
