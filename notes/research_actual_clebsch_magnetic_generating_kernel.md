# Actual Clebsch generating legs and their binomial dual

Private written proof, 18 November 2026.

The ordinary generating function of an actual normalized Clebsch column
admits an exact magnetic summation. A contracting finite recurrence then
gives a holomorphic unit on a full small activity disk. Its literal
ordinary-binomial dual has a selected coefficient-circle saddle with
nonzero amplitude. A uniform-Casimir extension then estimates both
literal confluent partner legs by Cauchy differentiation. The phases,
finite support and full Hermite channel row are retained. No subsequent
Casimir-channel contraction is estimated.

Complete direct H fixes the physical column and its full Hermite inverse.
Complete direct C supplies the finite Chu identity used below. The
recurrence, analytic estimates, and dual contour proof are given here.
Complete direct U supplies the stronger uniform-Casimir magnetic unit;
Section 5 proves its actual binomial-dual and partner extension.

## 1. The actual column and its magnetic generating function

Put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1},
 \quad f_a=(Q;Q)_a,\quad
 s_a=\prod_{h=1}^a2\sin(\pi h/N).
 \tag{1}
\]
Write \(\beta(a,b)=s_a/(s_bs_{a-b})\). For indices below \(N\),
\({a\brack b}_Q=q^{b(a-b)}\beta(a,b)\), with the displayed phase.
On the physical degree \(0\le T\le d\), H defines the normalized
Casimir column \(f_T(\lambda_j)\), whose first entry is one, at
\(\lambda_j=q^{2j+1}+q^{-2j-1}\), \(0\le j\le T\).
Set \(r=T-j\). Its literal highest vector and descendant are
\[
 h_j=\sum_{a=0}^j(-1)^ax^{-a}Q^{a(a-1)/2}
       {j\brack a}_Q|a,j-a\rangle,
 \qquad
 f_T(\lambda_j)=\frac{x^r}{{T\brack j}_Q}
                   \frac{F_\Sigma^r}{f_r}h_j.
 \tag{2}
\]
The first formula follows from H's generic highest vector by root
specialization. In polynomial coordinates it is
\[
 h_j(w_1,w_2)=\prod_{a=0}^{j-1}(w_2-x^{-1}Q^aw_1).
 \tag{3}
\]
Let \(v(w)|a,b\rangle=w_1^aw_2^b\), and define
\(L_{T,j}(w)=v(w)f_T(\lambda_j)\). We claim the exact formula
\[
 \boxed{
 L_{T,j}(w)=\frac{x^r}{{T\brack j}_Q}h_j(w)
 [t^r]\frac1{(tw_1;Q)_{j+1}(x^{-1}tw_2;Q)_{j+1}}.}
 \tag{4}
\]

Here is a finite proof including the cap. The literal actions are
\(F_i=w_i(1-QT_{Q,i})\), \(K_1^{-1}=x^{-1}T_{Q,1}\), and
\(F_\Sigma=F_1+K_1^{-1}F_2\). Its two summands obey
\(AB=Q^{-1}BA\); in the order \(A^{r-b}B^b\), the divided
coefficient is \(1/(f_{r-b}f_b)\). On one actual head,
\[
 \sum_{n=0}^{d-a}\frac{t^nF^n}{f_n}w^a
 =w^a\frac{1-(tw)^N}{(tw;Q)_{a+1}}.
 \tag{5}
\]
This follows either from Gaussian Pascal or multiplication by the
denominator. The numerator is retained; it first affects degree \(N\).
Since \(r<T+1\le N\), extraction of \(t^r\) from the two-head
product is therefore exactly extraction from
\[
 \sum_{a=0}^j
 \frac{(-1)^ax^{-a}Q^{a(a-1)/2}{j\brack a}_Q
                 w_1^aw_2^{j-a}}
 {(tw_1;Q)_{a+1}(x^{-1}tQ^aw_2;Q)_{j-a+1}}.
 \tag{6}
\]
Put \(U=tw_1,V=x^{-1}tw_2\). After taking the common denominator
in (4), its numerator divided by \(w_2^j\) is
\[
 (UQ;Q)_j\sum_{a=0}^j
 \frac{(Q^{-j};Q)_a(V;Q)_a}{f_a(UQ;Q)_a}
                    (UQ^{j+1}/V)^a
 =(QU/V;Q)_j.
 \tag{7}
\]
The equality is C's finite Chu identity. Since \(x^{-2}=Q\), the
last polynomial is \(h_j/w_2^j\). Apparent denominators in this
calculation are removed by polynomial continuation. This proves (4).
It does not extend removal of the numerators in (5) to degrees at
least \(N\).

On \(w_2\ne0\) put \(\rho=xw_1/w_2\), and define
\[
 P_{n,j}(\rho)=\sum_{a=0}^n
       \beta(j+a,a)\beta(j+n-a,n-a)\rho^a,
 \qquad p_{n,j}=P_{n,j}/\beta(j+n,n).
 \tag{8}
\]
All indices used below satisfy \(j+n<N\). The two Gaussian
coefficients in (4) have the common phase \(q^{jn}\). It cancels
the phase of the normalizer in (2), giving
\[
 \boxed{L_{T,j}(w)=w_2^T\mathcal L_{T,j}(\rho),\qquad
 \mathcal L_{T,j}(\rho)=(Q\rho;Q)_j p_{r,j}(\rho).}
 \tag{9}
\]
Thus \(\mathcal L_{T,j}(0)=1\). Neither the highest-vector phase
nor an input/output gauge has been discarded.

## 2. A full disk, not only a positive-radius estimate

Fix a compact set of real parameters
\[
                  0<\xi<\tau<1,
 \qquad \xi=j/N,\quad\tau=T/N,\quad\kappa=\tau-\xi.
 \tag{10}
\]
All asymptotics use these actual scaled integer parameters. There
is an \(\epsilon>0\), depending only on that compact set, such
that \(\mathcal L_{T,j}\) is zero-free on \(|\rho|<\epsilon\)
for all sufficiently large \(N\), and has the relative asymptotic
proved below. No interpolation of \(j\) or \(T\) is intended.

The exact recurrence which proves this is
\[
 p_{0,j}=1,\quad p_{1,j}=1+\rho,\qquad
 p_{n,j}=(1+\rho)p_{n-1,j}-\rho b_n p_{n-2,j},
 \tag{11}
\]
where
\[
 b_n=
 \frac{\sin(\pi(2j+n)/N)\sin(\pi(n-1)/N)}
 {\sin(\pi(j+n)/N)\sin(\pi(j+n-1)/N)}.
 \tag{12}
\]
To verify it without an orthogonal-polynomial assertion, let
\(G(t)=[(t;Q)_{j+1}(\rho t;Q)_{j+1}]^{-1}\). Then
\[
 (1-t)(1-\rho t)G(t)
 =(1-Q^{j+1}t)(1-\rho Q^{j+1}t)G(Qt).
\]
Its \(t^n\) coefficient, after removing the common phase
\(q^{jn}\), is
\[
 \sin(\pi n/N)P_{n,j}
 =(1+\rho)\sin(\pi(j+n)/N)P_{n-1,j}
 -\rho\sin(\pi(2j+n)/N)P_{n-2,j}.
\]
Dividing by the specified \(\beta\) gives (11).

The \(b_n\), \(1\le n\le r\), are uniformly bounded on (10).
Choose \(\epsilon\) so small that
\[
 z\longmapsto1+\rho-\rho b_n/z
 \tag{13}
\]
maps \(|z-1|\le1/4\) into itself and has Lipschitz constant at
most \(1/3\) there, uniformly in \(n,N\). Induction proves every
ratio \(r_n=p_{n,j}/p_{n-1,j}\) exists, is in that disk, and is
holomorphic in \(\rho\). This proves the asserted zero-freeness,
including the whole coefficient circle needed later. It does not use
positivity at complex \(\rho\).

Here are the phase and amplitude, including the subprincipal term.
Write \(h=1/N\), and use \(s\in[0,\kappa]\) as a real
integration parameter. Uniformly there, (12) has the expansion
\[
 b_n=b(s)+h b_1(s)+O(h^2),\quad s=n/N,
\]
\[
 b(s)=1-\frac{\sin^2(\pi\xi)}{\sin^2(\pi(\xi+s))},
 \qquad
 b_1(s)=-\frac{\pi\sin(\pi\xi)\sin(\pi(2\xi+s))}
                    {\sin^3(\pi(\xi+s))}.
 \tag{14}
\]
There is no singularity at \(s=0\) in these formulas. Let
\[
 R(s)=\frac{1+\rho+
           \sqrt{(1+\rho)^2-4\rho b(s)}}2,
 \qquad
 a(s)=-\frac{\rho b(s)R'(s)+\rho b_1(s)R(s)}
                         {R(s)^2-\rho b(s)}.
 \tag{15}
\]
The square root and logarithms below are their holomorphic branches
at \(\rho=0\); all denominators are units after shrinking
\(\epsilon\). A prime in (15) means \(s\)-derivative, not a
Casimir or meridian derivative.

Substitution into (13) shows that
\(\widetilde r_n=R(nh)+h a(nh)\) has a residual \(O(h^2)\).
Indeed the coefficient of \(h\) is exactly
\[
 a(1-\rho b/R^2)=-\rho bR'/R^2-\rho b_1/R.
\]
At the first step, \(b(0)=0\), \(b_1(0)=-b'(0)\), and
\(a(0)=-R'(0)\). Hence
\(\widetilde r_1=1+\rho+O(h^2)\). The contraction (13) now gives
\(r_n=\widetilde r_n+O(h^2)\) uniformly for every \(n\le r\).
Taking the logarithms fixed at zero and summing yields, by the
ordinary Euler--Maclaurin formula with bounded derivatives,
\[
 \log p_{r,j}
 =N\int_0^\kappa\log R(s)\,ds
 +\tfrac12\log\frac{R(\kappa)}{R(0)}
 +\int_0^\kappa\frac{a(s)}{R(s)}\,ds+O(N^{-1}).
 \tag{16}
\]
Every error just used is holomorphic and uniformly bounded on a
slightly larger disk, so fixed \(\rho\)-derivatives follow by Cauchy.

Put \(c_0=2\pi i\). Applying the same elementary sum formula to
\(\log(Q\rho;Q)_j\) proves
\[
 \boxed{\mathcal L_{T,j}(\rho)
   =e^{N S_L(\rho)}A_L(\rho)(1+O(N^{-1})),}
 \tag{17}
\]
where
\[
 S_L=\int_0^\xi\Log(1-\rho e^{c_0s})\,ds
                         +\int_0^\kappa\log R(s)\,ds,
 \tag{18}
\]
\[
 A_L=
 \sqrt{\frac{1-\rho e^{c_0\xi}}{1-\rho}}
 \sqrt{\frac{R(\kappa)}{R(0)}}
       \exp\int_0^\kappa\frac{a(s)}{R(s)}\,ds.
 \tag{19}
\]
Both square roots equal one at zero. In particular
\(S_L(0)=0,A_L(0)=1\), and \(A_L\) is a holomorphic unit.
Direct differentiation of the integrals gives the useful calibration
\[
 c:=S_L'(0)
  =-\frac{\sin^2(\pi\xi)}{\pi}
                  (\cot(\pi\tau)+i)
  =-\frac{\sin^2(\pi\xi)e^{i\pi\tau}}
                         {\pi\sin(\pi\tau)}\ne0.
 \tag{20}
\]
The exact factor \(x\) remains in \(\rho=xw_1/w_2\); replacing
it by its limit would change a subprincipal term.

## 3. The literal ordinary-binomial dual

The original coherent input on this degree block has components
\[
 c(z)_{a,T-a}=\binom da\binom d{T-a}z_1^az_2^{T-a}.
\]
Its right value leg is therefore exactly
\[
 R_{T,j}(z)=\operatorname{CT}_{u,v}
      L_{T,j}(u,v)(1+z_1/u)^d(1+z_2/v)^d.
 \tag{21}
\]
The two coefficient circles are the original finite dual, with all
indices between zero and \(d\). Homogeneity reduces (21) to
\[
 \boxed{R_{T,j}(z)=z_2^T\binom dT\operatorname{CT}_{\rho}
       \mathcal L_{T,j}(\rho)\mathcal B_T(\eta/\rho),
 \quad \eta=xz_1/z_2,}
 \tag{22}
\]
where
\[
 \mathcal B_T(t)=\binom dT^{-1}
       \sum_{a=0}^T\binom da\binom d{T-a}t^a
 =\binom dT^{-1}[v^T](1+tv)^d(1+v)^d.
 \tag{23}
\]
In particular (22) is not a Hermitian pairing or a reciprocal-monomial
replacement of the coherent input.

For later use, (23) has a uniform holomorphic unit on a full small
\(t\)-disk. Let \(v=v(t)\) be the root near
\(v_0=\tau/(1-\tau)\) of
\[
                  \frac{tv}{1+tv}+\frac{v}{1+v}=\tau,
 \qquad
 D(t)=\frac{tv}{(1+tv)^2}+\frac{v}{(1+v)^2}.
 \tag{24}
\]
Then
\[
 \mathcal B_T(t)=e^{N S_B(t)}A_B(t)(1+O(N^{-1})),
 \tag{25}
\]
\[
 S_B=\log(1+tv)+\log(1+v)-\tau\log v
       +\tau\log\tau+(1-\tau)\log(1-\tau),
\]
\[
 A_B=\frac{\sqrt{\tau/(1-\tau)}}{(1+tv)(1+v)\sqrt{D(t)}}.
 \tag{26}
\]
The branches continue their positive values at zero, and
\(S_B(0)=0,A_B(0)=1,S_B'(0)=b:=\tau/(1-\tau)>0\).

For completeness, this is an actual coefficient estimate. At \(t=0\)
the circle \(v=v_0e^{i\theta}\) has a unique modulus maximum at
\(\theta=0\), with quadratic coefficient
\(D(0)=\tau(1-\tau)>0\). Outside a fixed small arc the binomial
modulus has a uniform exponential gap. For small complex \(t\), use
the circle \(v(t)e^{i\theta}\); its radius and argument change by
a small amount and coefficient extraction is unchanged. The outside
gap persists by continuity on the compact circle. Near zero the
phase is holomorphic, stationary, and has positive real quadratic
part. Taylor expansion, Gaussian integration and the vanishing of
the odd cubic integral give relative \(O(N^{-1})\), uniformly on
a fixed smaller disk. The amplitude \([(1+tv)(1+v)]^{-1}\) is
the exact \(d=N-1\) correction. Dividing by
\[
 \binom dT=\sqrt{\frac{1-\tau}{2\pi N\tau}}
 e^{N[-\tau\log\tau-(1-\tau)\log(1-\tau)]}
 (1+O(N^{-1}))
\]
gives (25)--(26). Zeros of the polynomial on the distant portion
of a circle do not require a logarithm there: the complement bound
uses its actual modulus. This proves the full-disk relative estimate
and zero-freeness, not just a formal saddle equation.

## 4. A selected nonzero saddle for the whole right leg

Fix \(0<\vartheta_0<\pi/2\). Parameterize the small input activity
by
\[
                  \eta=\frac{a^2}{bc},\qquad
             0<|a|<\epsilon_1,\quad|\arg a|<\vartheta_0.
 \tag{27}
\]
Here \(b,c\) are exactly (20),(26). Choose \(\epsilon_1\)
uniformly on the compact parameter set (10). There is a unique
stationary point near \(a/c\),
\[
 \rho_*=(a/c)(1+O(a)),\qquad
 D_\rho\{S_L(\rho)+S_B(\eta/\rho)\}|_{\rho_*}=0,
 \quad D_\rho=\rho\partial_\rho.
 \tag{28}
\]
It is holomorphic in \(a\) through its scaled coordinate
\(c\rho_*/a\). Put
\[
 \Psi=S_L(\rho_*)+S_B(\eta/\rho_*),\qquad
 \mathcal H=D_\rho^2\{S_L(\rho)+S_B(\eta/\rho)\}|_{\rho_*}.
 \tag{29}
\]
Then \(\Psi=2a+O(a^2)\) and \(\mathcal H=2a+O(a^2)\).
On every compact subset of (27), the actual finite right leg obeys
\[
 \boxed{
 R_{T,j}(z)=z_2^T\binom dT
 \frac{e^{N\Psi}A_L(\rho_*)A_B(\eta/\rho_*)}
                   {\sqrt{2\pi N\mathcal H}}
       (1+O(N^{-1})).}
 \tag{30}
\]
The square root is continued from positive real \(a\). The coefficient
in front of this selected Gaussian is exactly \(+1\).

To prove the contour assertion, write \(\rho=(a/c)u\). Uniformly
on a fixed annulus about \(|u|=1\), the phase in (22) is
\(a(u+u^{-1})+O(a^2)\). Divide its stationary equation by \(a\)
and apply the analytic inverse-function theorem near \(u=1\).
Use the permitted original coefficient circle
\(\rho=\rho_*e^{i\theta}\). Both its arguments \(\rho\) and
\(\eta/\rho\) lie in the full disks of (17),(25). Exact
stationarity and bounded second angular derivatives give
\[
 \Re\{S_L(\rho_*e^{i\theta})+
 S_B(\eta e^{-i\theta}/\rho_*)-\Psi\}
 \le-[2\Re a-C|a|^2](1-\cos\theta).
 \tag{31}
\]
Indeed the leading difference is \(2a(\cos\theta-1)\);
the remainder has derivative zero at zero, hence is
\(O(|a|^2\theta^2)\) there, and is \(O(|a|^2)\) on the
rest of the circle. These bounds give the stated global factor
\(1-\cos\theta\). For sufficiently small \(\epsilon_1\), (31)
is a strict gap on every compact subset of (27).

Insert the uniform relative units (17),(25) into the exact integral.
The integral of the error is bounded by \(O(N^{-1})\) times the
same Gaussian scale, using (31). The retained central arc has
quadratic coefficient \(\mathcal H\) with positive real part.
Its Gaussian integral, with measure \(d\theta/(2\pi)\), is
\((2\pi N\mathcal H)^{-1/2}\); its odd cubic term integrates to
zero and the remaining error is relative \(O(N^{-1})\). This proves
(30), including the entire complementary circle. The amplitude is
nonzero, so the actual right leg is nonzero for all sufficiently large
\(N\) on smaller compact subsets. Fixed coherent-variable derivatives
follow by Cauchy on nested complex neighborhoods. The theorem does
not cover a sequence \(a\to0\) without a separate uniform scaling
analysis, although the exact finite leg at \(\eta=0\) is (22).

## 5. Uniform Casimir dependence and both true partner legs

The preceding proof is retained independently. A stronger input from U
now removes its restriction to values at integer channels. Define the
literal polynomial
\[
 \mathsf L_T(\rho;\lambda)=
       \sum_{a=0}^T x^{-a}f_a(\lambda)\rho^a,
 \qquad \sigma_N=(T+1)/N,\quad\tau_N=T/N.
 \tag{32}
\]
Here \(f_a\) is H's actual continuant column, with \(f_0=1\).
Keep \(\sigma_N\) in a fixed compact subinterval of \((0,1)\).
U proves, uniformly for \(\lambda\) in any fixed compact disk,
\[
 \mathsf L_T(\rho;\lambda)
  =e^{N\phi(\rho;\lambda,\sigma_N)}
       \mathcal A(\rho;\lambda,\sigma_N)(1+O(N^{-1}))
 \tag{33}
\]
on a full small \(\rho\)-disk. Its relative error is holomorphic
with fixed \(\rho,\lambda\) derivatives of the same size on smaller
sets. Its phase is calibrated by
\[
 \phi=\frac1{c_0}\int_0^\rho\frac{\log Y(t)}t\,dt,
 \quad (1-\rho)^2(1-Y)(1-e^{-c_0\sigma}Y)
                    +(2-\lambda)\rho=0,\quad Y(0)=1.
 \tag{34}
\]
Its explicit transported amplitude \(\mathcal A\) is U's formula
(5), normalized by \(\mathcal A(0)=1\), including all first-order
quantum shifts. In particular put
\[
 c_\lambda:=\phi_\rho(0;\lambda,\sigma_N)
       =\frac{\lambda-2}{c_0(e^{-c_0\sigma_N}-1)},\qquad
 k_N=\partial_\lambda c_\lambda
       =\frac1{c_0(e^{-c_0\sigma_N}-1)}.
 \tag{35}
\]
The subscript on \(c_\lambda\) denotes its dependence, not a
derivative. These quantities are nonzero on compact Casimir sets
avoiding \(2\), except that no such exclusion is needed for \(k_N\).

Let \(R_T(z;\lambda)=f_T(\lambda)^{\mathsf t}c(z)\).
Equations (21)--(23) remain exact with \(\mathcal L_{T,j}\)
replaced by \(\mathsf L_T\), since they were coefficient identities.
Use the binomial phase and amplitude (24)--(26) with
\(\tau=\tau_N\), and write \(b=\tau_N/(1-\tau_N)\).
On compact Casimir sets avoiding \(2\), set
\[
 \eta=\frac{a^2}{b c_\lambda},\qquad
       0<|a|<\epsilon_2,\quad |\arg a|<\vartheta_0<\pi/2.
 \tag{36}
\]
Replace \(S_L,A_L\) in (28)--(31) by
\(\phi(\cdot;\lambda,\sigma_N),\mathcal A\). Denote the
resulting stationary point, action, Hessian and amplitude by
\[
 \begin{split}
 \widehat\rho_*&=(a/c_\lambda)(1+O(a)),\\
 \widehat\Psi&=\phi(\widehat\rho_*;\lambda,\sigma_N)
                       +S_B(\eta/\widehat\rho_*;\tau_N),\\
 \widehat{\mathcal H}
   &=D_\rho^2\{\phi(\rho;\lambda,\sigma_N)
                     +S_B(\eta/\rho;\tau_N)\}|_{\widehat\rho_*},\\
 \widehat A
   &=\frac{\mathcal A(\widehat\rho_*;\lambda,\sigma_N)
                   A_B(\eta/\widehat\rho_*;\tau_N)}
                    {\sqrt{\widehat{\mathcal H}}}.
 \end{split}\tag{37}
\]
The same exact coefficient-circle proof gives
\[
 \boxed{R_T(z;\lambda)=z_2^T\binom dT
       \frac{e^{N\widehat\Psi}\widehat A}{\sqrt{2\pi N}}
                    (1+O(N^{-1})).}
 \tag{38}
\]
This is uniform and holomorphic on nested complex neighborhoods of
compact subsets of (36), including the Casimir variable. In detail,
U's full-disk estimate supplies (33) on the entire coefficient
circle; \(c_\lambda\) is uniformly bounded away from zero there;
the expansion is again \(a(u+u^{-1})+O(a^2)\) on a fixed annulus.
The inverse-function construction and the global gap (31) are thus
uniform in \(\lambda\). Their actual complementary integral and
relative error estimates apply without any change to the finite caps.

Consequently the actual partner rows have the controlled logarithmic
derivatives
\[
 \boxed{\begin{split}
 \frac{\partial_\lambda L_T(w;\lambda)}{L_T(w;\lambda)}
    &=N\phi_\lambda(\rho;\lambda,\sigma_N)
                    +\partial_\lambda\log\mathcal A+O(N^{-1}),\\
 \frac{\partial_\lambda R_T(z;\lambda)}{R_T(z;\lambda)}
    &=N\partial_\lambda\widehat\Psi
                    +\partial_\lambda\log\widehat A+O(N^{-1}).
 \end{split}}\tag{39}
\]
The first line has \(L_T(w;\lambda)=w_2^T\mathsf L_T(\rho;\lambda)\).
In both lines the physical coherent arguments are held fixed. In
particular the second derivative holds \(\eta=xz_1/z_2\) fixed,
not the auxiliary \(a\). Stationarity gives the exact envelope
identity \(\partial_\lambda\widehat\Psi
=\phi_\lambda(\widehat\rho_*;\lambda,\sigma_N)\).
Locally the branch in (36) varies holomorphically as \(\lambda\)
varies with \(\eta\) fixed. Cauchy differentiation of the relative
error in (33),(38) proves (39); no derivative of a coarse absolute
error or of an integer channel is used.

For sufficiently small nonzero activity these are nontrivial partner
estimates: \(\phi_\lambda=k_N\rho+O(\rho^2)\) and
\(\widehat\Psi_\lambda=(k_N/c_\lambda)a+O(a^2)\) are nonzero.
Thus each partner has a nonzero order-\(N\) leading factor relative
to its value on compact subsets of those punctured charts. At zero
activity the exact partners vanish, and no such assertion is made.
Higher fixed Casimir derivatives follow from the same holomorphic
error control.

At an actual node use \(\lambda_j=2\cos(2\pi j/N+\pi/N)\)
literally in (33)--(39). Their \(\sigma_N=(T+1)/N\) differs from
the \(\tau_N=T/N\) in the binomial dual. Neither shift is dropped.
The older formulas (17)--(20) use their own exact-root, integer-channel
calibration. Equality of the leading characteristic equations alone
does not identify their subprincipal amplitudes with (33).
At a double node H identifies the derivative in (39) with the actual
generic-quantum confluent column. This is still a fixed-root Casimir
derivative, not a meridian or quantum-parameter normal of the source.

## 6. The retained Hermite channel contour and source requirements

The argument sums the physical magnetic coordinate, and (30) also
pays its actual ordinary-binomial dual. It leaves the integer channel
unsummed. On the complete paired chamber the exact reciprocal-monomial
identity has phase \(\nu_j=(-1)^jq^{j(j+1)}\); it is not a reason
to replace (21) by a positive pairing. H's inverse measure itself
contains \(\nu_j\), and its derivative columns remain essential.

More precisely, write \(f_T(\lambda)\) for H's actual continuant
column, and define \(L(\lambda)=v(w)f_T(\lambda)\) and
\(R(\lambda)=f_T(\lambda)^{\mathsf t}c(z)\). For a Casimir
polynomial multiplier \(m\), the exact contribution of a double
node is
\[
 \frac{(mLR)'(\lambda_j)-\eta_jm(\lambda_j)L(\lambda_j)R(\lambda_j)}
      {\sigma_j},
 \tag{40}
\]
and that of a simple node is \(mLR/\sigma_j\). The prime here
is the actual Casimir derivative. H proves its equality with the
specified generic-quantum divided difference, including its source
normalization. Equations (33)--(39) estimate both actual legs and
partners on their stated charts. They do not estimate the sum of
(40) over its physical channels.

There is an exact way to combine all the partners before that
remaining step. Keep H's continuants \(p_a\), characteristic
polynomial \(P_T=p_{T+1}\), and
\(B_T=A_0\cdots A_{T-1}\). Let \(\Gamma_T\) be a union of small
positive circles around the distinct roots of \(P_T\), excluding
the zeros of \(p_T\). Such circles exist: \(p_T\) is nonzero at
every root of \(P_T\), either by H's nonzero inverse normalizers or
by backwards use of the continuant recurrence. For every actual
Casimir polynomial multiplier \(m\),
\[
 \boxed{v(w)m(J_T)c(z)=\frac{B_T^2}{2\pi i}
       \int_{\Gamma_T}\frac{m(\lambda)L(\lambda)R(\lambda)}
                       {P_T(\lambda)p_T(\lambda)}\,d\lambda.}
 \tag{41}
\]
Indeed H gives \(\sigma_j=P_T'(\lambda_j)p_T(\lambda_j)/B_T^2\)
at a simple node. At a double node put
\(Q_j=P_T/(\lambda-\lambda_j)^2\); then
\(\sigma_j=Q_jp_T/B_T^2\) and
\(\eta_j=Q_j'/Q_j+p_T'/p_T\). The residue is exactly (40).
This proves (41), with no lost derivative or additional coefficient.

Equivalently let \(\mathfrak r_T\) denote the polynomial of the
original \(\kappa\)-stripped checked crossing on this block. H's
endpoint calibration, including its derivative, says
\(p_T\equiv B_Tx^T\mathfrak r_T\pmod {P_T}\).
The crossing is invertible, so its inverse in this same finite algebra
gives the alternative exact row
\[
 \frac{B_Tx^{-T}}{2\pi i}\int_{\Gamma_T}
       \frac{m(\lambda)\mathfrak r_T^{-1}(\lambda)
                         L(\lambda)R(\lambda)}{P_T(\lambda)}
                 \,d\lambda.
 \tag{42}
\]
The inverse is the actual polynomial remainder, with its phase and
Hermite jets. Equation (42) removes the extra \(p_T\) poles
algebraically; it does not replace the inverse crossing by a positive
weight. Enlarging (41) instead must retain any \(p_T\) poles it
crosses. No channel-contour deformation or complementary-channel
estimate is asserted by either exact representation.

Every multiplier, inverse measure, original pivot, turnover, and
peripheral line remains where the actual Hermite contraction puts it.
The construction proves no nonzero value for that channel sum or for
the closed opposite-source period. It supplies no uniform meridian or
quantum-parameter normal. Nor is the small activity chart asserted to
contain a specified geometric point. The generic-q and whole-meridian
families must be transported before any such normal is taken.
All asymptotic charts keep the physical total away from its top value:
\(T=d\), where \(e^{-c_0\sigma_N}=1\), is excluded. The exact
identities (4),(21),(40)--(42) still retain that finite block.

## Complete proof directs and coverage

* H: notes/actual_complete_casimir_hermite_packet.md,
  SHA256 a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c.
* C: notes/research_balanced_gauss_cyclic_divisor_source.md,
  SHA256 c15668d7dff95346d72801b721bf95970b661e5b17d125aaadd7e0dc38905b00.
* U: notes/research_actual_jacobi_generating_unit.md,
  SHA256 ab3760dd38817c2345c231d8ef67c8a7fa8bb03e3b26d4ef1de1b87182f6728d.

The complete q-Hahn Fourier coefficient variational theorem,
holomorphic Fourier--Legendre transport, and complete-core complex
packet were read for coverage. Their Fourier polynomial, selected
action chart, and certified complete-image period are different
objects from the ordinary magnetic generating leg and the literal
dual (21). No asymptotic from them is imported here.

Only written mathematics and text/hash operations are used. Frozen
and public files are unchanged.
