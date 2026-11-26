# Crossing transport by the full kernel difference operator

Research note, 3 November 2026.

The original kernel difference operator admits an exact Gaussian
conjugation that has no physical-window endpoint current. The reason
is specific to its coefficients: the coefficient of the shift that
leaves the physical window vanishes to order three. This is enough
to preserve both values and first normals, including at even levels.
The conjugated operator is bounded on every fixed complex angular
strip by a constant independent of the level.

At an uncontracted boundary the kernel still has its original
Chebyshev defect. We retain that term explicitly. These identities
give a coherent integration-by-parts rule with arbitrary spectators;
they do not prove a nonzero geometric contribution to an arbitrary
rational-word source.

The Askey--Wilson operator and its quantum trace interpretation are
known structures. The starting finite identity, its normalization,
and the classical recurrence references are in
[the full kernel difference note](research_edge_kernel_difference_and_endpoint_bound.md).
The quantum character algebra is already recorded in
[the Newton crossing note](actual_newton_twist_canonical_graph.md).
The issue treated here is the analytic realization on the original
Gaussian source, with all endpoint and free-boundary data retained.

## 1. The operator in the physical angle

Fix \(N\ge2\), and put
\[
 \theta=\pi/N,\quad q=e^{i\theta},\quad D=N-1,\quad
 \eta=(-1)^D,\quad c_0=2\cos\theta,\quad
 P_N(z)=2T_N(z/2)+2.
 \tag{1}
\]
The original algebra is \(\mathcal A_N=\mathbb C[z]/(P_N)\).
Its Newton basis, trace, and turn are
\[
 e_j(z)=\frac{\prod_{r<j}(2\cos((2r+1)\theta)-z)}
                   {\prod_{r=1}^{j}4\sin^2(r\theta)},\quad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f,\quad
 T e_j=e_{D-j}.
 \tag{2}
\]
Write \(z(t)=-2\cos t\). An angular polynomial means an even
\(2\pi\)-periodic trigonometric polynomial, equivalently a polynomial
in \(z(t)\). Define
\[
 \begin{split}
 A_N(t)&=\frac{4\cos^4((t-\theta)/2)}
                       {\sin t\,\sin(t-\theta)},\\
 C_N(t)&=A_N(-t)
       =\frac{4\cos^4((t+\theta)/2)}
                       {\sin t\,\sin(t+\theta)},\\
 (\mathcal L f)(t)
   &=(c_0+A_N(t)+C_N(t))f(t)
       -A_N(t)f(t-2\theta)-C_N(t)f(t+2\theta).
 \end{split}
 \tag{3}
\]
The notation \(C_N(t)\) here is a difference coefficient, not the
scalar in the crossing Gaussian. Apparent poles in combined
expressions are removed by continuation. In the Newton basis,
\[
 \mathcal L e_0=c_0e_0,\qquad
 \mathcal L e_j=c_je_j-4\sin^2(j\theta)e_{j-1}.
 \tag{4}
\]
Consequently, in the full quotient,
\[
                   \mathcal L=T\,m_z\,T.
 \tag{5}
\]
Here \(m_z\) denotes multiplication by \(z\). Both \(m_z\) and \(T\)
are self-adjoint for the original bilinear pairing
\(\phi_N(fg)\), so \(\mathcal L\) is also self-adjoint.
No positive inner product is asserted.

## 2. Exact Gaussian conjugation

For an integer \(n\), define
\[
 \boxed{\begin{split}
 (\mathcal L_n f)(t)
  ={}&(c_0+A_N(t)+C_N(t))f(t)\\
   &-q^n A_N(t)e^{-int}f(t-2\theta)
    -q^n C_N(t)e^{int}f(t+2\theta).
 \end{split}}
 \tag{6}
\]
All powers of \(q\) use the fixed logarithm \(i\pi/N\).

**Theorem 1.** The operator \(\mathcal L_n\) maps angular
polynomials to angular polynomials and preserves the ideal
\((P_N(z(t)))\). In the original full quotient it is exactly
\[
                        \mathcal L_n=R^{-n}\mathcal L R^n.
 \tag{7}
\]
Thus (7) includes every required first normal and holds at both
parities. If the input has Fourier degree \(r\), the output has
degree at most \(r+|n|\).

*Proof.* Under \(t\mapsto-t\), the two shifted terms in (6)
exchange. The expression is even and periodic. Its possible
finite Laurent poles are at
\(t=0,\pi,\pm\theta,\pi\pm\theta\), modulo \(2\pi\).
At \(t=\theta\), the pole of \(A_N\) cancels because
\[
 q^n e^{-in\theta}=1,\qquad f(\theta)=f(-\theta).
 \tag{8}
\]
The cancellation at \(-\theta\) is the same. At zero the
residues of \(A_N\) and \(C_N\) are opposite and the shifted
values agree. At \(\pi\) the same argument uses periodic
evenness and \(e^{in\pi}=e^{-in\pi}\).
At \(\pi\pm\theta\) the relevant coefficient has a cubic zero.
Hence there is no finite Laurent pole. The orders at zero
and infinity in \(e^{it}\) give the stated degree bound.
The same removability argument applies to any even periodic
function holomorphic on a strip.

The physical relation is shift invariant:
\[
 P_N(z(t+2\theta))=P_N(z(t-2\theta))=P_N(z(t)).
 \tag{9}
\]
Therefore \(\mathcal L_n(P_N f)=P_N\mathcal L_n f\),
which proves ideal preservation.

Let \(r_n(t)\) be the canonical polynomial of \(R^n\).
Its original Gaussian representative is
\[
 g_n(t)=\mathfrak c_{N,n}
                \exp\!\left(\frac{inNt^2}{4\pi}\right),\qquad
 \mathfrak c_{N,n}=\exp\!\left(\frac{\pi i nD^2}{4N}\right).
 \tag{10}
\]
It has exactly the values and first normals of \(r_n\) at
the physical angles
\[
                  \tau_j=\pi-(2j+1)\theta.
 \tag{11}
\]
The scalar \(\mathfrak c_{N,n}\) is the original one; it
cancels from the following conjugation. Direct calculation gives
\[
             g_n(t\pm2\theta)/g_n(t)=q^n e^{\pm int},
 \qquad \mathcal L(g_n f)=g_n\mathcal L_n f.
 \tag{12}
\]

It remains to justify replacing \(r_n\) by \(g_n\) under the
operator, rather than just at ordinary distinct roots.
Away from its coalescing coefficient poles, \(\mathcal L\)
uses neighboring physical values and first normals, so their
agreement suffices. There are three exceptional configurations.

At the even-level middle angle \(t=\theta\), put
\(H(t)=(r_n(t)-g_n(t))f(t)\). It is even and
\(H(\theta+\delta)=O(\delta^2)\). Hence
\[
 H(\theta+\delta)-H(-\theta+\delta)
   =H(\theta+\delta)-H(\theta-\delta)=O(\delta^3).
 \tag{13}
\]
The simple pole of \(A_N\) leaves an \(O(\delta^2)\)
remainder. This preserves the first spectral normal as well
as the value. The point \(-\theta\) is identical.

At the odd-level middle angle zero only the simple spectral
value is required. The function \(H\) is even, vanishes at
zero, and vanishes to order two at the neighboring double
angles \(\pm2\theta\). The opposite poles of \(A_N,C_N\)
therefore leave a vanishing combined value.

Finally, at \(t=\pi-\theta\), the term that reaches outside
the Gaussian window is multiplied by \(C_N(t)\), which
vanishes to order three. Its value and first derivative are
zero regardless of the off-window mismatch. The other end
uses the cubic zero of \(A_N\). For \(N=2\) a middle point
and an endpoint coincide; the simple-pole cancellation in
(13) and the cubic-zero argument concern different terms
and apply together.

It follows that \(\mathcal L(r_n f)\) and
\(g_n\mathcal L_n f\) have the same full physical data.
Replace \(g_n\) by \(r_n\) once more in their product data.
Since \(R\) is invertible in the original algebra, this proves
(7). \(\square\)

The theorem concerns the full original representative, not a
semisimple replacement of the repeated roots. It is precisely the
cubic endpoint zeros that distinguish (6) from an unweighted
Gaussian translation, whose signed Ward current need not vanish.

## 3. A fixed-strip bound with no level-dependent loss

For \(h>0\), let \(\|f\|_h\) be the supremum of an even
periodic function on \(|\Im t|\le h\), assuming it is
holomorphic on a neighborhood of that closed strip.

**Proposition 2.** For every fixed integer \(n\),
\[
 \|\mathcal L_n f\|_h\le
 \left[
 2+\frac{8\cosh^4(h/2)}{\sinh^2h}
                      (1+e^{|n|h})
 \right]\|f\|_h.
 \tag{14}
\]
The constant is independent of \(N\). A fixed finite composition
of such operators has the product of these constants and preserves
the same strip.

*Proof.* On either boundary \(\Im t=\pm h\),
\[
 |A_N(t)|,\ |C_N(t)|
       \le \frac{4\cosh^4(h/2)}{\sinh^2h},
 \qquad |q^ne^{\pm int}|\le e^{|n|h}.
 \tag{15}
\]
The shifts are real, so they stay on the same strip.
Equation (14) follows on its two boundary circles.
The removable-pole argument in Theorem 1 makes
\(\mathcal L_n f\) holomorphic throughout the periodic
cylinder. Its maximum principle proves the bound inside.
\(\square\)

This bound is for the conjugated operator. It does not assert a
uniform strip bound for the canonical crossing polynomial itself.
In particular it does not conflict with its nontrivial band-edge
Fourier coefficients.

## 4. The exact Green identity and the surviving source line

Self-adjointness in (5) and Theorem 1 give, for arbitrary
polynomial spectators \(f,g\),
\[
 \boxed{\displaystyle
 \phi_N(R^n f\,\mathcal L g)
          =\phi_N(R^n(\mathcal L_n f)\,g).}
 \tag{16}
\]
Spectators may have coefficients in the untraced boundary
polynomial ring. All mixed boundary normals and all products
of incident kernels are retained. In particular
\[
       \phi_N\!\left(R^n(\mathcal L_n-c_0)f\right)=0.
 \tag{17}
\]
This is a finite, coherent identity. It never takes absolute
values of separate spectral colors.

In the pulled-back residue formula, the detailed-balance relation is
\[
 \sin t\,A_N(t)
           =\sin(t-2\theta)\,C_N(t-2\theta).
 \tag{18}
\]
Thus (16) is also the integration-by-parts identity obtained by
translating the two weighted residue terms. The cubic zeros remove
the physical endpoint residues. The two internal coefficient poles
at \(\pm\theta\) must still be grouped before continuation; their
removability was proved in (8) and (13). The statement does not
license deforming separated singular terms while omitting their
residues.

There is an exact description of its range:
\[
 \begin{split}
 \ker(\mathcal L_n-c_0)&=\mathbb C R^{-n},\\
 \operatorname{im}(\mathcal L_n-c_0)
             &=\{f\in\mathcal A_N:\phi_N(R^n f)=0\}.
 \end{split}
 \tag{19}
\]
Indeed conjugation by \(TR^n\) reduces the operator to
multiplication by \(z-c_0\). Its image consists of classes
vanishing at \(c_0\), while
\[
                  (TR^n f)(c_0)=\phi_N(R^n f).
 \tag{20}
\]
Its kernel is the line spanned by \(e_D\), which the inverse
conjugation takes to \(R^{-n}\). Since \(c_0\) is a double
root even when \(N=2\), this kernel line lies in the image:
\(\phi_N(1)=0\). This retains the endpoint Jordan normal;
it is not a positive spectral projection.

Equations (14), (17), and (19) do not give a bounded right
inverse on that image. Such an estimate, on a useful deformed
cycle, would be an additional result. Nor does (19) estimate
the surviving one-dimensional quotient.

There is nevertheless an explicit moderate-growth primitive
for the kernel vector. Let \(G_N\) be the original canonical
sine factorial, \(g_N=\log G_N\), and put
\[
 \ell_N(t)=\frac D2-\frac{t}{2\theta},\qquad
 \widetilde Q_N(t)=-
       \frac{g_N'(\ell_N(t))-g_N'(0)}{2\theta\sin\theta}.
 \tag{21a}
\]
The logarithmic derivative has its exact finite expression
\[
       g_N'(x)=\frac{\pi}{N^2}
           \sum_{r=0}^{D}(x-r)\cot\frac{\pi(x-r)}N.
 \tag{21b}
\]
The removable summands are interpreted by continuity.
The [logarithmic Ward calculation](research_odd_ward_logarithmic_factorial.md)
shows that \(\widetilde Q_N\) is even and holomorphic on
\(|\Re t|<\pi+\theta\), and has the full physical jets of
\[
                         Q_N(z)=\partial_zK_N(c_0,z).
 \tag{21c}
\]
For every fixed height \(h\), it satisfies
\[
 \sup_{\substack{|\Re t|\le\pi\\|\Im t|\le h}}
       |\widetilde Q_N(t)|\le C_h N^2(1+\log N).
 \tag{21d}
\]
In addition to the equality of jets, it solves the exact
meromorphic difference equation
\[
                 (\mathcal L-c_0)\widetilde Q_N=1.
 \tag{21e}
\]
Indeed, the factorial recurrence gives
\(g_N'(x+1)-g_N'(x)=\theta\cot((x+1)\theta)\).
In the index coordinate \(x=\ell_N(t)\), substitution into
(3) reduces (21e) to the elementary identity
\[
 A(x)\cot((x+1)\theta)-C(x)\cot(x\theta)
       =\frac{2\{\sin^2((x+1)\theta)-\sin^2(x\theta)\}}
                    {\sin((2x+1)\theta)}
       =2\sin\theta.
 \tag{21f}
\]
Here \(A(x),C(x)\) are the same coefficients as (3) in the
index coordinate. The identity is meromorphic before any
physical specialization.

Thus the endpoint Jordan primitive has an explicit
logarithmic-factorial representative on the entire original
window. Conjugating (21e) by the Gaussian gives
\[
 (\mathcal L_n-c_0)(g_n^{-1}\widetilde Q_N)=g_n^{-1}.
 \tag{21g}
\]
This identity retains its actual Gaussian carrier. It is not
a periodic-strip estimate for \(g_n^{-1}\), nor a solution
operator for arbitrary right-hand sides. The poles and period
defect of \(\widetilde Q_N\) outside the original window remain
those explicitly listed in the logarithmic Ward note.

## 5. The ordinary free-boundary defect

Define the canonical turn on an arbitrary polynomial \(f\) by
\[
 (\mathscr T_N f)(w)
      =\phi_N^{(z)}[f(z)K_N(z,w)],\qquad
 K_N(z,w)=\sum_{j=0}^{D}e_j(z)e_j(w).
 \tag{21}
\]
This is the ordinary degree-at-most-\(D\) representative of
\(T[f]\), not just its class at the free variable \(w\).
The full kernel identity and self-adjointness give
\[
 w\mathscr T_N f
     =\mathscr T_N(\mathcal L f)
                  +\frac{\eta}{N^2}P_N(w)f(c_0).
 \tag{22}
\]
Here we used
\(\phi_N(f e_D)=f(c_0)\), which follows from
\((z-c_0)e_D=0\) in the quotient and \(\phi_N(e_D)=1\).
Consequently the exact crossed-source identity is
\[
 \boxed{\displaystyle
 w\mathscr T_N(R^n f)
   =\mathscr T_N(R^n\mathcal L_n f)
           +\frac{\eta\kappa^n}{N^2}P_N(w)f(c_0),\qquad
 \kappa=q^{D^2/2}.}
 \tag{23}
\]
The last term is a polynomial in the actual free variable.
It may be removed only after that variable is contracted in
the full original algebra. In particular the identity remains
valid with arbitrary other boundary variables and their mixed
derivatives, without claiming that the displayed defect is small.

For completeness put \(V_n=\mathcal L_n1\). These are explicit
polynomials with
\[
 V_0=c_0,\quad V_1=4q-q^2z,\qquad
 V_{n+1}+qzV_n+q^2V_{n-1}=8q
                 \quad(n\in\mathbb Z).
 \tag{24}
\]
To verify the recurrence in (24), use (6) and
\[
                   c_0+A_N+C_N=\frac8{c_0+z(t)}.
 \tag{25}
\]
The apparent denominator cancels after multiplication by
\(1+qz+q^2=q(c_0+z)\). For example
\[
 V_{-1}=4q^{-1}-q^{-2}z,\qquad
 V_2=q^3(z^2-1)-4q^2z+7q.
 \tag{26}
\]
The same recurrence holds for the operators \(\mathcal L_n\),
with \(z\) acting on their output and \(8q\) replaced by \(8qI\).
This is the established quantum trace recurrence in the explicit
physical-angle realization (6).

The exact terminal polynomial \(H_{n,N}=\mathscr T_N(R^n)\)
therefore satisfies the forced equation
\[
 \boxed{\displaystyle
       [\,w-V_n(\mathcal L_w)\,]H_{n,N}(w)
                =\frac{\eta\kappa^n}{N^2}P_N(w).}
 \tag{27}
\]
The equality
\(\mathscr T_N(zf)=\mathcal L_w\mathscr T_N f\)
used here is an ordinary polynomial identity: the kernel
defect is then in the traced variable and vanishes exactly.

## 6. Transport through an arbitrary fixed rational word

There is a useful operator consequence that does not require a
concentrated packet at every intermediate turn. Write \(Z=m_z\).
In the original algebra the three operators \(Z,\mathcal L,\mathcal L_1\)
obey
\[
 \begin{array}{lll}
 T ZT=\mathcal L,&T\mathcal LT=Z,&
 T\mathcal L_1T=\mathcal L_{-1},\\
 R^{-n}ZR^n=Z,&R^{-n}\mathcal LR^n=\mathcal L_n,&
 R^{-n}\mathcal L_1R^n=\mathcal L_{n+1}.
 \end{array}
 \tag{28}
\]
The first two turn identities follow from \(T^2=1\).
For the third use the original braid
\(TRT=\kappa R^{-1}TR^{-1}\) and its inverse; the two
scalar factors cancel. The crossing identities are conjugation.
Finally (24) expresses every \(\mathcal L_n\), including
negative \(n\), as a noncommutative polynomial in
\(Z,\mathcal L,\mathcal L_1\), with coefficients that are
Laurent polynomials in \(q\).

It follows that every fixed word \(W\) in the actual turns and
signed crossings has an explicitly transported cap operator
\[
                \mathcal D_{W,N}=W\mathcal LW^{-1}-c_0
 \tag{29}
\]
in the quotient. Use the substitutions (28), with the crossing
sign reversed when forming \(R^n(\cdot)R^{-n}\), to give
(29) a polynomial expression in those three generators.
Interpret this chosen expression on angular analytic functions
using (3), (6), and multiplication by \(z(t)\).
For every fixed \(h>0\) there is then a constant \(C_{W,h}\),
independent of \(N\), such that
\[
                    \|\mathcal D_{W,N}f\|_h
                                \le C_{W,h}\|f\|_h.
 \tag{30}
\]
This follows from (14), \(\|Z\|_h\le2\cosh h\), and the
finite polynomial expression. It applies to every fixed
rational word, including consecutive short turns.
The quotient character identities themselves are the existing
ones cited at the start of this note; (30) is their bounded
physical-angle realization.

Let \(F_{W,N}\) be the original canonical boundary polynomial
of \(W1\), with all carrier scalars retained. Since
\(\mathcal L1=c_0\), the ordinary polynomial identity is
\[
                \mathcal D_{W,N}F_{W,N}
                              =P_N E_{W,N}.
 \tag{31}
\]
The correction \(E_{W,N}\) is obtained by ordinary polynomial
division after applying the chosen operator expression. There
is an integer \(r_W\), independent of \(N\), bounding that
expression's degree increase, and hence
\(\deg E_{W,N}\le r_W-1\) whenever it is nonzero.
The coefficients of \(E_{W,N}\) have not been bounded here.
Equation (31) retains an actual finite-dimensional boundary
forcing rather than declaring the source homogeneous off
the physical spectrum. With other uncontracted polynomial
variables present, the same reasoning is coefficientwise.

This is operator closure. It is not closure of concentrated
states under turns: the exact example \(T(H_p)=R^p\) still
precludes the latter.

## 7. An exponential inverse cost in the original terminal source

The bounded operators cannot be inverted with subexponential
cost merely from their strip bounds. This can be proved within
the actual source, already for \(n=2\).

Set
\[
                     \mathscr D_{2,N}=z-V_2(\mathcal L).
 \tag{32}
\]
The operator \(\mathcal L\) preserves polynomial degree.
Therefore \(\mathscr D_{2,N}\) raises the degree of every
nonzero polynomial by exactly one and is injective on
polynomials. Equation (27) uniquely specifies its polynomial
solution to the forcing
\[
       \mathscr D_{2,N}H_{2,N}
                    =\eta\kappa^2 P_N/N^2.
 \tag{33}
\]
The original
[power-two terminal theorem](research_two_crossing_terminal_filling.md)
gives a nonzero leading coefficient and exponential rate
\(M_2=M_\infty/2>0\) at \(t=0\).
Thus \(|H_{2,N}(-2)|\ge c e^{NM_2}\) for sufficiently large
\(N\), with a fixed \(c>0\).
On the other hand the exact angular Chebyshev identity gives
\[
 \|P_N(-2\cos t)\|_h\le 2+2\cosh(Nh)\le4e^{Nh}.
 \tag{34}
\]
For any fixed \(0<h<M_2\), the inverse on the polynomial
image consequently satisfies
\[
 \|\mathscr D_{2,N}^{-1}\|_h
        \ge \frac c4\,N^2 e^{N(M_2-h)}.
 \tag{35}
\]
The same lower bound applies to any proposed solution
operator that returns this actual polynomial solution.
It is not inferred from a numerical condition number.

Thus the new transport rule removes a particular endpoint
current, but a controlled inverse or geometric cycle-selection
argument must handle genuine exponential behavior. A fixed
strip norm of the coefficients does not select the geometric
solution.

## 8. Scope

The weighted shift gives an exact source-level way to move a
crossing through a difference operator without a physical endpoint
Ward remainder. It preserves a fixed analytic strip, every original
normal, and arbitrary attached polynomial sources. Its remaining
free-boundary forcing is explicit.

This does not establish a simultaneous geometric kernel
representative on a proposed large contour. Inverting
\(\mathcal L_n-c_0\), or selecting the surviving solution of
(27), still requires control of the original cycle. The exponential
cancellation in the negative-two terminal example in
[the all-color note](research_all_color_path_normal_bound.md)
continues to apply. Thus no arbitrary adjacent-component
volume theorem is inferred from the identities above.

## 9. Reproduction

[The independent finite checker](../experiments/check_current_free_aw_crossing_transport.py)
compares (6) with the original crossing and Newton matrices,
using unreduced Fourier reconstruction of the left side.
It checks values and first normals at every physical root,
the ordinary free-boundary correction (23), the terminal
forcing (27), and the logarithmic Green primitive.
Both level parities and signed powers are included.

The saved
[100-digit output](../repro/results/research-current-free-aw-crossing-transport.json)
records the source hash and dependency hashes. These finite
comparisons test signs, normalization, and confluent data;
the all-level statements are proved above.
The [150-digit replay](../repro/results/research-current-free-aw-crossing-transport-root.json)
checks the same 63 level-power cases, 1,120 physical values and
normals, and nine levels for the logarithmic Green primitive.
Chebyshev polynomials and their derivatives are evaluated by their
finite recurrence, avoiding a hypergeometric evaluator at the
coalescing endpoint.

## 10. A closed recurrence for the original charge observations

The Green identity also gives an equation in the Fourier charge,
with a fixed number of neighboring charges. This is an equation for
the actual finite source, including its free color. It is not
obtained by discarding the free-boundary term in (23).

For every integer \(k\), put
\[
 Z_{k,N}^{(n)}(w)=
 \phi_N^{(z)}\!\left[R(z)^nK_N(z,w)T_k(-z/2)\right],
 \qquad T_{-k}=T_k .
 \tag{36}
\]
Thus \(Z_{-k,N}^{(n)}=Z_{k,N}^{(n)}\). The small-charge
variable is \(\chi=1-k/N\); in particular the uninserted
source occurs at \(k=0\). All equalities below are ordinary
polynomial identities in the free variable \(w\).

Define four finite trigonometric polynomials:
\[
 \begin{split}
 d_N(t)&=\sin(t-\theta)\sin(t+\theta)
                    \sin(t-2\theta)\sin(t+2\theta),\\
 a_N(t)&=4(\cos\theta+\cos t)
                    \sin(t-2\theta)\sin(t+2\theta),\\
 b_N(t)&=4\cos^4((t-\theta)/2)
                    \sin(t-3\theta)\sin(t-4\theta),\\
 a_N(t)&=\sum_{s=-3}^{3}a_s e^{ist},\qquad
 d_N(t)=\sum_{s=-4}^{4}d_s e^{ist},\qquad
 b_N(t)=\sum_{s=-4}^{4}b_s e^{ist}.
 \end{split}
 \tag{37}
\]
The letters \(a_N,b_N,d_N\) in this section denote these
displayed polynomials only. In particular \(b_N\) is not a
Fourier coefficient of a crossing. Extend \(a_s\) by zero
for \(|s|=4\).

**Theorem 4.** For every \(N\ge2\), every fixed integer \(n\),
every integer \(k\), and every free \(w\),
\[
 \boxed{\begin{split}
 0={}&\sum_{s=-4}^{4}(a_s-wd_s)Z_{k+s,N}^{(n)}(w)\\
 &-q^n\sum_{r=-4}^{4}b_r
       \left(q^{-2k}Z_{k+r-n,N}^{(n)}(w)
                    +q^{2k}Z_{k-r+n,N}^{(n)}(w)\right).
 \end{split}}
 \tag{38}
\]
This equation retains the original normal data at both level
parities. It also holds after any fixed number of derivatives
in the free color, by differentiating the whole displayed
identity.

If \(n\ne0\), set \(R=|n|+4\) and \(\sigma=\operatorname{sgn}n\).
The coefficients of its two extreme terms are
\[
 [Z_{k+R}]\,(38)=\frac{q^{\,n+\sigma(2k+9)}}{16},
 \qquad
 [Z_{k-R}]\,(38)=\frac{q^{\,n+\sigma(9-2k)}}{16}.
 \tag{39}
\]
Both have modulus \(1/16\). In particular a window of \(2R\)
consecutive original observations determines all subsequent
and preceding observations. No division by a coefficient that
vanishes at a physical color or a special charge is needed.

*Proof.* Apply (16) to the kernel and an arbitrary angular
polynomial \(h\). The full kernel equation, with its original
free defect, gives
\[
 \phi_N\!\left[R^nK_N(z,w)(\mathcal L_n-w)h\right]
       =-\frac{\eta\kappa^n}{N^2}P_N(w)h(c_0).
 \tag{40}
\]
Indeed \((\mathcal L_z-w)K_N(z,w)
=-\eta P_N(w)e_D(z)/N^2\) and
\(\phi_N(R^ne_Dh)=\kappa^nh(c_0)\).
Choose \(h(t)=d_N(t)\cos kt\).
At the endpoint \(t=\pi-\theta\), the factor
\(\sin(t+\theta)\) vanishes, so \(h(c_0)=0\).
Thus the right side of (40) is exactly zero, even when
\(P_N(w)\ne0\). No estimate for that term is being used.

The pole cancellation is explicit:
\[
 \begin{split}
 (c_0+A_N(t)+C_N(t))d_N(t)&=a_N(t),\\
 A_N(t)d_N(t-2\theta)&=b_N(t),\\
 C_N(t)d_N(t+2\theta)&=b_N(-t).
 \end{split}
 \tag{41}
\]
For the first equality use (25) and
\(\sin(t-\theta)\sin(t+\theta)
=(\cos\theta-\cos t)(\cos\theta+\cos t)\).
For the second equality, the factors \(\sin t\) and
\(\sin(t-\theta)\) cancel literally; the third is its
reflection. Hence
\[
 \begin{split}
 (\mathcal L_n-w)(d_N\cos kt)
  ={}&(a_N-wd_N)\cos kt\\
  &-q^n\{b_N(t)e^{-int}\cos(k(t-2\theta))
          +b_N(-t)e^{int}\cos(k(t+2\theta))\}.
 \end{split}
 \tag{42}
\]
Pair the reflected terms before applying the trace. The
expression on the second line becomes
\(\sum_r b_r\{q^{-2k}\cos((k+r-n)t)
+q^{2k}\cos((k-r+n)t)\}\).
The first line uses the evenness of \(a_N,d_N\).
This proves (38), including at the apparent coefficient poles
by the original full-jet continuation.

Finally direct multiplication in (37) gives
\(b_4=-q^{-9}/16\) and \(b_{-4}=-q^9/16\).
For \(n>0\), the two extreme terms come only from \(r=-4\);
for \(n<0\), they come only from \(r=4\).
This proves (39). \(\square\)

The recurrence has a quantitative, but presently coarse,
transport estimate. If \(\|\cdot\|_{\ell^1}\) denotes the
sum of the absolute Fourier coefficients, then
\[
 \|d_N\|_{\ell^1}\le1,\qquad
 \|a_N\|_{\ell^1}\le8,\qquad
 \|b_N\|_{\ell^1}\le4.
 \tag{43}
\]
Each shifted sine has coefficient sum one, while
\(4\cos^4((t-\theta)/2)\) has coefficient sum four.
Thus the sum of the absolute coefficients in (38) is at most
\(16+|w|\), uniformly in \(N,k\).
For a vector \(\mathbf Z_k\) of \(2R\) consecutive observations,
(39) consequently yields both
\[
 \|\mathbf Z_{k+1}\|_\infty\le
      16(16+|w|)\|\mathbf Z_k\|_\infty,\qquad
 \|\mathbf Z_k\|_\infty\le
      16(16+|w|)\|\mathbf Z_{k+1}\|_\infty .
 \tag{44}
\]
The loss over order \(N\) steps is exponential. In particular
(44) does not turn the small-charge asymptotic into a sharp
lower bound at \(k=0\).

There is also a direct geometric interpretation of the leading
equation. Let \(k/N\to1-\chi\), keep \(n,w\) fixed, and insert
the local ratio \(Z_{k+s}/Z_k=e^{ist}\) in the leading
coefficients of (38). Away from \(\sin t=0\), its characteristic
equation is
\[
          w=2+4\cot^2(t/2)
                         \sin^2(nt/2-\pi\chi).
 \tag{45}
\]
For a free angle \(u\), write \(w=-2\cos u\). The original
one-edge critical equation is
\[
 \operatorname{arsinh}(\tan(t/2)\cos(u/2))
                         =int/2-i\pi\chi .
 \tag{46}
\]
Squaring its hyperbolic sine gives precisely (45).
Equation (45) has forgotten the selected logarithmic lift;
that lift remains part of (46). Conversely the recurrence
does not choose one root of (45) merely by satisfying it.
This is a Fourier-dual quantum equation for the actual
charge family, with its geometric characteristic verified
directly. A sharp connection estimate, respecting
\(Z_k=Z_{-k}\) and the original finite data, remains necessary.

The [finite checker](../experiments/check_fourier_charge_recurrence.py)
constructs the coefficients in (37) by Laurent multiplication,
and computes (36) independently from the original Newton
crossing and turn matrices. It compares (38) at unrestricted
free colors and their first normals, including charges beyond
one period, signed powers, and both level parities. Its
[saved output](../repro/results/research-fourier-charge-recurrence.json)
is a normalization check; the all-level recurrence is proved
by (40)--(42).

## 11. Centered ordering and the degree of a real clearing factor

Centering the two charge shifts is an exact operation, but it does not
make (38) Hermitian. The obstruction can be described for every real
even trigonometric clearing factor, rather than only the choice (37).

Let \(d(t)\) be a nonzero real even trigonometric polynomial for which
\[
 a_d(t)=(c_0+A_N(t)+C_N(t))d(t),\qquad
 b_d(t)=A_N(t)d(t-2\theta)
\]
are trigonometric polynomials. On bilateral charge sequences define
\((Ef)_k=f_{k+1}\) and \((Qf)_k=q^{2k}f_k\). Thus
\(EQ=q^2QE\), \(E^*=E^{-1}\), and \(Q^*=Q^{-1}\) for the
ordinary counting inner product. The associated charge operator is
\[
 \mathcal P_d=a_d(E)-wd(E)
   -q^n\left[Q^{-1}b_d(E)E^{-n}
                         +Qb_d(E^{-1})E^n\right].
 \tag{47}
\]
Here \(w\) is real when Hermitian symmetry is discussed.
The notation \(p(E)\) means substitution in the finite Laurent
expansion of \(p(t)\).

**Lemma 5.** For \(N\ge3\), the operator (47) is Hermitian if and
only if
\(b_d(t+\theta)=b_d(-t+\theta)\). A nonzero clearing factor
with this property has degree at least \(N-1\).

*Proof.* Use the literal square roots
\((Q^{1/2}f)_k=q^kf_k\). The two terms in (47) have the exact
centered form
\[
 \begin{split}
 q^nQ^{-1}b_d(E)E^{-n}
   &=Q^{-1/2}b_d(qE)E^{-n}Q^{-1/2},\\
 q^nQb_d(E^{-1})E^n
   &=Q^{1/2}b_d(qE^{-1})E^nQ^{1/2}.
 \end{split}
 \tag{48}
\]
Since \(b_d\) is real on the real circle, \(b_d(qE)\) is
Hermitian. The first line's adjoint therefore agrees with the
second line exactly when
\(b_d(qE)=b_d(qE^{-1})\).
The diagonal term \(a_d(E)-wd(E)\) is Hermitian as well.
Conversely, the coefficients of \(Q\) and \(Q^{-1}\) are
independent functions of the integer index for \(N\ge3\).
Comparison of these coefficients in \(\mathcal P_d\) and its
adjoint gives the same necessary condition. This argument is
on the bilateral sequence space, so there are no discarded
finite-interval endpoint terms.

The condition is elementary in the angular variable:
\[
 \begin{split}
 b_d(t+\theta)
   &=\frac{4\cos^4(t/2)}
          {\sin(t+\theta)\sin t}\,d(t-\theta),\\
 b_d(-t+\theta)
   &=\frac{4\cos^4(t/2)}
          {\sin(t-\theta)\sin t}\,d(t+\theta).
 \end{split}
 \tag{49}
\]
Equality away from the displayed zeros, and then continuation,
is equivalent to
\[
 f(t- \theta)=f(t+\theta),\qquad
 f(t)=d(t)\sin t,\qquad
 \deg f=\deg d+1.
 \tag{50}
\]
The polynomial \(f\) is odd and has period \(2\pi/N\).
Every nonzero frequency is therefore an integer multiple of
\(N\), proving \(\deg f\ge N\).
At the minimum degree, \(f\) is a constant multiple of
\(\sin Nt\), and \(d\) is a constant multiple of
\(U_{N-1}(\cos t)=\sin Nt/\sin t\). \(\square\)

For the multiplier (37), the centered coefficient is
\[
 b_N(t+\theta)=4\cos^4(t/2)
                         \sin(t-2\theta)\sin(t-3\theta),
\]
which is not generally even. Merely rewriting its shifts in
the centered order (48) does not remove this asymmetry.

The minimum-degree multiplier in Lemma 5 vanishes at every
double physical value, including \(c_0\); it is not an invertible
weight on the original Newton quotient. The lemma excludes
an exactly Hermitian bilateral charge equation obtained by a
uniformly bounded-degree real scalar clearing factor. It does
not exclude a positive form on the actual finite solution
space, a matrix-valued change of variables, or a nonlocal
boundary construction. In particular it is not a lower-bound
obstruction for the original quantum source.

## 12. The physical charge equation has two channels

The formal recurrence (38) has order \(2(|n|+4)\). Most of
its formal solutions are not original charge observations.
Imposing the full physical charge relations reduces its
solution space to dimension two. One of these two channels
is the source; the other comes from the multiplier used to
clear the poles.

Call a sequence physical if
\[
 Z_{-k}=Z_k,\qquad Z_{k+N}+Z_{k-N}=2\eta Z_k
                         \quad(k\in\mathbb Z).
 \tag{51}
\]
The second identity retains the confluent normal: shifting it
once gives the second difference
\(Z_{k+2N}-2\eta Z_{k+N}+Z_k=0\).
Every physical sequence has a unique representation
\[
               Z_k=\phi_N(F\,T_k(-z/2)),\qquad F\in\mathcal A_N .
 \tag{52}
\]
Indeed the polynomials \(T_0(-z/2),\ldots,T_{N-1}(-z/2)\)
form a basis. Their product identity shows that (51) is
exactly the condition that their associated linear functional
annihilate the ideal generated by
\(T_N(-z/2)-\eta=(-1)^NP_N(z)/2\).
The nondegenerate original Frobenius pairing then gives (52).

**Proposition 6.** For every \(N\ge2\), every integer \(n\),
and every free \(w\), the physical sequences satisfying (38)
form a two-dimensional space. In the representation (52)
this space is
\[
 \mathscr S_{n,N}(w)=
 \{F:d_N(z)(\mathcal L_{-n}-w)F=0\},\qquad
 d_N(z)=\frac{(z^2-4\cos^2\theta)(z^2-4\cos^2 2\theta)}{16}.
 \tag{53}
\]
Within it the additional condition
\[
                (\mathcal L_{-n}-w)F\in\mathbb C e_D
 \tag{54}
\]
defines a one-dimensional space, for every \(w\). Its unique
element with \(F(c_0)=\kappa^n\) is
\[
 F_0(w,z)=R(z)^nK_N(z,w),\qquad
 (\mathcal L_{-n}-w)F_0
                  =-\frac{\eta\kappa^n}{N^2}P_N(w)e_D.
 \tag{55}
\]
Thus (54) retains the actual endpoint support instead of
selecting a solution by a preferred asymptotic.

*Proof.* The bilinear adjoint of \(\mathcal L_n-w\) is
\(\mathcal L_{-n}-w\). Equations (40)--(42), the spanning
property of the Chebyshev polynomials, and nondegeneracy of
\(\phi_N\) show that (38) is equivalent to (53).

The greatest common divisor of \(d_N\) and \(P_N\) has degree
two. For even \(N\ge4\) its roots are \(c_0,-c_0\), each
simple in \(d_N\). For odd \(N\ge5\) they are
\(c_0,-2\cos 2\theta\), again simple. At \(N=2,3\) these
two common roots coalesce, and the common factor is
\((z-c_0)^2\). Consequently
\(\ker m_{d_N}\) has dimension two at every level and contains
\(e_D\).

If \(P_N(w)\ne0\), the operator
\(\mathcal L_{-n}-w\) is invertible, since it is conjugate
to multiplication by \(z-w\). This proves both dimension
claims in this case. The physical spectrum requires a
separate check. If \(P_N(w)=0\), that operator has a
one-dimensional kernel, including at a repeated root of
\(P_N\). Its bilinear left kernel is spanned by
\[
                  R^{-n}K_N(\,\cdot\,,w).
 \tag{56}
\]
Its pairing with \(e_D\) equals
\((R^{-n}K_N(\,\cdot\,,w))(c_0)=\kappa^{-n}\ne0\).
Therefore \(e_D\) does not belong to the image of
\(\mathcal L_{-n}-w\). The intersection of that image
with \(\ker m_{d_N}\) has dimension one: it is the kernel
of a nonzero linear functional on a two-dimensional space.
Its inverse image has dimension \(1+1=2\).
Likewise the inverse image of \(\mathbb C e_D\) is just
the one-dimensional kernel.

Finally (55) is the original full kernel identity after
multiplication by \(R^n\), and \(K_N(c_0,w)=1\).
Thus \(F_0(c_0)=\kappa^n\ne0\), proving the normalization
and uniqueness at all free colors. \(\square\)

For \(N\ge4\), the extra channel has an explicit form.
Let
\[
 a=c_j,\quad j=\lfloor N/2\rfloor-1,\qquad
 E_a(z)=\frac{\eta P_N(z)}{N^2(z-a)} .
 \tag{57}
\]
This is the second common root in the preceding proof.
It satisfies \(\phi_N(E_af)=f(a)\).
Define an ordinary divided-difference polynomial and its
turned source by
\[
 B_a(w,z)=\frac{K_N(a,z)-K_N(a,w)}{z-w},\qquad
 F_1(w,z)=R(z)^n\,T[B_a(w,\cdot)](z).
 \tag{58}
\]
The quotient is polynomial also at \(z=w\); no resolvent
or choice of a pole prescription is involved. Its exact
equation is
\[
 \begin{split}
 (\mathcal L_{-n}-w)F_1
       &=R(a)^n E_a-\kappa^nK_N(a,w)e_D,\\
 F_1(c_0)&=0 .
 \end{split}
 \tag{59}
\]
To prove it, use
\((\mathcal L-w)T=T(m_z-w)\),
\(T K_N(a,\cdot)=E_a\), \(T1=e_D\), and
\(R^nE_a=R(a)^nE_a\).
Also \((TB_a)(c_0)=\phi_N(B_a)=0\), since
\(\deg B_a=j-1<D\); this proves the second line.
Since \(E_a,e_D\) are independent, the first line is
nonzero for every \(w\). Thus \(F_0,F_1\) form a basis
of (53) for every free color.

There is useful information about the location of this
extra channel in the original algebra. The
[physical-row formula](research_edge_kernel_difference_and_endpoint_bound.md#2-physical-rows-and-coalescing-shifts)
shows that \(K_N(a,z)\) has degree exactly \(j\).
Hence \(B_a\) has degree \(j-1\). In the Newton basis,
\[
 T B_a\in\operatorname{span}\{e_{D-j+1},\ldots,e_D\}
       =\operatorname{span}\{e_{L+2},\ldots,e_D\},
 \qquad L=D-\lfloor N/2\rfloor .
 \tag{60}
\]
These indices lie strictly in the original high Newton
radical. That ideal is preserved by multiplication by
every original signed crossing, so \(F_1\) belongs to it
as well. In particular all its physical values vanish;
its first normals remain present.
The coincident-root levels \(N=2,3\) are covered by
Proposition 6 but are not included in (57)--(60).

The same distinction is visible without choosing a Newton
basis. The
[full derivative-sampling identity](research_fourier_lower_bounds_and_almost_invariance.md#15-the-exact-finite-system-for-changing-a-fourier-charge)
gives, for any \(F\) in (52),
\[
 Z_{k+N}-\eta Z_k
       =-iN\sum_{a=0}^{N-1}e^{-ik\tau_a}
                              \sin\tau_a\,F(c_a).
 \tag{61}
\]
The charge observations of \(F_1\) therefore have the
ordinary signed period \(Z_{k+N}=\eta Z_k\).
Those of \(F_0\) do not: its endpoint value is
\(\kappa^n\), and the finite Fourier transform on the
displayed grid is invertible. Thus, for \(N\ge4\),
\(F_1\) is exactly the periodic line in the two-channel
space. The endpoint-supported condition (54) fixes the
original lift across this periodic line; the period
increment by itself would not fix that lift.

This identifies the second channel created by this
particular pole clearing. It does not bound its coefficient
in a proposed approximate solution. Nor does a
one-dimensional source line imply that the scalar
\(\phi_N(F_0)\) is large or nonzero: it is one observation
of that line. To use a positive or accretive boundary
problem for a lower bound, its norm and observation
estimates must respect (51), (54), and the original first
normals. The rank reduction alone supplies none of those
estimates.

### The quotient still carries the complete-edge norm

Removing the extra channel does not make the original physical
Hermite norm have the filled-volume rate. This can be checked
on an actual source whose asymptotic is already proved.

Fix a positive integer \(n\ge64\) and set \(w=-2\).
For \(N\ge4\), use the two sources \(F_0,F_1\) in
(55), (58). Define
\[
 \|F\|_{\mathrm{jet},N}^2
  =\frac1N\sum_{a=0}^{N-1}
     \left\{|F(c_a)|^2+
       N^{-2}\left|
       \frac{d}{dt}F(-2\cos t)\bigg|_{t=\tau_a}
       \right|^2\right\},\qquad
 \|[F_0]\|_{\mathrm{quot},N}
       =\inf_{c\in\mathbb C}\|F_0+cF_1\|_{\mathrm{jet},N}.
 \tag{62}
\]
This is the normalized full angular-jet norm. At the odd
simple spectral root its angular derivative is automatically
zero; it does not prescribe an additional spectral normal.

**Proposition 7.** Put \(M_\infty=4G/\pi\). Along both
level parities,
\[
 \log\|[F_0]\|_{\mathrm{quot},N}
                         =NM_\infty+O_n(\log N).
 \tag{63}
\]
On the other hand the actual central observation satisfies
\[
 |\phi_N(F_0)|=\exp\{NM_n+O_n(\log N)\},\qquad
 \delta_n:=M_\infty-M_n>0 .
 \tag{64}
\]
Consequently
\[
 \frac{|\phi_N(F_0)|}{\|[F_0]\|_{\mathrm{quot},N}}
             =\exp\{-N\delta_n+O_n(\log N)\}.
 \tag{65}
\]
The numerator uses the original lift (54). The trace is
not being asserted to descend through the extra channel.

*Proof.* Let \(t_N=0\) for odd \(N\) and \(t_N=\pi/N\)
for even \(N\). The point \(z_N=-2\cos t_N\) is physical.
Every physical value of \(F_1\) is zero, whereas
\[
 |F_0(z_N)|=K_N(t_N,0)
       \ge cN^{-3/2}e^{NM_\infty}
\]
for all sufficiently large \(N\). Here the crossing has
unit-modulus physical values. The inequality is the
[proved full-kernel packet](research_bare_kernel_thin_rectangle.md)
at \(t_N,0\): its amplitude at zero is nonzero, and
evenness gives
\(\psi(t_N,0)=M_\infty+O(N^{-2})\).
The normalization \(1/N\) in (62) now yields
\[
       \|F_0+cF_1\|_{\mathrm{jet},N}
                 \ge cN^{-2}e^{NM_\infty}
                         \quad(c\in\mathbb C).
 \tag{66}
\]

For the upper bound choose \(c=0\). The
[real Newton bounds](research_three_crossing_real_period_newton_bound.md)
give
\(\sup_{t\in\mathbb R}|K_N(t,0)|
\le CN^A e^{NM_\infty}\).
Explicitly, the lower-half terms are bounded by
\(CN^A e^{2NV_0(j/N)}\), whose maximum rate is
\(2V_0(1/4)=M_\infty\); the high radical terms have
polynomial real-period bounds. Markov's inequality bounds
the spectral derivative of this degree-\(D\) polynomial
at polynomial additional cost. The exact Gaussian physical
jets of \(R^n\) have unit values and angular derivatives
\(O_n(N)\). Thus
\(\|F_0\|_{\mathrm{jet},N}\le C_nN^{A_n}e^{NM_\infty}\).
Together with (66), this proves (63).

The [signed long-path source theorem](research_uniform_path_trace_assembly.md)
applies to the one-edge path with one selected vertex
of power \(n\) and one complete endpoint. It identifies
the original scalar \(\phi_N(R^nK_N(\cdot,-2))\)
and gives its nonzero leading term at rate \(M_n\).
The positive charge branch on this path satisfies
\(\partial_\chi M(\chi)=-H(\chi)\),
\(M(0)=M_\infty\), and \(H(\chi)>0\) for
\(0<\chi\le1\), by the
[partial-charge theorem](research_positive_path_partial_charge_bounds.md).
Hence
\(\delta_n=\int_0^1H(\chi)\,d\chi>0\).
This proves (64), and (65) follows. \(\square\)

Equation (65) remains true with an \(o(N)\) change in its
exponent for any positive norm that is subexponentially
equivalent to the quotient norm in (62), with its scale
fixed by that comparison. It does not exclude a norm with
an explicit exponential geometric weight or a norm on
the selected complex contour. Such a form would need to
account for the filled action \(M_n\), as well as the
original observation. The positive real transfer for an
ordinary spectral tail does not supply that change of
norm: it controls a different state, before the signed
crossing trace.

## 13. An exact positive projection of the charge observations

The signed-periodic channel can be removed by an orthogonal projection
with norm one. This gives a positive identity for the complete charge
vector, while keeping separate the scalar observation \(Z_0\).

For the physical observations (52), form two consecutive blocks
\[
 A=(Z_0,\ldots,Z_{N-1}),\qquad
 B=(Z_N,\ldots,Z_{2N-1}),\qquad
 \Pi_\eta(A,B)=\frac12(A-\eta B,\ B-\eta A).
 \tag{67}
\]
Use the unnormalized Euclidean norm on these \(2N\) entries.
The map \(\Pi_\eta\) is the orthogonal projection onto the
subspace \(B=-\eta A\). In particular it annihilates every
signed-periodic block, including the extra channel \(F_1\).
It is a projection of a finite block; no assertion is made
that its output extends to a solution of (38).

**Proposition 8.** For every \(F\in\mathcal A_N\), the exact
projection norm is
\[
 \|\Pi_\eta Z(F)\|_2^2
     =\frac12\sum_{k=0}^{N-1}|Z_{k+N}-\eta Z_k|^2
     =\frac{N^3}{2}\sum_{a=0}^{N-1}
                       \sin^2\tau_a\,|F(c_a)|^2.
 \tag{68}
\]
Consequently the original source satisfies
\[
 \|\Pi_\eta Z(F_0)\|_2^2
       =\frac{N^3}{2}\sum_{a=0}^{N-1}
                    \sin^2\tau_a\,|K_N(c_a,w)|^2.
 \tag{69}
\]
This quantity is exactly independent of the integer crossing
power \(n\). At the complete free color \(w=-2\), there are
constants \(c,C>0\) such that, for all sufficiently large \(N\),
\[
 cN^{-1}e^{NM_\infty}
    \le\|\Pi_\eta Z(F_0)\|_2
    \le CN^{1/2}e^{NM_\infty},\qquad
 M_\infty=\frac{4G}{\pi}.
 \tag{70}
\]
These estimates hold through both level parities.

*Proof.* The first equality in (68) follows from (67).
Equation (61) expresses its difference vector as \(-iN\)
times the unnormalized discrete Fourier transform of
\((\sin\tau_a F(c_a))_a\). The grid has spacing \(2\pi/N\),
so its Fourier matrix has squared norm factor \(N\).
Parseval's exact finite identity proves the second equality.
The physical values of every signed integer crossing power
have modulus one. Substitution of \(F_0=R^nK_N(\cdot,w)\)
therefore proves (69).

For the lower bound in (70), choose a nonzero physical angle
\(t_N=\pi/N\) when \(N\) is even and \(t_N=2\pi/N\) when
\(N\) is odd. In the latter case the simple angle zero
contributes nothing to (68), so the adjacent physical node
is necessary. The
[uniform original kernel theorem](research_bare_kernel_thin_rectangle.md)
gives
\[
 K_N(t_N,0)
   =N^{-3/2}\bigl(\tfrac14+O(N^{-1})\bigr)
                    e^{NM_\infty+O(N^{-1})}.
\]
Here evenness and holomorphy give
\(\psi(t_N,0)=M_\infty+O(N^{-2})\).
Also \(|\sin t_N|\ge c/N\).
Retaining this one term of the positive sum (69) proves the
lower bound.

For the upper bound, fold each physical root to its index
\(j\le\lfloor(N-1)/2\rfloor\). Its Newton row terminates:
\(e_r(c_j)=0\) for \(r>j\). For \(r\le j\), all defining
factors are nonnegative and
\(0\le e_r(c_j)\le e_r(-2)\). It follows directly that
\[
 0\le K_N(c_j,-2)
       \le\sum_{r=0}^{N-1}e_r(-2)^2
       =K_N(-2,-2).
\]
The same kernel theorem bounds the last expression by
\(CN^{-3/2}e^{NM_\infty}\). There are \(N\) terms in (69),
and \(\sin^2\tau_a\le1\). This proves the upper bound.
\(\square\)

Since \(\Pi_\eta\) is a contraction, (70) is also a genuine
lower bound for the full \(2N\)-component charge vector.
It does not give a lower bound for its uninserted entry.
For example, at the actual integer power \(n=0\),
\[
 Z_0=\phi_N(K_N(\cdot,-2))=e_D(-2)
   =\begin{cases}
      0,&N\ \text{odd},\\[1mm]
      \displaystyle\frac{4}{N^2(2+c_0)},&N\ \text{even}.
     \end{cases}
 \tag{71}
\]
The last formula uses \(S_D=N\) and the exact polynomial
\(P_N\); it is not an asymptotic example. Thus the projected
norm has exponential rate \(M_\infty\) even when this original
scalar entry is zero or polynomially small. The preceding
subsection gives the corresponding strict rate loss for
fixed positive powers with nonzero geometric packets.

The projection removes the additional channel in a bounded,
explicit way. Recovering the endpoint-supported lift and
estimating its specified scalar observation remain separate
operations; Parseval alone does not control their cancellation.
