# The original source at a stationary wire escape

Private written proof, 16 November 2026.

At a finite real-period boundary the stationary wire can escape to
infinity even though its endpoint angles and returns remain bounded.
The exact source distinguishes three objects there. Its extreme
Laurent coefficient deletes the edge and inserts one signed crossing
at each endpoint. Its compactification residue retains the original
edge kernel. Its complete lower lattice correction has zero residue
after the full physical Hermite data are retained.

This note identifies those objects, their constants and their actual
seam current. It also records the constrained integer charge shifts
of the limiting primitive equations. No edge deletion is asserted for
the residue, and no estimate for a partial joint connecting chain
follows from the completed-circle estimate below.

## 1. The literal factorial end

Fix \(N\ge2\), \(D=N-1\), \(\eta=(-1)^D\), and
\[
 q_N=e^{\pi i/N},\qquad
 C_N=e^{\pi iD^2/(4N)},\qquad \kappa=C_N^2,\qquad R=\kappa r_N .
 \tag{1}
\]
The last symbols denote the original physical crossing and its
normalized full-Hermite class. They are unrelated to the geometric
square root \(q_e\) below. Use the original halfwire
\[
 B_N(x,t)=
 \frac{N}{G_N(D/2-Nx+Nt/(2\pi))
          G_N(D/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
 \tag{2}
\]
In this section \(t\) stays in a fixed compact complex set and
\(\Im x\) is sufficiently negative. Put
\[
 w=e^{-2\pi ix},\quad d_N=\frac{D}{2N},\quad T=\frac{t}{2\pi},
 \quad Q_N=e^{2\pi i/N},\quad
 a_\pm=e^{2\pi i(d_N\pm T)} .
 \tag{3}
\]
Thus \(a_\pm^N=\eta e^{\pm iNt}\). All disk logarithms below
are their series at zero. Define
\[
 \begin{split}
 L_\pm(w)&=\log(1-\eta e^{\pm iNt}w^N),\\
 L_0(w)&=\log(1-w^N),\\
 f_\sigma(z)&=-\frac1N\sum_{k=0}^{N-1}k
                   \log(1-zQ_N^{\sigma k})
               +\frac{\sigma i}{2\pi N}\operatorname{Li}_2(z^N),
                 \qquad \sigma=\pm1,\\
 \Psi_{N,t}(w)&=-(d_N+T)L_+(w)-(d_N-T)L_-(w)\\
 &\hspace{12mm}-f_-(a_+w)-f_-(a_-w)-2f_+(w).
 \end{split}
 \tag{4}
\]
These are holomorphic where \(|w|,|a_+w|,|a_-w|<1\), and
\(\Psi_{N,t}(0)=0\).

**Proposition 1 (the exact lower end).** On this lifted disk,
\[
 \begin{split}
 R_{N,t}(w)
 &=\frac{(1-\eta e^{iNt}w^N)(1-\eta e^{-iNt}w^N)}
          {(1-w^N)^2}\\
 &=1+\frac{P_N(-2\cos t)w^N}{(1-w^N)^2},\\
 B_N(x,t)
 &=\frac{e^{i\pi D x+iNt^2/(4\pi)}}{NC_N}
       \exp\{x\log R_{N,t}(w)+\Psi_{N,t}(w)\}.
 \end{split}
 \tag{5}
\]
In particular the multiplier under \(x\mapsto x+1\) is
\(\eta R_{N,t}\). The factor containing \(x\log R_{N,t}\)
is retained; the factorial itself has not been declared a
single-valued function of \(w\).

**Proof.** The exact canonical factorial formula and its conjugate
give, with \(\sigma\Im y<0\),
\[
 \begin{split}
 \log G_N(Ny)
 ={}&\tfrac12\log N+\frac{\sigma i\pi N}{2}y^2
       -\frac{\sigma i\pi D}{2}y
       +\sigma i\pi\left(\frac N{12}-\frac14+\frac1{12N}\right)\\
 &+y\log(1-e^{-2\pi i\sigma Ny})
                   +f_\sigma(e^{-2\pi i\sigma y}).
 \end{split}
 \tag{6}
\]
Use the lower formula for \(y=x\), and the upper one for
\(y=d_N-x\pm T\). The denominator's polynomial part is
\[
 2\log N-i\pi D x+\frac{i\pi D^2}{4N}
                                      -\frac{iNt^2}{4\pi}.
 \tag{7}
\]
Its negative nonpolynomial part is exactly
\(x(L_++L_--2L_0)+\Psi_{N,t}\). This proves (5), including
the \(N^{-1}\) and \(C_N^{-1}\) constants. Finally
\(P_N(-2\cos t)=2-2\eta\cos Nt\) proves the second expression
for \(R_{N,t}\). \(\square\)

For fixed \(N\), the exponential after the first factor tends to
one as \(\Im x\to-\infty\) on a bounded real lift, uniformly with
fixed derivatives on smaller endpoint-angle compacts. Conjugation
of the same canonical gamma product gives the upper end:
\[
 B_N(x,t)\sim
       \frac{C_N}{N}e^{-i\pi D x-iNt^2/(4\pi)}
                       \qquad(\Im x\to+\infty).
 \tag{8}
\]
These are fixed-level end statements. Formula (5), rather than
an interchange of limits, will be used for large-\(N\) estimates.

The canonical half-plane primitive of the incidence phase satisfies
\[
 b_{\rm can}(x,t)
   =i\pi x+\frac{it^2}{4\pi}-\frac{i\pi}{4}+o(1)
                    \qquad(\Im x\to-\infty),
 \tag{9}
\]
and its upper counterpart is the negative of this polynomial,
with an \(o(1)\) remainder. This follows either from the explicit
canonical sine primitive in (6) or by substituting its two
half-plane primitives in
\(-J(1/2-x+T)-J(1/2-x-T)-2J(x)\).
The primitive constants are those fixed by the original \(G_N\);
no geometric logarithmic marking has yet been substituted.

## 2. The extreme coefficient and the residue are different sources

The exact cardinal representative is
\[
 \widetilde B_N(x,z)=\sum_{j=0}^{D}
    \frac{\sin\pi N(x-j/N)}{N\sin\pi(x-j/N)}e_j(z).
 \tag{10}
\]
It is an ordinary degree-at-most-\(D\) polynomial in \(z\),
with wire frequencies
\(\Lambda_N=\{-D/2,-D/2+1,\ldots,D/2\}\).
Its full Hermite data agree with (2). Thus its top coefficient is
\[
 [e^{i\pi D x}]\widetilde B_N(x,z)
   =\frac1N\sum_{j=0}^{D}(-q_N)^j e_j(z)=\frac{r_N(z)}N ,
 \tag{11}
\]
and the bottom coefficient is \(r_N^{-1}/N\), represented by
its degree-below-\(N\) polynomial.

One can identify the crossing in (11) directly from (5).
The pinned signed Gaussian source gives \(R=\kappa r_N\) and,
at the original unwrapped nodes \(y_j=(2j+1)\pi i/N\), the
values and first logarithmic derivatives of \(r_N\) as those of
\[
 q_N^{-D^2/4}
          \exp\!\left(\frac{(y-\pi i)^2}{2\hbar}\right),
                  \qquad \hbar=2\pi i/N .
 \tag{11a}
\]
With \(y=i(\pi-t)\), multiplication by \(\kappa\) makes
(11a) exactly \(C_Ne^{iNt^2/(4\pi)}\). This retains both
physical values and normals, including \(N=2\).
Hence the leading coefficient of
(5) has class \(R/(NC_N^2)=r_N/N\). Equality of the
degree-below-\(N\) representatives gives the ordinary polynomial
identity (11). Conjugation gives its inverse version. At the odd
simple node only the original value is imposed; at every double
node all first normals are included.

For a direct same-index edge define the polynomial-valued Laurent
function
\[
 F_N(w;z,z')=
       \widetilde B_N(x,z)\widetilde B_N(x,z')
       =\sum_{m=-D}^{D}A_m(z,z')w^{-m}.
 \tag{12}
\]
Exact wire averaging and (11) give
\[
 A_0=\frac{K_T(z,z')}{N},\qquad
 A_D=\frac{\kappa^{-2}}{N^2}R(z)R(z'),\qquad
 A_{-D}=\frac{\kappa^2}{N^2}R^{-1}(z)R^{-1}(z').
 \tag{13}
\]
These hold in the full tensor algebra; with free endpoints they
mean the specified ordinary polynomial representatives. For
\(A_0\), evaluate (12) at the original \(N\)-point wire grid:
its frequencies satisfy \(|m|\le D<N\), so the sum is exactly
\(NA_0=\sum_j e_j(z)e_j(z')=K_T\).

**Theorem 2 (the exact current normal form).** Put
\[
 V_N(w)=\sum_{\substack{-D\le m\le D\\m\ne0}}
                         \frac{A_m w^{-m}}{2\pi i m}.
 \tag{14}
\]
Then
\[
 \boxed{\quad
 F_N\,dx=-\frac{K_T}{2\pi iN}\frac{dw}{w}+d_wV_N .
 \quad}
 \tag{15}
\]
In particular the compactification residue retains the original
edge kernel. It is not either of the rank-one extreme coefficients
in (13).

**Proof.** Use \(dx=-dw/(2\pi iw)\) and differentiate each
finite term in (14). This proves (15). The increasing original
\(x\)-period winds clockwise in \(w\), so its integral is
\(+K_T/N\). The usual wire prefactor \(N\) restores exactly
\(K_T\), with no sign or normalization loss. \(\square\)

All other original factors may be attached before this identity
is used. Wedge (15) with their angular and wire differentials
and multiply by their coefficients. Derivatives of the resulting
primitive in any remaining coordinate wedge with that already
present differential and vanish. Thus (15) is an exact joint
source-current identity, with arbitrary signed vertex powers,
shared spectators, and free boundary polynomials and their normals.
It also applies simultaneously to any specified set of wires.
Its iterated residue retains all their original kernels.

The extreme coefficient does have a separate precise deletion
meaning. If both endpoints are traced, the original wire-normalized
coefficient \(NA_D\) replaces the edge by
\[
             \frac{\kappa^{-2}}N R(z)R(z').
 \tag{16}
\]
It deletes that edge and increases both endpoint crossing powers
by one, retaining every other original factor. The upper extreme
decreases both powers by one and has factor \(\kappa^2/N\).
This is an identity of coefficients, not an identity for the
wire-period integral or for a changed knot framing. At a free
endpoint the prescribed polynomial is multiplied by the ordinary
representative \(r_N\) or \(r_N^{-1}\); that endpoint is not
silently traced.

For completeness the same finite-band statement covers actual
reversed halfwires. Give an incidence orientation
\(\delta=1\) for \(x\) and \(\delta=-1\) for \(D/N-x\).
At the end \(q_e=\sigma i\), \(\sigma=\pm1\), its extreme
halfwire coefficient is
\[
                       \frac{\kappa^{-\sigma}}N R^{\sigma\delta}.
 \tag{17}
\]
Indeed reversal reverses the frequency and adds
\(\exp(-\sigma i\pi D^2/N)=\kappa^{-2\sigma}\).
The pair extreme is therefore
\(\kappa^{-2\sigma}R^{\sigma\delta_v}R^{\sigma\delta_w}/N^2\).
Its constant coefficient is the actual \(K_T/N\) or \(K_I/N\),
according to the two orientations. The geometric statements below
refer only to the original same-index circle-tree chart.

## 3. The lower lattice cap and the retained phase

For the original lower lattice correction, (12) implies
\[
 \frac{F_N}{e^{2\pi iNx}-1}\,dx
   =-\frac1{2\pi i}\frac{w^NF_N(w)}{w(1-w^N)}\,dw .
 \tag{18}
\]
Since \(N-D-1=0\), this form is holomorphic at \(w=0\).
Its integral on every complete sufficiently small circle is
exactly zero. This includes all lower aliases, all physical
first normals, and arbitrary original exterior contractions.
It is the adopted finite-band cancellation, now placed at
the stationary wire end.

Before physical contraction the factorial pair
\(f_N(x;t,u)=B_N(x,t)B_N(x,u)\) has the exact form
\[
 f_N=C_{N;t,u}\,w^{-D}
       \exp\{x\log R_N(w)+\Psi_N(w)\},
 \quad
 C_{N;t,u}=\frac{\kappa^{-1}}{N^2}
                  e^{iN(t^2+u^2)/(4\pi)},
 \tag{19}
\]
where \(R_N=R_{N,t}R_{N,u}\), \(\Psi_N=\Psi_{N,t}+\Psi_{N,u}\).
After multiplication by \(w^N\) and removal of the explicitly
displayed covering factor, the lower correction has order
\(N-D=1\). Its normalized one-form is holomorphic at zero.
Removing that covering factor is not an exact untraced-source
replacement.

**Proposition 3 (completed factorial alias cap).** Let the endpoint
angles range over a fixed compact complex set. For every prescribed
real rate \(L\), a sufficiently small fixed \(\rho>0\) gives
\[
 \left|\int_{\text{one full lift of }|w|=\rho}
           \frac{f_N(x;t,u)}{e^{2\pi iNx}-1}\,dx\right|
                   \le C_LN^{-2}e^{NL}
 \tag{20}
\]
uniformly for all sufficiently large \(N\). The original covering
factor in (19) is included in this integral.

**Proof.** Choose \(T\) bounding both endpoint imaginary parts
in absolute value, and put \(r=e^T\rho<1/2\). All the disk
arguments in (4) have modulus at most \(r\), uniformly in \(N\).
The series bounds in the exact factorial formula give
\[
 |\log R_N|\le\frac{8r^N}{1-r^N},\qquad
 |\Psi_N|\le\frac{4(N-1)r}{1-r}+C\frac{r^N}{1-r^N}.
 \tag{21}
\]
The constant \(C\) is uniform on the endpoint compact set.
On one bounded real lift of the circle, \(|x|\le C_\rho\).
Also \(|C_{N;t,u}|\le N^{-2}e^{NV_0}\) for a fixed \(V_0\).
The integral with \(e^{x\log R_N}\) removed is zero, since
its normalized form is holomorphic at zero. Subtract this
zero integral and use
\[
 |e^{x\log R_N}-1|
       \le |x|\,|\log R_N|e^{|x|\,|\log R_N|}.
 \tag{22}
\]
The factor \(w^Nw^{-D}\) is \(w\), so no negative growing
power of \(\rho\) remains. The resulting bound is
\[
 C_\rho N^{-2}
   \exp N\left\{V_0+\frac{4r}{1-r}+\log r\right\}.
 \tag{23}
\]
Increasing \(C_\rho\) absorbs the uniformly bounded remaining
terms for large \(N\). The expression in braces tends to
\(-\infty\) as \(\rho\to0\). This proves (20).
It is the balanced-order cap estimate with its hypotheses
verified for the literal paired edge. \(\square\)

Multiplication by an exterior independent of this wire multiplies
the bound by that exterior's norm. No such norm or geometric rate
for an arbitrary partially integrated exterior is supplied here.
In particular (20) is not an estimate for a partial arc, or for
the original main wire period in (15).

There is a matching statement about the actual logarithmic phase.
On a connected positive stationary tail with \(q_e\to i\),
let \(\beta_{\rm can}=b_{\rm can}(x,t)+b_{\rm can}(x,u)\).
Its exponential stationary equation is one, whereas (9) gives
\(\partial_x\beta_{\rm can}\to2\pi i\). Consequently, sufficiently
far along that tail,
\[
       \partial_x\beta_{\rm can}=2\pi i,\qquad
       \partial_x\beta_{\rm geom}=0 .
 \tag{24}
\]
Here the second equality is the original retained stationary
marking. Local differences of the sine-log primitives are integer
affine Fourier characters. Their wire term is therefore exactly
\(-2\pi ix\), with all angular characters and constants still
retained. At \(q_e\to-i\) the wire term is \(+2\pi ix\).
Thus the marked end carries the factor \(w^N\), or its upper
analogue, relative to the canonical end. This explains the
regular order one; it does not select that sector in the original
period or authorize discarding the other sectors.

## 4. Limiting primitive rows and their coupled charge lifts

Assume now the bounded finite-real-period setting of the pinned
compactness theorem: a proper selected subset of a connected
original tree, complete outside angles, fixed powers, positive
charges, and a supplied positive approach with bounded real periods.
At a convergent escaping edge write
\[
 q_e\to\sigma i,\quad \sigma=\pm1,\quad
 a_v=\tan(t_v/2),\quad a_w=\tan(t_w/2).
 \tag{25}
\]
The limiting angles and returns are bounded, their half-angle
cosines are nonzero, and \(q_e\pm a_v,q_e\pm a_w\ne0\).
The original return identities imply
\[
 e^{2r_{ve}}=\frac{q_e+a_v}{q_e-a_v}=e^{-\sigma it_v}.
 \tag{26}
\]
Therefore there are fixed integers \(k_{ve},k_{we}\), determined
by the actual continued returns, such that
\[
 r_{ve}=-\frac{\sigma i t_v}{2}+\pi i k_{ve}.
 \tag{27}
\]
These two integers are not independent. In fact
\[
 e^{r_{ve}+\sigma it_v/2}
    =\sigma i\,\frac{\cos(t_w/2)}{\cos(t_v/2)},\qquad
                    k_{ve}+k_{we}\ \text{is odd}.
 \tag{28}
\]
For the first equality substitute \(q_e=\sigma i\) in
\(e^{r_{ve}}=\cos(t_w/2)(q_e+a_v)\); the elementary half-angle
identity is
\((\sigma i+\tan(t/2))e^{\sigma it/2}
       =\sigma i/\cos(t/2)\).
Multiplication of the endpoint equalities proves the parity.

The weak positive-domain inequality at (25) forces
\(\Re a_v=\Re a_w=0\). Since the half-angle cosines are units,
the closed real-angle ranges give \(s_v,s_w\in\{0,\pi,-\pi\}\).
They cannot both be zero: then both imaginary tangent moduli
are strictly less than one, contradicting
\(a_v^2+a_w^2=-2\). They cannot both have modulus \(\pi\):
their nonzero heights then give both moduli strictly greater
than one. Exactly one endpoint has \(s=\epsilon\pi\),
\(\epsilon=\pm1\); the other has \(s=0\).

At the zero-real-angle endpoint the closed range
\(|\Im r|\le\pi/2\) in (27) forces \(k=0\). At the other,
that range and (28) force
\[
            k=\sigma\epsilon,\qquad
            \Im r=\sigma\epsilon\pi/2 .
 \tag{29}
\]
The limiting nonnegative positive-prefix pairing is
\(\Re(r\overline t)=\pi k\,\Im t\); because the endpoint
height is nonzero, it also gives
\(\sigma\epsilon\,\Im t>0\).
These are constraints on a supplied escape, not an assertion
that such an escape occurs in the inverse component of the center.

Write the original period row as
\(P_v=\sum_f r_{vf}-in_vt_v/2=u_v-\pi ic_v\).
Removing the escaping edge and substituting (27) gives exactly
\[
 \boxed{\quad
 P^{G\setminus e}_{\,n_v+\sigma}(t)
                   =u_v-\pi i(c_v+k_{ve})
 \quad}
 \tag{30}
\]
at each selected endpoint, with the other rows unchanged. An outside
complete endpoint retains its fixed angle and has no selected period
row to replace.
Thus the limiting classical edge deletion agrees with the signed
crossing change of the extreme Laurent coefficient, but its
selected charge lifts are fixed by (28)--(29). A unit charge
can become zero or two at the endpoint, so no previous
nonzero-charge deletion comparison is automatic. Equation (30)
does not change the original peripheral marking or assert a
quantum identity between entire cosine coupons of different charge.

## 5. What the seam current preserves

Use only the admissible lifted charts and homotopies of the original
source theorems in this section. The endpoint compact sets allowed
in the scalar estimate (20) do not by themselves supply such a
joint source chart or homotopy.

The adopted joint-lens and moving-seam identities retain
\[
 \Omega_{\rm fac}-\Omega_{\rm car}=d\Theta,\qquad
 J_e=(\tau_e^*-1)\Theta,\qquad
 \tau_e^*\Omega_{\rm fac}-\Omega_{\rm fac}=dJ_e.
 \tag{31}
\]
For a compact chain with paired wire faces and the prescribed
coordinate-fixed angular endpoint faces, their exact normalization is
\[
 \int_C\Omega_{\rm fac}-\sum_e\int_{F_e}J_e
                         =\int_C\Omega_{\rm car}.
 \tag{32}
\]
Combining (15) with (31) supplies an explicit primitive for the
factorial wire-end form minus its original-kernel residue. The
primitive includes both the finite Laurent primitive \(V_N\)
and \(\Theta\); its seam defect is precisely the existing \(J_e\).
This is an exact original-source boundary relation at every
finite truncation. Full free boundary polynomials remain cardinal.

On a partial geometric angular patch the additional angular side
faces need not annihilate \(\Theta\). On an incomplete wire arc
the Laurent primitive need not have cancelling endpoint values.
Neither contribution is a scalar Ward endpoint evaluation.
The even-twist vertex deletion therefore cannot be substituted
for this wire current.

The finite-real-period energy gap bounds the retained classical
action on compact annuli away from its center. It does not estimate
the full original-kernel residue in (15), the other Fourier sectors,
or these angular and seam sides. A sufficient next source step
would be an actual global relative-chain decomposition that
completes the escaping marked pieces by the alias caps in (20),
and retains and controls the remaining sides or cancels their
original-kernel residues. This note constructs the local boundary
identity and the completed alias cap; it does not construct that
global decomposition.

## Direct sources

The complete source proofs and directly used implications were read
at the following versions; unchanged earlier full readbacks of the
two author-owned notes are retained.

* Exact canonical factorial:
  research_exact_cyclotomic_factorial.md,
  SHA256 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b.
* Balanced factorial boundary order:
  research_balanced_factorial_boundary_order.md,
  SHA256 aa8db0d6b55b45791d1d9c8ff734fd79e5d985ec6c7a69d485a2bcff6e7e5c35.
* Full-Hermite finite Fourier band:
  research_newton_interpolation_finite_fourier_band.md,
  SHA256 2e2d95184081ba6440b56268cb597624d97a5f1931e8c0df886fa754e6684304.
* Original signed crossing normalization and full Gaussian jets:
  research_signed_gaussian_ward_endpoint_packet.md,
  SHA256 6bdced1b01917e41631386a24b337b60dfe5b04d35d70007cb56badc511a0191.
* Original joint factorial lens:
  research_joint_factorial_lens_relative_source.md,
  SHA256 a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54.
* Exact moving-seam source descent:
  research_moving_wire_seam_source_descent.md,
  SHA256 2b632735243fc450e2ce0f276f339c9fad0b5524724364b83f15690b4896f33d.
* Original unsummed stationary ideal and logarithmic marking:
  research_unsummed_two_square_morse_lift.md,
  SHA256 82ad7a75e6ab2857bbebb2f003f7e182ab1f26da1cf425f579106cdad11d15dd.
* Finite-real-period compactness and its exact return identities:
  research_real_period_image_compactness.md,
  SHA256 8ecdecc2c71e8a47a83fe60986ed618abaa926937920f376abebed779fb0c37e.

Only written mathematical proofs, source-text reads, and file hashes
were used. No mathematical program, numerical computation, test,
or compilation was run. Frozen and public files were unchanged.
