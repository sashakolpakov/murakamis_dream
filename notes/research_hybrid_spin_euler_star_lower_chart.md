# A hybrid spin-coherent lower chart for the actual Euler star

Private written proof, 19 November 2026.

The actual finite Euler star has a nonzero ordinary-binomial coherent
kernel near its lower donor row. Physical recipients may range over any
fixed compact set off incidence. Recipients in a factorial gauge are
allowed near their lower coherent row. The latter caps are restored by
exponentially small, relative, finite Cauchy tails. All donor slots and
all physical recipient caps are exact throughout.

This supplies a mixed chart for every resolved lower-donor configuration
whose physical \(K,f\) are units, using a physical recipient when \(p\ne0\)
and a factorial recipient at \(p=0,A=1\). It does not put the rest of a
closed period in this chart. All gauge interfaces, physical crossings,
closing rows, and meridian derivatives remain.

Complete directs G and C are pinned below. G supplies the literal star
and its resolved rational correspondence. C supplies the finite-degree
padding method; the different recurrence, its estimates and graph
identification are proved here.

## 1. Finite operators and the hybrid kernel

Put \(d=N-1, h=N^{-1}, c=2\pi i, Q=e^{ch}\),

\[
 x=-M e^{-ch/2},\qquad f_a=(Q;Q)_a,\qquad
 G_Fw_a=f_aw_a,\qquad 0\le a\le d.                 \tag{1}
\]

The quantum root is fixed when \(M\ne0\) varies. In G's physical basis,

\[
 Lw_a=w_{a-1},\quad Fw_a=(1-Q^{a+1})w_{a+1},\quad
 Kw_a=xQ^{-a}w_a,                                  \tag{2}
\]

with the missing bottom/top arrows. On \(r\ge2\) heads let

\[
 F_{\rm t}=\sum_{j=2}^r K_2^{-1}\cdots K_{j-1}^{-1}F_j,
 \qquad S=\sum_{n=0}^d\frac{(x^{-1}L_1F_{\rm t})^n}{f_n}.
                                                        \tag{3}
\]

For \(S^{-1}\), the summand has the additional multiplier

\[
                         (-1)^nQ^{n(n-1)/2}.             \tag{4}
\]

Choose a subset \(H\subset\{2,\ldots,r\}\). Conjugate both operators
by \(G_F\) on the donor and on precisely the recipients in \(H\):

\[
 \widetilde S^{\pm}=G_H^{-1}S^{\pm1}G_H,\qquad
 G_H=G_{F,1}\prod_{i\in H}G_{F,i}.                        \tag{5}
\]

The donor lowering arrow becomes \(1-Q^a\); a recipient in \(H\)
has unit raising arrow except at its physical top. The other recipients
keep (2). Cartans are unchanged. These are actual finite diagonal
conjugations; the original source uses the inverse changes on its
incident rows and columns.

Use an evaluation row and ordinary binomial column on every head:

\[
 \mathcal K_N^\pm(z,w)=
 \sum_{\alpha,\beta\in\{0,\ldots,d\}^r}
 z^\alpha(\widetilde S^\pm)_{\alpha\beta}
 \prod_i\binom d{\beta_i}w_i^{\beta_i}.
                                                        \tag{6}
\]

Write \(t=w_1, v=tz_1, v_i=z_iw_i, I_i=1+v_i\) for \(i\ge2\).
We work near any fixed compact set of \(M,z_1,z_i,w_i\) on which

\[
 M\ne0,\qquad I_i\ne0,
 \qquad |v_i|\le\rho\quad(i\in H),                       \tag{7}
\]

where, for example, \(0<\rho<1/8\) is sufficient. No size restriction
is imposed on the physical-recipient products \(v_i\), \(i\notin H\).
All assertions are uniform on smaller compacts and sufficiently small
fixed complex \(t\)-disks, independently of \(N\).

First remove only the output caps on the \(H\) recipients. Their unit
raising operators become multiplication by \(z_i\). This defines an
auxiliary finite polynomial: each such output degree is at most \(2d\),
since the total donor transfer is at most \(d\). Physical recipients
retain their exact operator

\[
              F_i^{\rm out}=z_i(1-QT_i),\qquad
              T_i:z_i\longmapsto Qz_i.                  \tag{8}
\]

In particular its apparent degree-\(N\) coefficient is exactly zero.
Every transfer raises recipients. Consequently applying the physical
output projections at the end is exactly the original hybrid kernel;
no path which has crossed a top can return.

## 2. An exact donor-slot evolution

For an artificial donor binomial degree \(0\le j\le d\), keep all
recipient input degrees equal to \(d\). Let

\[
 \mathcal Z=x^{-1}F_{\rm t}^{\rm out},\qquad
 H_a^+(A)=\sum_{n=0}^a{a\brack n}_Q A^n,
 \qquad H_a^-(A)=(A;Q)_a.                               \tag{9}
\]

Then the auxiliary kernel is exactly

\[
 K_j^\pm=\sum_{a=0}^j\binom ja(tz_1)^a
 H_a^\pm(\mathcal Z/z_1)\prod_{i=2}^r I_i^d.             \tag{10}
\]

The expression is polynomial, including at \(z_1=0\). Indeed the
factorial donor arrow supplies \(f_a/f_{a-n}\), and division by \(f_n\)
in (3) gives the finite Gaussian coefficient in (9). Formula (4)
gives the finite Pochhammer polynomial. This proves (10), not just a
principal symbol for it.

Gaussian Pascal and the Pochhammer product give

\[
 H_{a+1}^+(A)=H_a^+(QA)+AH_a^+(A),\qquad
 H_{a+1}^-(A)=(1-Q^aA)H_a^-(A).
\]

Ordinary binomial Pascal therefore gives the two literal evolutions

\[
 \begin{split}
 K_{j+1}^+&=K_j^++tz_1K_j^+(Qt,Q^{-1}z_1)
                                      +t\mathcal ZK_j^+,\\
 K_{j+1}^-&=(1+tz_1)K_j^-
                                      -t\mathcal ZK_j^-(Qt,z_1).
 \end{split}                                             \tag{11}
\]

All recipient arguments not displayed are unchanged. These identities
also hold with the actual capped recipient operators. We use the
uncapped \(H\) version first for the relative cap estimate below.

Normalize

\[
             G_j^\pm=K_j^\pm/
                   \bigl[(1+v)^j\prod_{i=2}^r I_i^d\bigr]. \tag{12}
\]

Thus \(G_0=1\) and \(G_j(t=0)=1\). For \(I\subset\{2,\ldots,r\}\),
put

\[
 B_{I,h}=\prod_{i\in I}
       \left(\frac{1+Qv_i}{1+v_i}\right)^{h^{-1}-1}.
                                                        \tag{13}
\]

This has a holomorphic germ at \(h=0\), using the logarithm of each
ratio which is zero there. The germ is an analytic device for the
coefficients, not an off-root finite-matrix assertion.

Index terms by \(\nu=(j,e)\), where \(2\le j\le r\), \(e=0\), and
also \(e=1\) if \(j\notin H\). Define

\[
 I_\nu=\{2,\ldots,j-1\}\cup\bigl(\{j\}\text{ if }e=1\bigr),
 \quad a_{\nu,h}=(-1)^eQ^ex^{-(j-1)}z_jB_{I_\nu,h},
 \quad Y_\nu=c\sum_{i\in I_\nu}z_i\partial_{z_i}.
                                                        \tag{14}
\]

Let \(D=t\partial_t, Y_0=c(D-z_1\partial_{z_1})\),
\(\theta=v/(1+v)\), and

\[
 R_h(\tau,v)=
 \exp\left\{\frac\tau h\log\frac{1+Qv}{1+v}\right\}.
                                                        \tag{15}
\]

With \(\tau=jh\), (11) becomes

\[
 \begin{split}
 G_{j+1}^+&=G_j^++\theta(e^{hY_0}G_j^+-G_j^+)
       +\frac t{1+v}\sum_\nu a_{\nu,h}e^{hY_\nu}G_j^+,\\
 G_{j+1}^-&=G_j^--\frac t{1+v}R_h(\tau,v)
                  \sum_\nu a_{\nu,h}e^{h(cD+Y_\nu)}G_j^-.
 \end{split}                                             \tag{16}
\]

Every shifted spatial term has an explicit factor \(t\). This is the
finite-degree fact which permits arbitrary compact physical-recipient
products. In particular no unit-time clock orbit is required to stay
off incidence.

## 3. Low-degree logarithms and the complete finite tail

We give the analytic estimate, including its finite-tail recovery.
Work on a buffered polydisk about a point of (7), then use a finite
cover. Set \(V_j=h\log G_j\) as a formal series in \(t\), with zero
constant coefficient. The exact recurrence is

\[
 V_{j+1}=V_j+h\mathcal F_h^\pm(\tau,V_j),                 \tag{17}
\]

where

\[
 \begin{split}
 \mathcal F_h^+(\tau,V)&=\log\left[1+
 \theta\left(e^{(e^{hY_0}-1)V/h}-1\right)
 +\frac t{1+v}\sum_\nu a_{\nu,h}
                       e^{(e^{hY_\nu}-1)V/h}\right],\\
 \mathcal F_h^-(\tau,V)&=\log\left[1-
 \frac t{1+v}R_h(\tau,v)\sum_\nu a_{\nu,h}
                    e^{(e^{h(cD+Y_\nu)}-1)V/h}\right].
 \end{split}                                             \tag{18}
\]

For the coefficient of \(t^n\), the multiplier of \([t^n]V_j\)
in (17) is exactly one. All other terms use strictly lower activity
degrees. The logarithms in (18) are their branches at one.

Collapse absolute spatial Taylor coefficients to a positive variable

\[
 y,\qquad \mathcal L=C(1+y)^2\partial_y,
\]

increasing \(C\) to majorize all the finitely many vector fields in
(14),(16), including their displacements at the center. Let \(\phi_s\)
be its positive flow. For positive series

\[
 (e^{h\mathcal L}-1)U/h\preceq
                         e^{h\mathcal L}\mathcal LU.     \tag{19}
\]

If activity coefficient \(k\) is bounded at \(\phi_{kh}(y)\), one
additional clock shift or divided difference is bounded at
\(\phi_{(k+1)h}(y)\), with at most \(Ck+\mathcal L\) applied to its
majorant. A shifted coefficient in (18) contributes only to output
degree at least \(k+1\). In products every shifted factor has this
same property, so positivity moves every argument to the common
\(\phi_{nh}(y)\) at output degree \(n\). This proves the padding
rule term by term for the full exponentials and logarithm.

The coefficients \(a_{\nu,h},R_h\) and their fixed derivatives are
uniformly bounded on buffered neighborhoods, for \(0\le\tau\le1\)
and small \(h\). Their absolute Taylor series and (18) are majorized
by a positive analytic function of the form

\[
 \mathcal H(t,y,p,q)=
             \frac{C(y)t}{1-C(y)(t+p+q)},\qquad
 C(y)=C/(1-y/R),\quad p=DU,\quad q=\mathcal LU.           \tag{20}
\]

The term with \(\theta\) is included because \(\theta=O(t)\).
Consider \(U_\tau=\mathcal H(t,y,DU,\mathcal LU)\), \(U(0)=0\).
This has an analytic solution on fixed small \(t,y\) disks through
time two. To see this directly, write its right side as

\[
 H(t,y,p,q),\qquad p=DU,\quad q=U_y.
\]

The characteristic equations are

\[
 \dot t=-tH_p,\quad\dot y=-H_q,\quad
 \dot p=tH_t,\quad\dot q=H_y,\quad
 \dot U=H-pH_p-qH_q.                                    \tag{21}
\]

At \(t=0\) all momenta and \(U\) remain zero and the coordinates
remain fixed. On a small polydisk their deviations for time two are
bounded by \(C(|t|+|p|+|q|+|U|)\). Picard iteration and Gronwall keep
them \(O(|t(0)|)\); the initial-to-final coordinate map is identity
at \(t=0\) and hence invertible on a smaller polydisk. Differentiating
the equations gives \(p=DU,q=U_y\). This constructs the analytic
solution. Its Taylor coefficients are nonnegative, by positive
coefficient Picard iteration and continuation.

The positive time-\(h\) flow dominates one positive Euler step. Using
(19),(20) in the exact coefficient recursion, induction therefore
bounds \(V_j\) by \(U(2jh,t,\phi_{nh}(y))\) at activity degree \(n\).
We use this only for \(n\le L=\lfloor\delta N\rfloor\). Choose
\(\delta>0\) so that all padding by \(nh\le\delta\) stays in the
buffered incidence complement. Cauchy's estimate then gives

\[
             |[t^n]V_j|\le C_1R_1^{-n},
       \quad 1\le n\le L,\quad 0\le j\le d.             \tag{22}
\]

All fixed spatial and meridian derivatives obey the same estimate
on smaller buffered sets. Repeated background ratios in (13)
telescope to the corresponding bounded small-arc displacement;
the proof uses degree padding, not a bound on an unrestricted
length-\(N\) clock path.

The actual whole polynomial has a separate elementary bound

\[
                    |G_j|\le e^{C_2N}.                   \tag{23}
\]

Here and below a polynomial factor in \(N\) is absorbed in a slightly
larger constant. Indeed \({a\brack n}_Q\) is a sum of
\(\binom an\) unit phases, so its absolute value is at most that
integer. In a fixed compact coordinate set, each term of the output
tail operator has coefficient bounded independently of \(N\): a raw
raising coefficient has modulus at most two, a gauged one is one,
and the Cartan phases have modulus one apart from fixed powers of

\[
 |x|^{\pm1}.
\]

Thus its \(n\)-th power has coefficients bounded by \(C^n\), including
the finitely many ordered choices. In (10), \(a\le j\le d\), input
recipient binomial sums have total absolute coefficients \(2^{(r-1)d}\),
and every output degree is at most \(2d\). Evaluation on a fixed
compact and division by (12) cost at most another \(e^{CN}\).
The inverse's multiplier (4) is a unit phase. This proves (23) for
both signs and for every artificial slot number. No \(N^{CN}\)
norm bound for a gauged raising operator is used.

Let \(V_j^{[L]}\) be the Taylor polynomial through degree \(L\).
On a circle \(|t|=R_2<R_1\), (22) bounds it by \(C_3R_2\).
The functions \(G_j\) and \(\exp(V_j^{[L]}/h)\) have identical Taylor
coefficients through degree \(L\). For \(|t|\le\eta R_2\),

\[
 |G_j-e^{V_j^{[L]}/h}|
 \le\frac{2\eta^{L+1}}{1-\eta}e^{N(C_2+C_3R_2)}.         \tag{24}
\]

The comparison exponential has modulus at least
\(e^{-C_3N\eta R_2}\). Choose \(\eta>0\) after all the constants
so that its power in (24) pays this entire bound. Then

\[
                 G_j=e^{V_j^{[L]}/h}(1+O(e^{-\gamma N})). \tag{25}
\]

This proves zero-freeness of the actual auxiliary polynomial and
recovers all its finite high activity degrees.

## 4. Explicit phase and unit transport

Set \(t_i=v_i/(1+v_i)\). The limiting coefficients in (14) and their
first corrections are

\[
 a_{\nu,0}=(-1)^e(-M)^{-(j-1)}z_j
                 e^{c\sum_{i\in I_\nu}t_i},
\]
\[
 b_\nu=ec+(j-1)c/2+
       \sum_{i\in I_\nu}\{-ct_i+c^2t_i(1-t_i)/2\},
 \qquad a_{\nu,h}=a_{\nu,0}(1+hb_\nu+O(h^2)).            \tag{26}
\]

Also

\[
 R_h(\tau,v)=e^{c\tau\theta}
          [1+h\tau c^2\theta(1-\theta)/2+O(h^2)].        \tag{27}
\]

Define \(V^\pm(0)=0\) by

\[
 V_\tau^\pm=\log Z_\pm(V),                              \tag{28}
\]
\[
 \begin{split}
 Z_+(V)&=1+\theta(e^{Y_0V}-1)
           +\frac t{1+v}\sum_\nu a_{\nu,0}e^{Y_\nu V},\\
 Z_-(V)&=1-\frac t{1+v}e^{c\tau\theta}
                     \sum_\nu a_{\nu,0}e^{(cD+Y_\nu)V}.
 \end{split}
\]

The same characteristic proof as (21) gives a unique analytic solution
through time one on smaller fixed neighborhoods. All characteristic
velocities vanish at \(t=0\); the initial projection is identity.
The branch is fixed by \(V(\tau,0)=0\).

For clarity the complete first correction is specified. Let

\[
 \begin{split}
 F_{1,+}(V)=Z_+^{-1}\{&\tfrac12\theta e^{Y_0V}Y_0^2V
 +\tfrac t{1+v}\sum_\nu a_{\nu,0}e^{Y_\nu V}
                         (b_\nu+Y_\nu^2V/2)\},\\
 F_{1,-}(V)=-Z_-^{-1}\tfrac t{1+v}e^{c\tau\theta}
 \sum_\nu a_{\nu,0}e^{(cD+Y_\nu)V}
 \{&b_\nu+\tau c^2\theta(1-\theta)/2
                         +(cD+Y_\nu)^2V/2\}.
 \end{split}                                             \tag{29}
\]

With \(\mathcal F_\pm(V)=\log Z_\pm(V)\), solve the linear analytic
transport

\[
 A_\tau^\pm=d\mathcal F_\pm[V^\pm]A^\pm
                  +F_{1,\pm}(V^\pm)-\tfrac12V_{\tau\tau}^\pm,
 \qquad A^\pm(0)=0.                                    \tag{30}
\]

This includes the Cartan half-step, the recipient degree \(d=N-1\),
and the time dependence of the inverse. The linear characteristic
solution is analytic and is zero at \(t=0\).

To justify comparison, put \(W_j=V(jh)+hA(jh)\). Taylor expansion of
(18),(26),(27) gives

\[
 W_{j+1}-W_j-h\mathcal F_h(jh,W_j)=O(h^3),               \tag{31}
\]

with an analytic residual \(O(t)\). The low-degree error obeys the
same padding rule. The derivative of the right side of (18) has a
positive majorant \(B_1(t,y)De+B_2(t,y)\mathcal Le\), with both

\[
                         B_i(t,y)=O(t).
\]

Indeed every divided difference in (18) has its explicit activity
factor. The positive linear flow with this right side and an analytic
forcing \(B_0(t,y)=O(t)\) exists through time two by (21). Comparing
the coefficient recursion with it bounds \([t^n](V_j-W_j)\) by

\[
                    h^2 C R^{-n},\qquad n\le L.          \tag{32}
\]

The argument is the positive Euler-step induction used for (22), now
with residual \(h^3B_0\). This pays discrete stability as well as
consistency. Summing (32), using the analytic tails of \(V,A\), and
then (25), proves

\[
 G_d^\pm=e^{NV^\pm(1)}a_\pm(1+O(N^{-1})),\qquad
 a_\pm=\exp\{A^\pm(1)-V_\tau^\pm(1)\}\ne0.             \tag{33}
\]

The term \(-V_\tau(1)\) is the final donor slot \(d/N=1-h\).
At \(t=0\), \(V=A=V_\tau=0\), so \(a_\pm=1\).

## 5. Restoring every hybrid cap

For each \(i\in H\), mark its output variable by \(z_i\mapsto\xi_i z_i\).
Choose \(R>1\) with \(R\rho<1\) and

\[
 g=\log R-\log\frac{1+R\rho}{1-\rho}>0.                 \tag{34}
\]

For example \(R=2,\rho<1/8\) works. Prove (33) on the compact union
of all such marker circles, with the other physical recipient products
unchanged. They all remain off incidence. The normalized phase and
transport are respectively \(O(t)\) and a bounded unit there.

For a nonempty subset \(J\subset H\), Cauchy's formula for the sum
of coefficients of degree at least \(N\) in each corresponding marker
gives the factor

\[
                   R^{-N|J|}(1-R^{-1})^{-|J|}.           \tag{35}
\]

Compared with the unmarked kernel, the background factors cost at most

\[
 \left(\frac{1+R\rho}{1-\rho}\right)^{d|J|},
\]

and the ratio of the phase/transport factors costs at most
\(C e^{CN|t|}\). The donor background is unchanged. Thus every such
tail is \(O(e^{-gN|J|+CN|t|})\) relative to the unmarked auxiliary
kernel. Shrink the donor disk after (34). Inclusion--exclusion of the
finitely many output projections gives

\[
             \mathcal K_N^\pm/K_d^\pm=1+O(e^{-\gamma_1N}). \tag{36}
\]

This is the original hybrid finite kernel by the monotonicity argument
after (8). Unrelated physical recipient phases have not been replaced
by absolute majorants in this relative comparison.

Combining (12),(33),(36) proves the theorem:

\[
 \boxed{\quad\mathcal K_N^\pm
 =(1+tz_1)^d\prod_{i=2}^rI_i^d\,
 e^{NV^\pm(1)}a_\pm(1+O(N^{-1})).\quad}                 \tag{37}
\]

It is zero-free on the stated fixed open chart for all sufficiently
large \(N\). The relative remainder is holomorphic and \(O(N^{-1})\)
on a buffered chart. Cauchy therefore gives the same bound for all
fixed derivatives in coherent variables and in the actual fixed-root
meridian \(M\). In particular this is a genuine meridian family of
(3),(5), not a derivative of a root-only identification of \(E(M)\).
No complex-\(q\) zero-free domain is asserted.

## 6. The actual mixed principal graph and resolved lower row

The full phase in (37) is

\[
 \mathfrak F_\pm=\log(1+tz_1)+\sum_{i=2}^r\log I_i+V^\pm(1).
                                                        \tag{38}
\]

Its full amplitude is \(a_\pm/[(1+tz_1)\prod I_i]\), so the literal
identity endpoint remains \(I_i^{N-1}\). Define occupations

\[
 u_i=w_i\mathfrak F_{w_i},\quad
 u_i'=z_i\mathfrak F_{z_i},\quad
 A_i=e^{cu_i},\quad A_i'=e^{cu_i'}.                       \tag{39}
\]

In a physical recipient chart the input/output coordinate dictionaries
are

\[
 p_i=w_i(1-u_i)/u_i,\quad f_i=(1-A_i)/p_i;
 \qquad p_i'=z_i^{-1},\quad f_i'=z_i(1-A_i').             \tag{40}
\]

For the donor and a factorial recipient they are

\[
 f_i=u_i/[w_i(1-u_i)],\quad p_i=(1-A_i)/f_i;
 \qquad f_i'=z_i,\quad p_i'=(1-A_i')/z_i.                \tag{41}
\]

The displayed ratios are taken by their analytic limits at a lower
row. These formulas follow directly from the binomial coefficient
ratio \(\binom d{a-1}/\binom da=a/(N-a)\) and the literal arrows,
or from the mixed symplectic form: in either chart

\[
 d\log A\wedge d\log p=c\,du\wedge d\log w,
 \quad d\log A'\wedge d\log p'=-c\,du'\wedge d\log z.
\]

We identify the graph by an exact donor contiguity. Gaussian Pascal
applied to each donor coefficient, including its binomial ratio,
gives at degree \(d\)

\[
 \begin{split}
 \partial_tK_d^+&=(d-D)
       \{z_1K_d^+(Qt,Q^{-1}z_1)+x^{-1}F_{\rm t}^{\rm out}K_d^+\},\\
 \partial_tK_d^-&=(d-D)
       \{z_1K_d^--x^{-1}F_{\rm t}^{\rm out}K_d^-(Qt,z_1)\}.
 \end{split}                                             \tag{42}
\]

These hold for actual caps as well; for the auxiliary kernels (8)
gives their ordinary shift form. The relative cap estimate permits
the same principal equations for (37). Using (39)--(41) gives

\[
 f_1=z_1 A_1/A_1'+F_{\rm t}'/x_{\rm cl}\quad(+),\qquad
 f_1=z_1-A_1F_{\rm t}'/x_{\rm cl}\quad(-),                \tag{43}
\]

where \(x_{\rm cl}=-M\), and

\[
 F_{\rm t}'=\sum_{j=2}^r x_{\rm cl}^{-(j-2)}
                 \left(\prod_{2\le i<j}A_i'\right)f_j'.
\]

For the first equation use \(f_1=\mathfrak F_t/(1-t\mathfrak F_t)\).
The factor \(d-D\) in (42) gives its denominator; omitting it would
give the wrong ordinary-binomial graph.

G's rational positive star has \(C=1-p_1F_{\rm t}/x_{\rm cl}\),
preserves the tail \(F\), and satisfies \(A_1/A_1'=C\) and

\[
 f_1=C f_1'+F_{\rm t}/x_{\rm cl}.
\]

Its inverse gives the second equation of (43). Thus the literal
contiguity agrees with G on the regular resolved correspondence.
At \(t=0\) the initial phase is exactly

\[
                      \mathfrak F_\pm=\sum_{i=2}^r\log I_i.\tag{44}
\]

Near that row (43) is an analytic first-order equation for
\(\mathfrak F_t\): every occurrence of that derivative on the other
side through \(A_1\) or its denominator has a factor \(t\). Its
implicit derivative at \(t=0\) is one. Hence successive Taylor
coefficients in \(t\) determine its analytic solution uniquely.

The mixed projection of G's map is regular there. With a nonzero
donor \(f_1\), its input spin coordinate is

\[
 w_1=\frac{\Log A_1/c}{f_1(1-\Log A_1/c)}
                       =-p_1/c+O(p_1^2).                \tag{45}
\]

Recipients are unchanged at \(p_1=0\). At fixed nonzero output \(z_i\),
the input changes are \(w_i=p_i u_i/(1-u_i)\) in (40), or
\(w_i=u_i/[z_i(1-u_i)]\) in (41); their derivatives in \(u_i\) are
units away from \(u_i=1\). All G's \(C,T_j\) equal one at this row.
The inverse function theorem and G's symplectic identity therefore
give its local mixed generating function, normalized by (44).
It satisfies (43); uniqueness identifies it with (38).

In particular the mixed Hessian at the row is triangular: its donor
diagonal entry is one, its recipient entries are \(I_i^{-2}\), and
its recipient-input/donor-output entries vanish. It is nondegenerate
on a smaller chart. The result is an actual generating kernel, not
only a nonzero scalar function.

At completeness a resolved lower donor has \(p_1=0,A_1=1,f_1\ne0\).
For a physical recipient with \(p_i\ne0,A_i\ne1\), choose a retained
logarithm \(u_i=\Log A_i/c\ne1\) and set

\[
 z_i=1/p_i=f_i/(1-A_i),\qquad w_i=p_i u_i/(1-u_i).
                                                        \tag{46}
\]

Then \(I_i=1/(1-u_i)\ne0\), without any modulus restriction on \(A_i\).
For a resolved recipient \(p_i=0,A_i=1,f_i\ne0\), choose the lower
logarithm and its factorial gauge:

\[
                  z_i=f_i,\qquad w_i=0.                 \tag{47}
\]

It belongs to (7), and \(p_i\sim-cw_i\) there. These coordinate
choices cover all such resolved lower-donor configurations. They do
not reset an independently prescribed nonlower logarithmic mark at
an endpoint, and they do not make a generic nonlower donor small.

## 7. Retained source scope

Every statement concerns the literal finite star (3) with the hybrid
conjugations (5) and ordinary binomial columns (6). Returning to a
physical braid network retains each actual \(G_F^{\pm1}\) interface;
no uniform conditioning for those separate factors is asserted.
The original κ, diagonal generator, physical crossing, framing and
pivotal/first-jet source factors are not part of (37) and remain
explicit. A source-preserving presentation may place its star on a
covered lower row, but that separate presentation theorem does not
follow from this local estimate.

The theorem does not construct the full coherent integration chain,
control its complement or its closing row, interpolate occupation
blocks, or prove a geometric contribution or closed invariant lower
bound. It supplies a uniform actual finite factor and its fixed-root
meridian family where the stated mixed chart applies.

## Complete proof-source pins

* G: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.
* C: notes/research_actual_coupled_euler_coherent_flow.md,
  SHA256 a7d3d29f4381f669fd3f6e72a6c637fa259e650757bd39a517e47c0419692def.

Both complete directs were freshly read nontruncated in this active
author sequence. The entire matching final was read back, every used
implication checked, and all three hashes renewed before freezing.
Only written mathematics and text/hash operations were used.
Frozen and public files were unchanged.
