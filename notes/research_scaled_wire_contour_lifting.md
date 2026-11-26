# Lifting a two-variable contour estimate to an arbitrary vertex degree

The wire variables around one original filled vertex are independent
once its trace angle is fixed. This gives an exact reduction of the
exponential estimates to a scaled two-variable phase. It does not
remove the contour corrections. Rather, a specified list of
two-variable inequalities controls every combination of those
corrections, with their original weights.

The order of the contour identities matters. We first write the exact
trace contour and then expand each wire sum pointwise on that contour.
This avoids an interior simultaneous-height homotopy whose mixed
endpoint terms would need stronger estimates.

## 1. The original source and the scaled phase

Fix a degree \(d\ge1\), a positive integer power \(n\), and the
original source
\[
 P_{d,n,N}(\mathbf u)=\phi_N^{(t)}
       \left[R^n\prod_{j=1}^dK_N(t,u_j)\right],
 \qquad K_N(t,u)=\sum_{k=0}^{N-1}e_k(-2\cos t)e_k(-2\cos u).
 \tag{1}
\]
The degree and power are fixed before \(N\to\infty\).
Negative powers follow by coefficient conjugation once the
positive-power statement is proved. The particular contour
construction below assumes a selected wire height \(h_x>0\);
it does not cover zero power merely by setting \(n=0\).

Choose \(0<\alpha<\beta<1/2\), a real angular cutoff
\(0<T<\pi\), and heights
\[
                         h_t>2\pi h_x>0.
 \tag{2}
\]
Retain wire indices \(k/N\in[\alpha,\beta]\), with half-grid
endpoints \(\alpha_N,\beta_N\), and trace angles
\(|\tau|<T_N\), where \(T_N\ge T\) is a physical midpoint
and \(T_N-T=O(N^{-1})\).

Let \(B_N(x,t)\) be the exact canonical Newton interpolation.
At \(x=k/N\) it is the original \(e_k(-2\cos t)\). Its phase
is the continued factorial phase \(b(x,t)\), with the branches
specified in
[the three-crossing phase note](research_terminal_three_central_phase.md),
Section 1. Define
\[
\begin{split}
 F(x,t)&=b(x,t)+b(x,0),\\
 C_n(t)&=\frac{in}{4\pi}t^2-it,\\
 \Psi_{d,n}(x,t)&=dF(x,t)+C_n(t),\\
 \mathcal F_{d,n}(\mathbf x,t)&=\sum_{j=1}^dF(x_j,t)+C_n(t).
\end{split}
 \tag{3}
\]
On each specified side of every factorial cut these functions
have the literal identity
\[
                  \mathcal F_{d,n}(\mathbf x,t)
                       =\frac1d\sum_{j=1}^d\Psi_{d,n}(x_j,t).
 \tag{4}
\]
If the \(j\)-th wire weight has exponential penalty \(p_j\ge0\),
the corresponding real rate is exactly
\[
 \Re\mathcal F_{d,n}-\sum_jp_j
       =\frac1d\sum_j\{\Re\Psi_{d,n}(x_j,t)-dp_j\}.
 \tag{5}
\]
The factor \(d\) multiplying each wire penalty is essential.
The unit trace charge \(-it\) is already in \(C_n\), once
in (4); it must not be added separately for each wire.

## 2. The two-dimensional hypotheses

Assume there is a selected critical point
\[
                x_*=\xi_*+ih_x,\qquad t_*=\tau_*-ih_t,
 \qquad \alpha<\xi_*<\beta,\quad 0<\tau_*<T,
 \tag{6}
\]
of the *unexponentiated* phase \(\Psi_{d,n}\). Let
\(M=\Re\Psi_{d,n}(x_*,t_*)\). Choose a closed real rectangle
\(Q\) strictly inside \((\alpha,\beta)\times(0,T)\) containing
\((\xi_*,\tau_*)\).

The following inequalities are sufficient. Every phase uses
the factorial branch on the displayed surface. Each indicated
strict gap is a positive fixed number.

1. On \(x=\xi+ih_x,\ t=\tau-ih_t\), for
   \(\alpha\le\xi\le\beta,\ 0\le\tau\le T\), the real phase
   is at most \(M\), with equality only at (6). It has a
   strict gap outside \(Q\), and its real Hessian is negative
   definite throughout \(Q\).
2. On the same upper wire with \(-T\le\tau\le0\), the real
   phase has a strict gap below \(M\).
3. On \(x=\xi-ih_x,\ t=\tau-ih_t\), \(|\tau|\le T\),
   \[
                 \Re\Psi_{d,n}(x,t)-2\pi d h_x<M-\delta_L.
   \tag{7}
   \]
4. For either wire endpoint \(e=\alpha,\beta\), all
   \(-h_x\le y\le h_x\), and \(|\tau|\le T\),
   \[
    \Re\Psi_{d,n}(e+iy,\tau-ih_t)
                      -2\pi d\max(-y,0)<M-\delta_E.
   \tag{8}
   \]
5. On the angular cutoff connectors, for each \(\sigma=\pm1\),
   \(0\le s\le1\), and \(\alpha\le\xi\le\beta\),
   \[
   \begin{split}
    \Re\Psi_{d,n}(\xi+ih_xs,\sigma T-ih_ts)&<M-\delta_A,\\
    \Re\Psi_{d,n}(\xi-ih_xs,\sigma T-ih_ts)
                       -2\pi d h_xs&<M-\delta_A.
   \end{split}
   \tag{9}
   \]
6. On every nested wire endpoint in an angular connector,
   \(e=\alpha,\beta\), \(\sigma,\epsilon=\pm1\), and
   \(0\le s,v\le1\),
   \[
    \Re\Psi_{d,n}(e+\epsilon ih_xvs,\sigma T-ih_ts)
       -2\pi d h_xvs\,\mathbf1_{\epsilon=-1}
                                      <M-\delta_{AE}.
   \tag{10}
   \]

It is enough to certify negative Hessian on \(Q\), exact
stationarity in its interior and a strict bound outside it
in condition 1; strict concavity then supplies its unique
maximum. No concavity assertion is needed outside \(Q\).

These are two-real-variable domains. In particular, (10)
has independent parameters \(s,v\); checking just its corners
or the diagonal \(s=v\) would be insufficient. Conversely,
we do not require a bound on
\[
 x=e+ih_xs,\qquad t=\tau-ih_ts,\qquad
                      |\tau|<T,\quad 0<s<1.
 \tag{11}
\]
That interior simultaneous-height family is absent from
the exact decomposition used below.

## 3. Finite-source hypotheses that remain separate

The limiting phase inequalities must be accompanied by the
following established kinds of finite estimate.

* The original complete Hermite norm of a wire outside the
  chosen interval has rate at most \(E_w\), whereas an
  unrestricted wire has rate at most \(M_\infty=4G/\pi\).
  Require
  \[
                         (d-1)M_\infty+E_w<M.
  \tag{12}
  \]
  For a symmetric interval \([\alpha,1/2-\alpha]\), the
  standard bound is \(E_w=2g(\alpha)\), with
  \(g(x)=J(2x)-4J(x)\); the high-index bound is included.
* The retained polynomial obeys, uniformly for every real
  outside angle,
  \[
   |K_{N,I}(t,u)|\le CN^A e^{NE_T}\quad(T\le|t|\le\pi),
                         \qquad dE_T<M.
   \tag{13}
  \]
  Its first normal is bounded on a fixed outer spectral
  interval at polynomial cost. A bound for the full kernel
  alone may not be assigned to the retained subset.
* The exact factorial interpolation is holomorphic on all
  rectangles used in the one-sided wire identities, with
  the uniform upper bounds on the selected factorial sides.
  Near (6) the exact local product has the bulk expansion
  \[
   B_N(x,t)B_N(x,u)=
      \frac{e^{N\{b(x,t)+b(x,u)\}}}
           {4N^2\sin^2(\pi x)}(1+O(N^{-1})).
   \tag{14}
  \]
  The chosen branches in this expansion agree with (3).

These hypotheses are verifiable with the original
[uniform factorial and boundary-decay bounds](research_uniform_factorial_and_boundary_decay.md).
For example, (2) keeps \(1/2-x+t/(2\pi)\) on its lower
side and \(1/2-x-t/(2\pi)\) on its upper side throughout
each nested rectangle. The parents near \(u=0\) stay in
their fixed holomorphic charts. The phase certificate
must still use those literal sides when a real part is
negative or zero.

## 4. The exact decomposition generates only the listed surfaces

The retained integrand before the trace is the full product
\[
 f_N(t,\mathbf u)=
       \prod_{j=1}^d\sum_{k/N\in I}
                    B_N(k/N,t)B_N(k/N,u_j).
 \tag{15}
\]
It is even in \(t\). Apply the exact original midpoint trace
first, with \(g_N(t)=\sin t\,f_N(t,\mathbf u)e^{inNt^2/(4\pi)}\):
\[
\begin{split}
 \mathcal D_{n,N}^{T_N}f_N={}&
 -\frac{N^2C_{N,n}}{\pi i}
 \int_{-T_N-ih_t}^{T_N-ih_t}
  g_N(t)\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt\\
 &+\frac{\eta N^2C_{N,n}}{\pi}
 \int_{-h_t}^{h_t}
       \frac{g_N(T_N+iy)}{4\cosh^2(Ny/2)}\,dy,
 \quad \eta=(-1)^{N-1}.
\end{split}
 \tag{16}
\]
The carrier is \(C_{N,n}=e^{\pi i n(N-1)^2/(4N)}\).
No normal or charge has been removed.

On the lower horizontal trace contour, apply the exact
[one-sided wire formula](research_terminal_one_sided_wire_formula.md)
separately to every sum in (15), always at height \(h_x\).
For each wire this gives:

| Wire term | Point | Exponential penalty |
|---|---|---|
| upper main | \(x=\xi+ih_x\) | \(0\) |
| upper correction | \(x=\xi+ih_x\) | \(2\pi h_x\) |
| lower correction | \(x=\xi-ih_x\) | \(2\pi h_x\) |
| endpoint current | \(x=e+iy,\ |y|\le h_x\) | \(2\pi\max(-y,0)\) |

The two endpoint signs and their oriented differentials remain
in the identity. The correction weights are the full rational
functions \(E_\pm/(1-E_\pm)\). Their absolute bounds retain
all higher wire charges.

On the angular endpoint current, use oddness to fold its
two halves to
\[
                      t=\pm T_N-ih_ts,\qquad 0\le s\le1.
 \tag{17}
\]
Its exact weight has exponential bound \(e^{-Nh_ts}\),
which is precisely the unit-charge contribution in \(C_n(t)\).
For \(s\ge1/N\), expand each wire at height \(h_xs\).
The table becomes the same table with \(h_x\) replaced
by \(h_xs\); each endpoint has its own independent
parameter \(y_j=\epsilon_jh_xv_js\), \(0\le v_j\le1\).
The denominators obey
\[
                  1-e^{-2\pi Nh_xs}\ge1-e^{-2\pi h_x}>0.
 \tag{18}
\]
Thus products of the wire identities have uniformly bounded
rational denominators at this stage. Their number is finite
for fixed \(d\), and no dimension-dependent exponential
factor in \(N\) is introduced.

For \(0\le s\le1/N\), keep the entire product (15)
unexpanded. Equation (13) and interval
Bernstein--Walsh continuation give the rate
\[
                         dE_T+O_d(N^{-1/2})
 \tag{19}
\]
on this collar. The crossing chirp has modulus \(e^{O_n(1)}\),
and the other trace factors cost only a polynomial.
The collar is strictly below \(M\). This avoids a spurious
product of \(1/s\) bounds at zero height.

This construction is an exact sequence of one-variable
identities with the other variables held fixed. It never
moves the interior of the angular horizontal contour
through smaller heights while expanding wire endpoints.
Therefore it produces (7)--(10), but no surface (11).

## 5. Why the two-dimensional bounds control every mixed term

On the bottom angular contour every main upper wire has
scaled rate at most \(M\). A lower wire satisfies (7);
an endpoint satisfies (8). An upper correction has the
same phase as a main upper wire and the additional
scaled loss \(2\pi d h_x\).

Consequently (5) bounds every product containing a
nonprincipal wire term strictly below \(M\). If a single
wire is known to have scaled gap \(\delta\), while the
others have scaled rate at most \(M\), the full gap is
at least \(\delta/d\). The independent endpoint-height
parameters cause no problem: (8) holds for each of them
at the same fixed trace angle.

For the all-main product with negative real trace angle,
every wire has the negative-angle gap from condition 2,
so the full gap is that gap, not divided by \(d\).
On the positive main region equality with \(M\) requires
every pair \((x_j,t)\) to equal the unique point (6).
Thus the full main phase has its unique maximum at
\((x_*,\ldots,x_*,t_*)\). Outside the lifted local region
where every \((\Re x_j,\Re t)\) belongs to \(Q\), at
least one wire has the certified main gap. Again (5)
gives a full gap at least its \(1/d\) fraction.

On an angular connector every wire, whether main,
corrected or an independently partially raised endpoint,
satisfies (9) or (10). All therefore have a strict
scaled gap; their average has a strict gap as well.
The shared angular weight has been counted exactly once.

The angular rational factor on the bottom contour obeys
\[
 \frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}
                         =e^{-iNt}(1+O(e^{-Nh_t})).
 \tag{20}
\]
The estimates above first bound its complete wire product.
Its nonleading angular charges then have the extra
fixed loss \(h_t\). This retains all charges together.

Finally (12) removes the original wire tails before the
trace, and (13) removes the outer real trace nodes with
their first normals. There are only polynomially many
original wire assignments for fixed \(d\), and all trace
costs at a fixed \(n\) are polynomial. Half-grid shifts
of size \(O(N^{-1})\) preserve smaller strict gaps by
uniform continuity of the prescribed real phases,
including at the moving factorial zeros.

## 6. Hessian reduction and the exact leading coefficient

At the diagonal saddle write
\[
 a=F_{xx}(x_*,t_*),\qquad b=F_{xt}(x_*,t_*),\qquad
 c=dF_{tt}(x_*,t_*)+\frac{in}{2\pi}.
\]
The full complex Hessian and the scaled Hessian are
\[
 H_{\rm full}=
 \begin{pmatrix}aI_d&b\mathbf1\\b\mathbf1^T&c\end{pmatrix},
 \qquad
 H_{\rm sc}=\begin{pmatrix}da&db\\db&c\end{pmatrix}.
 \tag{21}
\]
An orthogonal change in the wire coordinates separates
\(d-1\) transverse modes with coefficient \(a\) and the
collective block
\(\begin{psmallmatrix}a&\sqrt d\,b\\\sqrt d\,b&c\end{psmallmatrix}\).
The latter is positively congruent to \(H_{\rm sc}\).
It follows that the real Hessian of the full phase is
negative definite exactly when the real Hessian of the
scaled phase is negative definite. Also
\[
             \det(-H_{\rm full})
                  =\frac{(-a)^{d-1}}d\det(-H_{\rm sc}).
 \tag{22}
\]
These assertions are at the diagonal point. On the lifted
local region, where the wire coordinates need not agree,
the quadratic form is instead the exact average
\[
 \Re D^2\mathcal F[(\mathbf v,w)]^2
    =\frac1d\sum_j
         \Re D^2\Psi_{d,n}(x_j,t)[(v_j,w)]^2.
 \tag{23}
\]
Negative definiteness of the scaled Hessian throughout
\(Q\) therefore implies negative definiteness throughout
this lifted region as well.

Near the saddle, insert (14) for each wire. The trace
contributes \(-N^2C_{N,n}/(\pi i)\); the \(d\) upper
wire integrals each contribute \(N\), with no factor
\(1/2\); their Newton products contribute \(N^{-2d}4^{-d}\).
The Gaussian dimension is \(d+1\). Thus the total power is
\[
                       N^{2+d-2d-(d+1)/2}
                              =N^{-3(d-1)/2}.
 \tag{24}
\]
At zero outside boundary its nonzero coefficient is
\[
 A(0)=
 \frac{i(2\pi)^{(d+1)/2}}{\pi4^d}\,
 \frac{\sin t_*}
 {\sin^{2d}(\pi x_*)\sqrt{\det(-H_{\rm full})}}.
 \tag{25}
\]
All roots are the Gaussian branches on the accretive
quadratic form. Equation (22) may be used to evaluate
(25) from the scaled two-dimensional Hessian; it does
not change the power of \(N\).

## 7. The resulting whole-boundary implication

**Lifting theorem.** Under the explicit hypotheses in
Sections 1--3, the original source (1) has
\[
 P_{d,n,N}(\mathbf u)=C_{N,n}N^{-3(d-1)/2}
      A(\mathbf u)e^{NS(\mathbf u)}(1+O(N^{-1}))
 \tag{26}
\]
on a fixed complex polydisk, through both parities.
Its amplitude is holomorphic and nonzero. The phase
is the selected critical value of
\[
 \sum_{j=1}^d\{b(x_j,t)+b(x_j,u_j)\}
                          +\frac{int^2}{4\pi}-it.
 \tag{27}
\]
At zero boundary the coefficient is (25).

Indeed all nonlocal terms have the proved strict gaps.
The selected saddle is nondegenerate by (21)--(23), so
it continues holomorphically in the separate boundary
variables. Their phases perturb every compact contour
by a uniformly small amount. The parent factorials stay
in their original charts near zero, and the original
tail polynomials have separate degree at most \(N-1\);
their strict gaps persist on a sufficiently small
polydisk. Local holomorphic stationary phase proves
(26) with its nonzero coefficient.

Separate evenness gives zero first variations of the
critical coordinates at \(\mathbf u=0\), and
\[
             S_{u_ju_k}(0)
                  =-\delta_{jk}\frac{\tan(\pi x_*)}{2\pi}.
 \tag{28}
\]
If \(\Re\tan(\pi x_*)>0\), this has negative real part.
The uniform exact parent-factorial estimate also supplies
on every wire contour the loss
\[
 -\gamma\sum_{j=1}^d(1-\cos u_j),\qquad
 \gamma=\min_{\alpha\le\xi\le\beta}
           \frac{\sin(2\pi\xi)}{4\pi\cosh^2(\pi h_x)}>0.
 \tag{29}
\]
The discarded original terms have fixed gaps, so reducing
the angular coefficient absorbs them on the full real
torus. Combining this with (28) and separate-degree
Chebyshev continuation away from the complete point
gives the usual full Gaussian strip bound.
This proves a source theorem, not merely a local saddle
formula.

## 8. The homotopy that would need stronger hypotheses

The preceding proof should not be reused for an arbitrary
simultaneous deformation of all heights. If regular wires
were allowed at
\[
 x=\xi+ih_xs,\qquad t=\tau-ih_ts,\qquad
 |\tau|<T,\quad 0<s<1,
\]
their scaled phase need not be at most \(M\). At \(s=0\),
\(\xi=1/4,\tau=0\), it is \(dM_\infty\), which exceeds
the selected positive-filling rate whenever the filling
has positive action loss.

For such a different deformation, an endpoint estimate
\(L_{\rm bad}<M-\delta\) would not suffice beside
\(d-1\) regular factors whose envelope is \(U_{\rm reg}>M\).
One would need the simultaneous bound
\[
           L_{\rm bad}(s,\tau)
               +(d-1)U_{\rm reg}(s,\tau)<dM,
 \tag{30}
\]
and corresponding bounds with multiple bad wires.
Equation (4) alone cannot prove these inequalities.
The trace-first nested identity avoids these interior
mixed-height surfaces and hence does not require (30).

For \(d=2,\ 3\le n\le31\), the nineteen required
two-dimensional inequalities, local Hessian and finite
tail comparisons have now been verified in
[the degree-two filling theorem](research_all_nonzero_degree_two_fillings.md).
That application uses \([1/32,15/32]\), already used
for the degree-two two-crossing theorem. The narrower
terminal interval does not automatically preserve the
degree-two wire-tail gap. The lifting theorem itself
does not assert these inequalities at other degrees
or powers.
