# An exact turn-trace formula for the original closing functional

Research note, 3 November 2026.

The original closing functional is an ordinary matrix trace with one
actual quarter-turn and a specified invertible density. This retains
every first normal at the repeated spectral roots. The density has
polynomially bounded physical jets and a polynomial bound on its
canonical representative along the whole real boundary. Nevertheless,
it is exponentially small at the central spectral nodes. Its natural
meromorphic representative has poles approaching the endpoint nodes.

Thus a trace representation exists, but its density is part of the
exponential action. It cannot be replaced by a positive rank or by
a nonzero scalar of subexponential size.

## 1. The algebra and the ordinary multiplication trace

Fix \(N\ge2\), put \(D=N-1\), \(\eta=(-1)^D\), and set
\[
 P_N(z)=2T_N(z/2)+2,\quad A_N=\mathbb C[z]/(P_N),\quad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f.       \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial. The original Newton basis
and quarter-turn are
\[
 \begin{split}
 c_j&=2\cos((2j+1)\pi/N),\\
 s_j&=2\sin(\pi j/N),\qquad S_i=\prod_{j=1}^i s_j,\\
 e_i(z)&=S_i^{-2}\prod_{j=0}^{i-1}(c_j-z),\qquad
 T e_i=e_{D-i}.
 \end{split}                                             \tag{2}
\]
Empty products are one. The original finite calculus proves
\[
                 \phi_N(e_i e_j)=\delta_{i+j,D}.           \tag{3}
\]
Write \(m_f\) for multiplication by \(f\) on \(A_N\), and use
\(\operatorname{Tr}\) for the ordinary vector-space trace.
The previously proved complete-circle identity says
\[
 \operatorname{Tr}(m_f)=\phi_N(E_N f),\qquad
 E_N=\frac{P_N'}{\eta N^2}=\frac{L_N}{N}
     =\sum_{i=0}^D e_i e_{D-i}.                           \tag{4}
\]
The last equality also follows by taking the trace in the dual bases
in (3). An ordinary multiplication trace inserts the complete circle
\(L_N/N\); it is not the physical closure \(\phi_N\). The last sum in
(4) is usually called the Euler, or handle, element of a Frobenius
algebra. The specific trace identity (4) is already proved in
[the finite Newton calculus](../papers/newton-calculus/finite.tex),
in the circle-trace equation.

There is a direct obstruction to dropping this distinction:
\[
                    e_D^2=0,\qquad \phi_N(e_D)=1.          \tag{5}
\]
For any finite-dimensional representation \(\rho\) of \(A_N\) and an
operator \(C\) commuting with its image, \(\rho(e_D)C\) is nilpotent.
Its trace is zero. The same holds for the supertrace of an even
operator on a finite-dimensional graded representation. Neither
kind of commuting-insertion trace can equal \(\phi_N\) on every
original spectator.

## 2. A turn gives an exact trace representation

Define the literal real polynomial
\[
             B_N(z)=\sum_{i=0}^D e_i(z)^2=K_N(z,z),       \tag{6}
\]
where \(K_N(z,w)=\sum_i e_i(z)e_i(w)\) is the original turn kernel.
Here \(B_N\) has degree \(2D\), before reduction. Since \(e_0=1\),
\[
                       B_N(x)\ge1\quad(x\in\mathbb R).    \tag{7}
\]
All roots of \(P_N\) are real, so \(B_N\) is a unit in \(A_N\).
Let \(b_N\) be its inverse, with canonical representative of degree
at most \(D\).

**Theorem 1.** For every \(f\in A_N\),
\[
 \boxed{\quad
 \operatorname{Tr}(T m_f)=\phi_N(B_N f),\qquad
 \phi_N(f)=\operatorname{Tr}(T m_{b_N f}).
 \quad}                                                   \tag{8}
\]
These are also identities with unreduced free-boundary polynomials
as coefficients.

**Proof.** Write \(f e_i=\sum_j a_{ji}e_j\). Equation (3) gives
\(a_{ji}=\phi_N(f e_i e_{D-j})\). The \(i\)-th diagonal entry of
\(T m_f\) is \(a_{D-i,i}=\phi_N(f e_i^2)\). Sum over \(i\);
then apply \(B_Nb_N=1\) in the full algebra. This includes the
first normals at every double root. \(\square\)

The turn is not an algebra homomorphism and does not commute with
all multiplication operators. Thus (8) does not contradict (5).
For a compiled source with \(m\) contracted algebra copies, it gives
\[
 \phi_N^{\otimes m}(F)=
 \operatorname{Tr}_{A_N^{\otimes m}}
 \left[T^{\otimes m}
 m_{\left(\prod_{v=1}^m b_N(z_v)\right)F}\right].             \tag{9}
\]
The numerator \(F\) retains every original signed crossing, turn
kernel and free-boundary factor. Products in the multiplication
operator use the original tensor-product quotient. Formula (9)
does not replace the state or choose a different closing functional.

## 3. Physical jets and the whole real boundary

Every distinct physical root is \(c_j\) with
\(0\le j\le\lfloor D/2\rfloor\). At this root, \(e_i(c_j)>0\)
for \(i\le j\), whereas \(e_i(c_j)=0\) for \(i>j\). Hence
\[
 \begin{split}
 B_N(c_j)&=\sum_{i=0}^j e_i(c_j)^2\ge1,\\
 B_N'(c_j)&=-2\sum_{i=0}^j e_i(c_j)^2
                    \sum_{k=0}^{i-1}\frac1{c_k-c_j}.
 \end{split}                                             \tag{10}
\]
The squares of the vanishing factors have zero first derivative,
so this calculation omits no first normal.
For \(k<j\),
\[
 c_k-c_j=
 4\sin\frac{(j+k+1)\pi}{N}\sin\frac{(j-k)\pi}{N}
          \ge\frac{16(j-k)^2}{N^2}.                       \tag{11}
\]
Indeed \(j-k\le N/2\), and both \(j+k+1\) and \(N-j-k-1\)
are at least \(j-k\); apply the elementary sine chord bound.
Using \(\sum_{r\ge1}r^{-2}<2\) in (10) proves
\[
          0\le-\frac{B_N'(c_j)}{B_N(c_j)}\le N^2/4.        \tag{12}
\]
At every double root the canonical inverse consequently satisfies
\[
              0<b_N(c_j)\le1,\qquad
              0\le b_N'(c_j)\le N^2/4.                   \tag{13}
\]
At the odd simple root only the value is prescribed by the quotient.
The derivative of the literal reciprocal \(1/B_N\) satisfies the
same bound there, but the canonical inverse need not share it.

Put \(g_N(t)=b_N(-2\cos t)\). This is an even trigonometric polynomial
of degree at most \(D\). At the physical angles
\(\tau_j=\pi(D-2j)/N\), (13) gives
\[
           |g_N(\tau_j)|\le1,\qquad
           |g_N'(\tau_j)|\le N^2/2.                      \tag{14}
\]
At the odd simple angle zero, the latter derivative is automatically
zero, irrespective of the unconstrained spectral derivative.
For \(g_N=\sum_{|k|<N}\gamma_ke^{ikt}\), set
\[
 V_k=N^{-1}\sum_jg_N(\tau_j)e^{-ik\tau_j},\qquad
 W_k=(iN)^{-1}\sum_jg_N'(\tau_j)e^{-ik\tau_j}.
\]
The exact two-alias Hermite equations give
\(\gamma_0=V_0\) and
\(\gamma_k=(1-k/N)V_k+W_k/N\) for \(1\le k<N\).
Thus
\[
 |\gamma_0|\le1,\quad |\gamma_k|\le1+N/2,\quad
 \boxed{\ \sup_{t\in\mathbb R}|b_N(-2\cos t)|
                         \le N^2+N-1.\ }                \tag{15}
\]
This is a bound for the canonical polynomial on the whole real
boundary, not a uniform estimate in a fixed complex strip.

## 4. The trace density is indefinite

In the Newton basis the matrix of \(T\) is the reversal matrix \(J\).
Equation (3) implies
\[
                     M_f^{\mathsf t}J=JM_f.              \tag{16}
\]
All physical values of \(b_N\) are positive. Real Hermite
interpolation therefore constructs a real unit \(a_N\in A_N\)
with \(a_N^2=b_N\): take the positive square root at each root
and its derivative at each double root. Hence the matrix density
in (8) is real symmetric:
\[
 Tm_{b_N}=JM_{b_N}=M_{a_N}^{\mathsf t}JM_{a_N}.             \tag{17}
\]
Its signature is exactly
\[
              \left(\left\lceil N/2\right\rceil,
                    \left\lfloor N/2\right\rfloor\right). \tag{18}
\]
It is invertible but indefinite, and its trace is \(\phi_N(1)=0\).
The exact trace in (8) is therefore not a positive weighted dimension
of spectral summands. This concerns the explicit matrix density;
it does not prohibit a different derived or microlocal construction.

## 5. The central density has an exponential rate

Let \(t_N=0\) at odd levels and \(t_N=\pi/N\) at even levels.
These are physical angles, so exactly
\[
                  b_N(-2\cos t_N)=K_N(t_N,t_N)^{-1}.      \tag{19}
\]
The established full edge asymptotic, uniform near \((0,0)\), is
\[
 K_N(t,u)=N^{-3/2}a(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
 \qquad a(0,0)=1/4,\quad \psi(0,0)=M_\infty=v_{\rm oct}/\pi.
                                                               \tag{20}
\]
Separate evenness gives \(\psi(t_N,t_N)=M_\infty+O(N^{-2})\).
Thus, at both parities,
\[
 \boxed{\quad b_N(-2\cos t_N)
        =4N^{3/2}e^{-NM_\infty}(1+O(N^{-1})).\quad}       \tag{21}
\]
An algebraic unit with polynomial upper bounds such as (13),(15)
does not supply a subexponential lower bound.

On a sufficiently small fixed complex disk about \(t=0\), the
same edge theorem makes the literal diagonal kernel nonzero and gives
\[
 \frac1{B_N(-2\cos t)}
 =N^{3/2}a(t,t)^{-1}e^{-N\psi(t,t)}(1+O(N^{-1})).          \tag{22}
\]
This statement concerns the literal reciprocal. It does not identify
the canonical polynomial \(b_N(-2\cos t)\) with (22) off the
physical nodes. The two functions have the same required physical
jets and different off-node continuations.

## 6. Poles of the literal reciprocal approach the endpoint

For \(1\le i<N\), direct differentiation of (2) gives
\[
                       e_i'(c_0)=\frac{(-1)^i}{s_1s_i}.  \tag{23}
\]
Use \(c_0-c_k=s_ks_{k+1}\) for \(1\le k<i\) and cancel
the factorials. Since \(e_i(c_0)=0\) for \(i>0\),
\[
 B_N(c_0)=1,\quad B_N'(c_0)=0,\quad
 B_N''(c_0)=\frac2{s_1^2}\sum_{i=1}^{N-1}s_i^{-2}
                        =\frac{N^2-1}{6s_1^2}.          \tag{24}
\]
For completeness, the last sum follows by differentiating twice
at zero the logarithm of the finite sine product
\[
 \prod_{k=1}^{N-1}
 \frac{\sin(x+k\pi/N)}{\sin(k\pi/N)}
                     =\frac{\sin(Nx)}{N\sin x}.          \tag{25}
\]
Let \(\rho_1,\ldots,\rho_{2D}\) be all complex zeros of the literal
polynomial \(B_N\), counted with multiplicity. Logarithmic
differentiation at \(c_0\) gives
\[
              B_N''(c_0)=-\sum_{\nu=1}^{2D}
                                     (c_0-\rho_\nu)^{-2}. \tag{26}
\]
If all zeros were farther than \(r\), the absolute value would be
at most \(2D/r^2\). It follows that at least one zero satisfies
\[
 |\rho_\nu-c_0|\le s_1\sqrt{\frac{12}{N+1}}
              \le\frac{2\pi}{N}\sqrt{\frac{12}{N+1}}.     \tag{27}
\]
There are no real zeros by (7), so these are genuine complex poles
of \(1/B_N\). This literal reciprocal has no common fixed
holomorphic neighborhood of the whole real spectral interval.
The canonical quotient inverse is a polynomial and has no poles;
using that representative instead retains its interpolation aliases.

## 7. The remaining localization problem

Equation (9) is an exact turn-trace representation for arbitrary
fixed signed Conway compositions. It is a possible starting point
for a semiclassical trace calculation and requires no graph-pullback
interpretation of \(T\).

On the spectral residue diagonal its mechanism is precisely
\[
                              B_N B_N^{-1}=1.            \tag{28}
\]
If the literal reciprocal is used near each spectral root, its
poles cancel in this complete diagonal product. They are not extra
singularities of the original trace. They do matter if the kernel
and density are separated and their contours are changed independently.
On the central chart, (22) cancels the entire diagonal turn action
in (20), including its exponential size and its \(N^{-3/2}\)
prefactor. Keeping only the algebraic nonzero status of the density
would lose that cancellation.

An actual fixed-point or critical-residue theorem must therefore
retain this density and prove the passage from the finite spectral
residue to the geometric critical summand. The finite trace formula
does not compute the original geometric intersection coefficient.
In particular it does not imply stability under every fixed short
partial filling, or a finite-exception theorem.

The relevant previous obstructions remain:
[the compact-source calculation](actual_compact_trace_and_lefschetz_obstruction.md)
rules out a bounded-branch exact graph-pullback description of the
original crossing; [the dualizing-residue construction](research_actual_source_dualizing_residue.md)
retains all generic spectral weights but does not identify them with
action-normalized geometric coefficients.

## 8. Attribution and reproduction

The Euler-element identity is standard Frobenius-algebra terminology;
see Moore and Segal,
[*D-branes and K-theory in 2D topological field theory*, Section 2](https://people.math.harvard.edu/~dafr/M392C-2012/Readings/MS.pdf).
Its concrete specialization (4) is prior work in this repository.
The calculations added here are the turn-trace density (8), its
physical and real-boundary bounds, the signature (18), and the
explicit endpoint-pole estimate (27). They are proved directly from
the original finite algebra.

The central estimate uses the full original edge theorem at both
parities, including its omitted-wire estimates.

Run
~~~sh
python3 experiments/check_turn_trace_residue_density.py \
  --precision 120 \
  --output repro/results/research-turn-trace-residue-density.json
~~~
The [script](../experiments/check_turn_trace_residue_density.py)
uses monic polynomial division in the power basis to construct all
multiplication matrices. It checks (8), the full quotient inverse,
every prescribed physical normal, the two-alias reconstruction,
the signature, and (24) at \(N=2,\ldots,12\). It also compares the
two different off-node representatives explicitly and records six
larger-level central normalization diagnostics. The
[saved results](../repro/results/research-turn-trace-residue-density.json)
are finite checks; the bounds and asymptotic assertions are proved
above rather than inferred from these records.

A [150-digit run](../repro/results/research-turn-trace-residue-density-root.json)
repeats the eleven full-quotient levels and the six central diagnostics
using the same monic-division construction.
