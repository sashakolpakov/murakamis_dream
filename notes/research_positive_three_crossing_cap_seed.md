# A sharp original cap seed for positive three-crossing moments

Research note, 3 November 2026. Frozen manuscripts are unchanged.

The third moment of the positive three-crossing operator is the
squared norm of an original source whose full coefficient profile
has already been proved. This gives a sharp cap moment, stronger
lower bounds at every greater fixed length, and a quantitative
spectral-overlap statement. It also shows that one positive block
does not prepare the top almost-invariant vector.

## 1. Identification of the actual source

Use the original \(N\times N\) crossing \(M\), reversal \(J\), unit
coordinate vector \(e_0\), and scalar \(\kappa\) of
[the positive-cycle theorem](research_positive_three_crossing_cycle.md).
Thus \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\),
\(\kappa=q^{D^2/2}\), and
\[
 A=JM^3,\qquad H=M^*M>0,\qquad
 MAM^{-1}=\kappa H,\qquad
 \mu_{r,N}=e_0^*H^r e_0 .
 \tag{1}
\]
The exact identities \(JHJ=H^{-1}\) and
\(\mu_{-r,N}=\mu_{r-1,N}\) hold for every integer \(r\ge1\).
All matrices act in the full original Newton algebra, including
the normal directions at the repeated spectral roots.

Put
\[
 a_N=He_0=JM^{-2}e_0,\qquad
 (a_N)_j=N\,\frac{(-q)^j}{(Q;Q)_j},\qquad Q=q^2,
 \qquad \gamma_N=MJM^3e_0 .
 \tag{2}
\]
The first two equalities are the exact reciprocal-factorial cap
formula, not a prepared approximation to the input.

**Proposition 1.** At every integer level,
\[
 Ma_N=\kappa J\overline{\gamma_N},\qquad
                    \boxed{\ \mu_{3,N}=\|\gamma_N\|_2^2\ }.
 \tag{3}
\]
More generally, for each integer \(r\ge0\),
\[
 \gamma_{r,N}:=M(JM^3)^r e_0
       =\kappa^{r-1}H^{r+1}e_D,\qquad
                  \|\gamma_{r,N}\|_2^2=\mu_{2r+1,N}.
 \tag{4}
\]

*Proof.* The braid relation and \(M^{-1}=\overline M\) give
\[
 MJM^{-2}
   =(MJM)M^{-3}
   =\kappa JM^{-1}JM^{-3}.
 \tag{5}
\]
Applying (5) to \(e_0\) proves the vector identity (3).
Also \(\|MHe_0\|^2=e_0^*H^3e_0\), proving its norm statement.
For (4), \(A e_D=\kappa^3e_0\) and (1) imply
\(H e_D=\kappa M e_0\). Therefore
\(\gamma_{r,N}=\kappa^rH^rMe_0
=\kappa^{r-1}H^{r+1}e_D\).
Its squared norm is
\[
 e_D^*H^{2r+2}e_D
      =e_0^*H^{-2r-2}e_0
      =\mu_{2r+1,N},
\]
using the two reciprocal identities above. \(\square\)

Only \(r=1\) in (4) is assigned a sharp global profile below.
For \(r>1\), the right side is a genuine multiple-turn original
source; (4) does not replace it by a single crossing run.

## 2. Sharp third moment and longer actual capped chains

We recall the quantities in
[the proved next-crossing Fourier theorem](research_three_crossing_next_crossing_fourier.md),
equations (7)--(8). For \(0\le x<1/2\), set
\[
 \begin{split}
 X(x)&=e^{-2\pi ix},\\
 \lambda(x)&=\frac{3-2X(x)+\sqrt{4/X(x)-3}}2,\qquad
 \lambda_-(x)=\frac{3-2X(x)-\sqrt{4/X(x)-3}}2,\\
 I(x)&=\int_0^x\log\lambda(t)\,dt,\qquad
 G(x)=\sqrt{\frac{\lambda(x)}{\lambda(x)-\lambda_-(x)}},\\
 \mathcal J(x)&=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 \mathcal A(x)=\Re I(x)-2\mathcal J(x).
 \end{split}
 \tag{6}
\]
The square root in \(\lambda\) starts at \(+1\), its logarithm
starts at zero, and \(G(0)=1\). The cited proof establishes a
strict modulus gap on every compact subinterval of \([0,1/2)\).
Let \(x_*\) be the unique maximum of \(\mathcal A\), characterized
by
\[
 2\cos(2\pi x_*)=z_*,
 \qquad z_*^3-2z_*^2-z_*+3=0,\qquad -2<z_*<-1.
 \tag{7}
\]
Define the positive constants
\[
 \begin{gathered}
 a_*=-\mathcal A''(x_*)>0,\qquad v=2\mathcal A(x_*),\\
 C_3=\frac{|G(x_*)|^2}{4\sin^2(\pi x_*)}
                            \sqrt{\frac{\pi}{a_*}},\qquad
 C_2=3^{-1/4},\\
 c=2\mathcal J(5/6),\qquad
 \rho=\frac{5-\sqrt{21}}2 .
 \end{gathered}
 \tag{8}
\]

**Theorem 2.** Through all integer levels,
\[
             \mu_{3,N}
       =C_3 N^{3/2}e^{Nv}\bigl(1+O(N^{-1/2})\bigr).
 \tag{9}
\]
For every fixed integer \(m\ge3\), the literal capped chain
\[
 \mathcal Z_{m,N}
   =\phi\!\left(M^3J\cdots M^3J M^2e_0\right)
   =\kappa^{m-1}\mu_{m,N}
 \tag{10}
\]
has the exact positive bounds
\[
 \frac{\mu_{3,N}^{m-2}}{\mu_{2,N}^{m-3}}
       \le|\mathcal Z_{m,N}|
       \le\|H\|^{m-3}\mu_{3,N}.
 \tag{11}
\]
In particular, writing \(\ell_m=v+(m-3)(v-c)\) and
\(u_m=v+2c(m-3)\),
\[
 \begin{split}
 \frac{C_3^{m-2}}{C_2^{m-3}}\,N^{3/2}e^{N\ell_m}
          \bigl(1-O_m(N^{-1/2})\bigr)
       &\le|\mathcal Z_{m,N}|,\\
 |\mathcal Z_{m,N}|
       &\le C_3\rho^{(m-3)/2}N^{3/2}e^{Nu_m}
                         \bigl(1+O_m(N^{-1/2})\bigr).
 \end{split}
 \tag{12}
\]

*Proof.* The cited Fourier theorem controls the actual
\(\gamma_N=MJM^3e_0\), with the original forced recurrence and
endpoint normalization
\(|\gamma_{N,0}|=N^{3/2}(1+O(N^{-1}))\).
It proves a strict rate loss outside a neighborhood of \(x_*\),
including the middle band where the two local characteristic
roots have equal modulus. Its norm equivalent, equation (22), is
\[
 \|\gamma_N\|_2
 =|\gamma_{N,0}|N^{-3/4}
     \frac{|G(x_*)|}{2\sin(\pi x_*)}
     \left(\frac{\pi}{a_*}\right)^{1/4}
       e^{N\mathcal A(x_*)}(1+O(N^{-1/2})).
 \tag{13}
\]
Squaring (13) and applying (3) proves (9). In particular no
nonzero profile coefficient is assumed for a new input.

The positive cap spectral measure makes consecutive moment
ratios nondecreasing. Iterating
\(\mu_{r+1,N}/\mu_{r,N}\ge\mu_{3,N}/\mu_{2,N}\)
for \(r\ge3\) proves the lower bound (11). Its upper bound is
the pointwise spectral inequality
\(\lambda^m\le\|H\|^{m-3}\lambda^3\).
Finally the positive-cycle theorem gives
\[
 \mu_{2,N}=C_2 N^{3/2}e^{Nc}(1+O(N^{-1})),\qquad
 \|H\|=e^{2Nc}\bigl(\sqrt\rho+O(N^{-1/2})\bigr).
 \tag{14}
\]
Substitution in (11) proves (12). \(\square\)

The scalar
\[
             \delta=3c-v
                  =0.0631253938\ldots
 \tag{15}
\]
is strictly positive. This assertion does not rely on the decimal.
The accepted
[outward scalar certificate](../repro/results/research-three-crossing-real-tail-rates.json),
proved by
[its rational-interval checker](../experiments/verify_three_crossing_real_tail_rates.py),
gives \(9/20<\mathcal A(x_*)<23/50\).
Also the integrated sine Fourier series gives
\[
 c=\frac{3\sqrt3}{4\pi}
       \sum_{r=0}^\infty
        \left\{\frac1{(3r+1)^2}-\frac1{(3r+2)^2}\right\}
   >\frac{399}{968}\frac{60939}{78400}
   =\frac{3473523}{10841600}>\frac8{25}.
 \tag{16}
\]
Here the first three positive summands have been retained,
using \(\sqrt3>19/11\) and \(\pi<22/7\).
Consequently \(\delta>1/25\).
The elementary upper bound \(c<1/3\) proved in
[the actual next-step estimate](research_three_crossing_next_step_profile.md),
Section 4, also shows \(v>2c\).
Thus (12) strictly improves the previous lower exponential
rate \((m-1)c\) for every \(m\ge3\).
The upper and lower rates in (12) differ by exactly
\((m-3)\delta\); no equality of these rates is claimed when
\(m>3\).

## 3. What the actual cap spectral mass now proves

Let \(L_N=\|H\|\), \(B_N=H/L_N\), and form the actual
one-block cap state
\[
                  f_N=\frac{He_0}{\sqrt{\mu_{2,N}}}.
 \tag{17}
\]
This vector is exactly normalized, and \(0<B_N\le I\).
There is a uniform gap below the top eigenvalue of \(B_N\),
by the one-crossing operator theorem. Nevertheless its original
cap state obeys
\[
 r_N:=\langle f_N,B_Nf_N\rangle
      =\frac{\mu_{3,N}}{L_N\mu_{2,N}}
      =\frac{C_3}{C_2\sqrt\rho}\,
                    e^{-N\delta}(1+O(N^{-1/2})).
 \tag{18}
\]
In particular
\[
 \langle f_N,(I-B_N)f_N\rangle=1-r_N,\qquad
 \|(I-B_N)f_N\|^2=1-O(r_N),\qquad
 \|\mathbf1_{[\epsilon,1]}(B_N)f_N\|^2\le r_N/\epsilon
 \tag{19}
\]
for every fixed \(\epsilon>0\). The norm assertion follows from
\(0\le B_N^2\le B_N\); its squared norm lies between
\(1-2r_N\) and \(1-r_N\).
Thus the cap after one positive block is far from almost
invariant, and even its overlap with any fixed upper spectral
window is exponentially small.

There is also a lower overlap bound with an explicitly selected
larger spectral window. Set
\[
 E_N=\frac{\mu_{3,N}}{\mu_{2,N}},\qquad
 P_N^{\mathrm{high}}=\mathbf1_{[E_N/2,L_N]}(H).
 \tag{20}
\]
The superscript distinguishes this spectral projection from
the physical quotient polynomial. For the actual cap,
\[
 \boxed{\quad
   \|P_N^{\mathrm{high}}e_0\|^2
               \ge\frac{\mu_{3,N}}{2L_N^3}.
 \quad}
 \tag{21}
\]
Indeed the part of the third moment below \(E_N/2\) is at most
\((E_N/2)\mu_{2,N}=\mu_{3,N}/2\). The remaining part is at most
\(L_N^3\|P_N^{\mathrm{high}}e_0\|^2\), proving (21).
Consequently some unit eigenvector \(u_N\) of the actual \(H\)
satisfies
\[
 \begin{split}
 \lambda_N&\ge E_N/2
                  =\exp\{N(v-c)+O(1)\},\\
 |\langle u_N,e_0\rangle|^2
       &\ge \frac{\mu_{3,N}}{2N L_N^3}
          =\exp\{-N(6c-v)+O(\log N)\}.
 \end{split}
 \tag{22}
\]
Choose an orthonormal eigenbasis on the range of the projection
and use its dimension at most \(N\) for the second inequality.
This is a quantitatively nonzero cap overlap for an actual
spectral mode, rather than a freely prepared test vector.

The lower threshold \(E_N/L_N=r_N\) is itself exponentially
small. Therefore (21)--(22) do not identify the top eigenspace or
a geometric mode. Conversely, for the original cap and every
fixed \(\epsilon>0\), positivity gives the upper estimate
\[
 \|\mathbf1_{[\epsilon L_N,L_N]}(H)e_0\|^2
          \le\frac{\mu_{3,N}}{\epsilon^3L_N^3}
          =\exp\{-N(6c-v)+O(\log N)\}.
 \tag{23}
\]
The same exponent in these upper and lower bounds refers to
different windows; it is not an exact top-overlap asymptotic.

For the normalized state \(H^r e_0/\sqrt{\mu_{2r,N}}\), its
expectation defect for \(B_N\) is exactly
\[
 \left\langle
 \frac{H^re_0}{\sqrt{\mu_{2r,N}}},
 (I-B_N)\frac{H^re_0}{\sqrt{\mu_{2r,N}}}
 \right\rangle
 =1-\frac{\mu_{2r+1,N}}{L_N\mu_{2r,N}} .
 \tag{24}
\]
For \(r\ge2\), the estimates above do not determine whether this
quantity tends to zero. Letting the block count grow with \(N\)
would change the fixed source and is not used here.

The results concern original finite source scalars and vectors
at all level parities. They do not identify the capped words
as knots, identify \(v\) with a manifold volume, or establish
a free-boundary packet for general short chains.

## 4. Focused reproduction

[check_positive_three_crossing_cap_seed.py](../experiments/check_positive_three_crossing_cap_seed.py)
builds the crossing matrix by polynomial multiplication in the
original quotient. It compares the literal three-vertex capped
word, the direct vector \(MJM^3e_0\), the vector identity (3),
and the positive moment. Both signs and both parities are
included. It also checks the rational inequalities used for
\(\delta>0\) against the existing outward interval record,
without rerunning that unrelated contour certificate.
The [result](../repro/results/research-positive-three-crossing-cap-seed.json)
records all code and input hashes. These finite checks concern
exact normalizations; the sharp profile is the previously
proved theorem used explicitly in (13).
