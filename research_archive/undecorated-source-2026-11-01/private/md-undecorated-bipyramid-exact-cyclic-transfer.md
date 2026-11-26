# The actual bipyramidal source as a cyclic polynomial transfer

This is a finite source identity, not a volume estimate. It applies to the opposite-offset matching on an even bipyramidal white sphere. It retains one common south-pole variable, every equatorial face demand, the original source polynomials and their spectral parameters. In particular it does not identify this diagram with a circle-operation tree or replace it by a product of scalar Newton edge kernels.

## 1. The original ordered source

Let \(m\ge6\) be even. The white vertices are \(N,S,z_j\), with \(j\) taken modulo \(m\). The oriented triangles are
\[
 (N,z_j,z_{j+1}),\qquad (S,z_{j+1},z_j).
 \tag{1}
\]
Match north spokes \(Nz_j\) for odd \(j\), and south spokes \(Sz_j\) for even \(j\). Mark the original nonmatching side \(Nz_0\). Thus the protected variables are \(N=z_0=0\), while \(S,z_1,\ldots,z_{m-1}\) all retain target \(d=n-1\) at quantum level \(n\). The lowercase \(n\) in this note is the quantum level, not a braid power.

The orientation-preserving local source factors, before the protected specialization, are
\[
 F_j=
 \begin{cases}
 H_{f_j}(N,z_{j-1},z_{j+1},z_j),&j\text{ odd},\\
 H_{f_j}(S,z_{j+1},z_{j-1},z_j),&j\text{ even}.
 \end{cases}
 \tag{2}
\]
Here the two middle arguments are in their original input/output order. Each \(f_j\) may be a full physical polynomial coupon, including \(R^{a_j}\), or the cleared full resolvent used to retain every root normal. The source is
\[
 [S^d z_1^d\cdots z_{m-1}^d]\,
 \left.\prod_{j=0}^{m-1}F_j\right|_{N=z_0=0}.
 \tag{3}
\]
The common mark, pivot and component/framing factors are exactly those in the general Morse source theorem. Formula (3) is its homogeneous marked coefficient, not a new invariant normalization.

Specialize \(N=0\), but for now leave \(z_0\) formal and impose its target zero. Write
\[
 F_j=\sum_{a,b,c\ge0} h_j(a,b,c;S)\,
                  z_{j-1}^{a}z_j^{b}z_{j+1}^{c}.
 \tag{4}
\]
For odd \(j\), the coefficient is independent of \(S\) and is zero unless \(a+b+c=d\). For even \(j\), it is a scalar multiple of \(S^{d-a-b-c}\), and is zero unless \(a+b+c\le d\). These statements are exact homogeneity, not a bound on physical matrix norms.

## 2. A transfer with two pending degrees

Set the original equatorial targets
\[
 t_0=0,\qquad t_j=d\quad(1\le j<m).
 \tag{5}
\]
Use states \((u,v)\in\{0,\ldots,d\}^2\). Define the polynomial matrix
\[
 \mathsf T_j(S)_{(u,v),(u',v')}
 =
 h_j(t_{j-1}-u,\ u'-v,\ v';S),
 \tag{6}
\]
with a coefficient declared zero if any displayed exponent is negative or outside its actual local support. Then
\[
 \boxed{\quad
 \text{the source in (3)}
   =[S^d]\operatorname{tr}
       \bigl(\mathsf T_0(S)\mathsf T_1(S)\cdots
                         \mathsf T_{m-1}(S)\bigr).
 \quad}
 \tag{7}
\]
This matrix has \((d+1)^2\) states. Its entries are exact local face coefficients. It is generally signed or complex, and is not asserted to be positive or uniformly conditioned.

For the proof, a monomial selection in (4) gives triples \((a_j,b_j,c_j)\). The target on \(z_{j-1}\) is
\[
 c_{j-2}+b_{j-1}+a_j=t_{j-1}.
 \tag{8}
\]
Just before row \(j\), set
\[
 u_j=c_{j-2}+b_{j-1},\qquad v_j=c_{j-1}.
 \tag{9}
\]
Then (8) fixes \(a_j=t_{j-1}-u_j\), and the next state is
\[
 (u_{j+1},v_{j+1})=(v_j+b_j,c_j).
 \tag{10}
\]
These are exactly (6). Every feasible monomial gives one closed state sequence, and conversely every nonzero term in the trace gives one feasible monomial. The states are determined by that monomial, so there is no extra multiplicity. Nonnegative degrees and the targets imply all states lie in the stated range. Finally \([S^d]\) retains the one original south-pole demand; it cannot be replaced by a product of separate south-pole estimates.

In fact homogeneity makes that last demand automatic once all the equatorial demands are enforced. Every selected local monomial has degree \(d\), their total degree is \(md\), and the prescribed equatorial degree is \((m-1)d\). Therefore
\[
 \operatorname{tr}\prod_j\mathsf T_j(S)
       =S^d\operatorname{tr}\prod_j\mathsf T_j(1).
 \tag{7a}
\]
Thus the exact source is also the numerical matrix trace at the single common gauge \(S=1\). This uses the one shared homogeneous coefficient, not independent south-pole choices at the even rows.

The same construction works for any fixed genuine CROSS/LEFT/RIGHT assignment by projecting each original \(h_j\) to its exact path support before forming (6). It also works for the unsplit full-minus-CROSS difference, by subtracting the two complete traces. No projection is called a covariant coupon.

There is an exact grading that may be useful for estimating the transfer. Let \(\ell(u,v)=u+v\). At an ordinary-target step, homogeneity gives
\[
 \ell(u',v')=\ell(u,v)-p,
 \tag{7b}
\]
where \(p\) is the local \(S\)-degree. Thus every odd row other than the marked-target step preserves \(\ell\), and each even row lowers it by its actual south-pole degree. At row \(j=1\), where the previous face is the protected \(z_0\), the nonzero conditions force \(u=0\) and
\[
 \ell(u',v')=d+\ell(u,v).
 \tag{7c}
\]
There is precisely one such increase. The total decrease around a closed state path is \(d\), agreeing with (7a). This grading does not take absolute values and does not alter the local coefficient phases.

## 3. Why this is not yet a uniform source estimate

The common south-pole demand couples the even rows; (7a) enforces it by total degree. The cyclic trace still couples the pending degrees at the two ends of any cut. Taking separate operator norms of the \(\mathsf T_j\), or choosing independent local south-pole weights before the shared coefficient, removes these constraints.

The known finite filling-functional estimate means that a strict exponential bound on this original shared remainder would pass to the entire original fixed-power filling without an additional normal or Fourier-tail loss. It does not provide that shared bound. A concrete remaining algebraic target is therefore a signed estimate for (7), or for blocks of consecutive matrices with their two boundary states and their \(S\)-degree all retained, compared with the original positive endpoint source and its non-CROSS support gap.

For odd levels that comparator must use the actual regularized full endpoint numerator. Bare evaluation at \(-2\) omits its one-sided normal channels. The transfer (6) itself always uses the raw original coupon.

## 4. A root-safe two-row telescoping identity

There is a smaller signed identity which illustrates the needed kind of calculation. It comes from the aligned, rather than opposite-offset, bipyramidal incidence and is not claimed to solve (7).

Return to the usual quantum notation \(N\ge3\), \(d=N-1\), \(M=\lfloor N/2\rfloor-1\), \(\theta=\pi/N\). Define
\[
 \mathcal B_N(\sigma)=
 [c^dy^d]\,
 H_{V,\mathrm L}(0,0,c,y;\sigma)\,
 H_{V,\mathrm C}(0,c,0,y;-2).
 \tag{11}
\]
The common \(y\)-demand is extracted before taking a bound. The other two pair-boundary loads are zero. This extraction differs from the earlier cap/CROSS all-demand theorem, which extracts the overloaded cap face; its stated coefficient range cannot simply be relabeled as (11).

Put \(c_r=2\cos((2r+1)\theta)\), \(s_r=2\sin(r\theta)\), and
\[
 b_k(\sigma)=
 \left(\prod_{r=1}^k s_r^2\right)
 \left(\prod_{r=k+1}^{d}(\sigma-c_r)\right),\qquad
 B_k=
 \left(\prod_{r=0}^{k-1}(2+c_r)\right)
 \left(\prod_{r=k+1}^{d}s_r^2\right).
 \tag{12}
\]
The full original path formula gives
\[
 \mathcal B_N(\sigma)=(-1)^d
                 \sum_{k=0}^{M}(-1)^k b_k(\sigma)B_k.
 \tag{13}
\]
All unused rows remain in these products. Let \(T_k=b_kB_k\) and \(D_k=(\sigma-c_k)T_k\). The polynomial recurrence, without division at any node, is
\[
 (\sigma-c_{k+1})T_{k+1}=(2+c_k)T_k,\qquad
 D_k+D_{k+1}=(\sigma+2)T_k.
 \tag{14}
\]
Consequently the exact finite telescope is
\[
 (\sigma+2)(-1)^d\mathcal B_N(\sigma)
       =D_0+(-1)^M D_{M+1}.
 \tag{15}
\]
It retains both endpoints.

For \(N=2m\), put \(P_m(\sigma)=2T_m(\sigma/2)\), where \(T_m\) is the ordinary Chebyshev polynomial. The two half node lists coincide,
\[
 \chi_N=P_m^2,\qquad
 \prod_{r=0}^{m-1}(2+c_r)=2.
 \tag{16}
\]
Using \(\prod_{r=1}^{d}s_r^2=N^2\) in the two endpoint terms yields
\[
 \boxed{\quad
 \mathcal B_N(\sigma)=
 -N^2\,\frac{P_m(\sigma)
          [P_m(\sigma)+2(-1)^{m-1}]}{\sigma+2}.
 \quad}
 \tag{17}
\]
The numerator vanishes at \(-2\), so (17) is a polynomial identity there as well. In particular
\[
 \mathcal B_N(2)=-N^2[1-(-1)^m].
 \tag{18}
\]
Thus the coefficient vanishes for \(4\mid N\), and equals \(-2N^2\) for \(N\equiv2\pmod4\).

For \(N=2m+1\), put \(P_m=U_m(\sigma/2)-U_{m-1}(\sigma/2)\). Then
\[
 \chi_N=(\sigma+2)P_m^2,\qquad
 \prod_{r=0}^{m-1}(2+c_r)=N,
 \tag{19}
\]
and the same telescope gives
\[
 \boxed{\quad
 \mathcal B_N(\sigma)=
 N^2P_m(\sigma)[P_m(\sigma)+(-1)^{m-1}N].
 \quad}
 \tag{20}
\]
This keeps the raw odd numerator and its original central cutoff; no regularizer was substituted into (11).

These identities imply a polynomial real-spectral bound at both parities. For even \(N\), the elementary Chebyshev bound \(|P_m|\le2\), together with \(|P_m'|\le m^2\) and its endpoint value, bounds the removable quotient in (17). For odd \(N\), \(|U_j(\sigma/2)|\le j+1\) on \([-2,2]\), so \(|P_m|\le N\). In particular
\[
 \sup_{\sigma\in[-2,2]}|\mathcal B_N(\sigma)|\le2N^4.
 \tag{21}
\]
This is only the explicit boundary specialization (11). Restoring the other boundary degrees and a second varying spectral parameter is an additional problem. Equations (17) and (20) do not permit those degrees to be dropped when sewing the full bipyramidal source.

The comparison with the fractional-flow local obstruction is useful: at \(\sigma=2\) the positive absolute summands in (13) have an exponential lower bound, while their signed sum has the exact polynomial values (18), (20). The cancellation follows from the original finite recurrence and endpoint currents, not a choice of geometric saddle.
